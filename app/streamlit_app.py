import streamlit as st
from predictor import FraudPredictor
from config import TRANSACTION_TYPES, TYPE_INFO, FRAUD_RISK_TYPES

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fraud Detection",
    page_icon="🛡️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .block-container { padding-top: 2rem; max-width: 700px; }

    .result-fraud {
        background: #fff1f0;
        border: 1.5px solid #ff4d4f;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        text-align: center;
    }
    .result-safe {
        background: #f6ffed;
        border: 1.5px solid #52c41a;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        text-align: center;
    }
    .result-title { font-size: 1.3rem; font-weight: 700; margin-bottom: 0.3rem; }
    .result-sub   { font-size: 0.9rem; opacity: 0.75; }

    .prob-bar-bg {
        background: #e8e8e8;
        border-radius: 99px;
        height: 10px;
        width: 100%;
        margin-top: 0.8rem;
    }
    .prob-bar-fill {
        height: 10px;
        border-radius: 99px;
        transition: width 0.5s ease;
    }

    .section-header {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        color: #8c8c8c;
        text-transform: uppercase;
        margin: 1.2rem 0 0.4rem;
    }
</style>
""", unsafe_allow_html=True)


# ── Model loading (cached) ────────────────────────────────────────────────────
@st.cache_resource
def load_predictor():
    return FraudPredictor()

predictor = load_predictor()


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 🛡️ Fraud Detection")
st.caption("Masukkan detail transaksi untuk mendeteksi potensi fraud.")
st.divider()


# ── Form ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">Tipe Transaksi</div>', unsafe_allow_html=True)

transaction_type = st.selectbox(
    "Tipe Transaksi",
    options=TRANSACTION_TYPES,
    format_func=lambda t: f"{t} — {TYPE_INFO[t]}",
    label_visibility="collapsed",
)

if transaction_type in FRAUD_RISK_TYPES:
    st.info(
        f"ℹ️ **{transaction_type}** adalah tipe transaksi yang paling sering "
        "ditemukan pada kasus fraud. Pastikan data diisi dengan benar.",
        icon=None,
    )

st.markdown('<div class="section-header">Detail Transaksi</div>', unsafe_allow_html=True)
amount = st.number_input(
    "Jumlah Transaksi (Amount)",
    min_value=0.0,
    value=1_000.0,
    step=100.0,
    format="%.2f",
    help="Nominal uang yang ditransaksikan.",
)

st.markdown('<div class="section-header">Saldo Pengirim</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    old_orig = st.number_input(
        "Saldo Sebelum (Old Balance Sender)",
        min_value=0.0,
        value=10_000.0,
        step=500.0,
        format="%.2f",
    )
with col2:
    new_orig = st.number_input(
        "Saldo Sesudah (New Balance Sender)",
        min_value=0.0,
        value=9_000.0,
        step=500.0,
        format="%.2f",
    )

st.markdown('<div class="section-header">Saldo Penerima</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    old_dest = st.number_input(
        "Saldo Sebelum (Old Balance Receiver)",
        min_value=0.0,
        value=0.0,
        step=500.0,
        format="%.2f",
    )
with col4:
    new_dest = st.number_input(
        "Saldo Sesudah (New Balance Receiver)",
        min_value=0.0,
        value=0.0,
        step=500.0,
        format="%.2f",
    )

st.divider()


# ── Predict ───────────────────────────────────────────────────────────────────
if st.button("🔍 Analisis Transaksi", use_container_width=True, type="primary"):

    with st.spinner("Menganalisis transaksi..."):
        input_data = {
            "type"          : transaction_type,
            "amount"        : amount,
            "oldbalanceOrg" : old_orig,
            "newbalanceOrig": new_orig,
            "oldbalanceDest": old_dest,
            "newbalanceDest": new_dest,
        }
        result     = predictor.predict(input_data)
        prediction = result["prediction"]
        fraud_prob = result["probability"]

    # ── Hasil ──
    st.markdown("### Hasil Analisis")

    if prediction == 1:
        st.markdown("""
        <div class="result-fraud">
            <div class="result-title" style="color:#cf1322;">🚨 Transaksi Terindikasi Fraud</div>
            <div class="result-sub">Sistem mendeteksi pola yang mencurigakan pada transaksi ini.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-safe">
            <div class="result-title" style="color:#389e0d;">✅ Transaksi Terlihat Normal</div>
            <div class="result-sub">Tidak ditemukan pola fraud yang signifikan.</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Probabilitas ──
    risk_label, risk_color = result["risk_label"], result["risk_color"]

    st.markdown(f"""
    <div style="margin-top:1rem;">
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;margin-bottom:4px;">
            <span>Probabilitas Fraud</span>
            <span style="font-weight:600;color:{risk_color};">{fraud_prob*100:.1f}% — {risk_label}</span>
        </div>
        <div class="prob-bar-bg">
            <div class="prob-bar-fill" style="width:{fraud_prob*100:.1f}%;background:{risk_color};"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Ringkasan Fitur ──
    balance_diff_orig = result["balance_diff_orig"]
    balance_diff_dest = result["balance_diff_dest"]

    st.markdown('<div class="section-header" style="margin-top:1.4rem;">Ringkasan Fitur</div>',
                unsafe_allow_html=True)

    m1, m2 = st.columns(2)
    m1.metric("Selisih Saldo Pengirim", f"{balance_diff_orig:,.0f}")
    m2.metric("Selisih Saldo Penerima", f"{balance_diff_dest:,.0f}")

    # ── Flags ──
    flags = result.get("flags", [])
    if flags:
        st.markdown('<div class="section-header">Pola Mencurigakan Terdeteksi</div>',
                    unsafe_allow_html=True)
        chips = "".join(
            f'<span style="display:inline-block;background:#fff1f0;border:1px solid #ffa39e;'
            f'border-radius:99px;padding:2px 12px;font-size:0.78rem;color:#cf1322;margin:2px;">⚑ {f}</span>'
            for f in flags
        )
        st.markdown(chips, unsafe_allow_html=True)

    # ── Rekomendasi ──
    st.markdown('<div class="section-header">Rekomendasi</div>', unsafe_allow_html=True)
    for rec in result["recommendations"]:
        st.markdown(f"- {rec}")

    st.caption(
        "⚠️ Hasil ini bersifat prediktif dan tidak menggantikan keputusan manusia. "
        "Selalu lakukan verifikasi manual untuk transaksi bernilai tinggi."
    )