import joblib
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.config import FRAUD_RISK_TYPES


class FraudPredictor:
    def __init__(self, model_path: str = "model/fraud_detection_pipeline.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, data: dict) -> dict:
        """
        Run inference on a single transaction and return a complete result dict
        (prediction, probability, risk level, derived features, flags, recommendations).

        Parameters
        ----------
        data : dict with keys:
               type, amount, oldbalanceOrg, newbalanceOrig,
               oldbalanceDest, newbalanceDest

        Returns
        -------
        dict with all fields needed by the UI — no logic required in streamlit_app.py.
        """
        df = pd.DataFrame([data])
        prediction  = int(self.model.predict(df)[0])
        probability = float(self.model.predict_proba(df)[0][1])

        # ── Risk level ────────────────────────────────────────────────────────
        risk_label, risk_color = self._risk_level(probability)

        # ── Derived features ──────────────────────────────────────────────────
        old_orig = data["oldbalanceOrg"]
        new_orig = data["newbalanceOrig"]
        old_dest = data["oldbalanceDest"]
        new_dest = data["newbalanceDest"]
        amount   = data["amount"]
        tx_type  = data["type"]

        balance_diff_orig = old_orig - new_orig
        balance_diff_dest = new_dest - old_dest

        # ── Flags ─────────────────────────────────────────────────────────────
        flags = []
        if balance_diff_orig >= old_orig * 0.95 and old_orig > 0:
            flags.append("Saldo pengirim terkuras hampir habis")
        if balance_diff_dest == 0 and amount > 0 and tx_type == "TRANSFER":
            flags.append("Penerima tidak mendapat dana")
        if tx_type in FRAUD_RISK_TYPES and new_orig == 0:
            flags.append("Saldo pengirim menjadi nol setelah transaksi")

        # ── Recommendations ───────────────────────────────────────────────────
        if prediction == 1:
            recommendations = [
                "Tahan transaksi dan lakukan verifikasi manual",
                "Hubungi nasabah untuk konfirmasi",
                "Catat kejadian untuk keperluan audit",
            ]
        else:
            recommendations = [
                "Transaksi dapat diproses",
                "Tetap pantau pola transaksi berikutnya",
            ]

        return {
            "prediction"       : prediction,
            "probability"      : probability,
            "risk_label"       : risk_label,
            "risk_color"       : risk_color,
            "balance_diff_orig": balance_diff_orig,
            "balance_diff_dest": balance_diff_dest,
            "flags"            : flags,
            "recommendations"  : recommendations,
        }

    # ── Private helpers ───────────────────────────────────────────────────────
    @staticmethod
    def _risk_level(prob: float) -> tuple[str, str]:
        if prob >= 0.75:
            return "Sangat Tinggi", "#ff4d4f"
        elif prob >= 0.50:
            return "Tinggi", "#fa8c16"
        elif prob >= 0.25:
            return "Sedang", "#fadb14"
        else:
            return "Rendah", "#52c41a"