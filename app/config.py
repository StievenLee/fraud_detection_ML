# ── Transaction types ─────────────────────────────────────────────────────────

TRANSACTION_TYPES = ["TRANSFER", "CASH_OUT", "PAYMENT", "CASH_IN"]

TYPE_INFO = {
    "TRANSFER" : "Perpindahan dana antar rekening",
    "CASH_OUT" : "Penarikan tunai",
    "PAYMENT"  : "Pembayaran ke merchant",
    "CASH_IN"  : "Setoran tunai",
}

# Types with highest fraud occurrence — triggers an info banner in the UI
FRAUD_RISK_TYPES = {"TRANSFER", "CASH_OUT"}