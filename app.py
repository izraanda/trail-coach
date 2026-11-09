import datetime
import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Trail Running Personal Coach", page_icon="🏃‍♂️", layout="wide"
)

# Judul Aplikasi
st.title("🏔️ Trail Running Personal Coach & Log")
st.markdown(
    "*Aplikasi pelacak latihan pribadi untuk persiapan MSR/DCR 2027, BDG100, & SLU.*"
)

# Sidebar Menu Navigasi
st.sidebar.header("Navigasi Menu")
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    [
        "📊 Dashboard Utama",
        "📝 Catat Lari (Workout Log)",
        "💪 Catat Strength (Tanpa Alat)",
        "🏁 Kalender & Target Race",
    ],
)

# ==========================================
# 1. MENU: DASHBOARD UTAMA
# ==========================================
if menu == "📊 Dashboard Utama":
  st.subheader("Ringkasan Musim Latih 2027")

  col1, col2, col3 = st.columns(3)
  with col1:
    st.metric(
        label="Target Race Terdekat",
        value="MSR / DCR",
        delta="Juni 2027 (~2300m+)",
    )
  with col2:
    st.metric(
        label="A-Race Utama", value="BDG100 (42K)", delta="September 2027"
    )
  with col3:
    st.metric(label="Race Penutup", value="SLU (30K/50K)", delta="Desember 2027")

  st.info(
      "💡 **Tips Coach:** Fokuskan bulan-bulan awal ini pada *Base Building* dan"
      " konsistensi latihan *strength* eksentrik untuk persiapan turunan curam"
      " (*downhill*)."
  )

# ==========================================
# 2. MENU: CATAT LARI (WORKOUT LOG)
# ==========================================
elif menu == "📝 Catat Lari (Workout Log)":
  st.subheader("Catat Sesi Lari / Trail Running")

  with st.form("form_lari"):
    tanggal_lari = st.date_input(
        "Tanggal Latihan", datetime.date.today()
    )
    jenis_lari = st.selectbox(
        "Kategori Latihan",
        ["Easy Run", "Long Run / Trail", "Interval / Tempo Run"],
    )

    col_a, col_b = st.columns(2)
    with col_a:
      jarak_km = st.number_input(
          "Jarak (KM)", min_value=0.0, format="%.2f", value=10.0
      )
      durasi_menit = st.number_input(
          "Durasi Moving Time (Menit)", min_value=1, value=60
      )
    with col_b:
      elevasi_gain = st.number_input(
          "Elevation Gain (Meter+)", min_value=0, value=500
      )
      rpe = st.slider(
          "Tingkat Capek / RPE (Skala 1-10)", min_value=1, max_value=10, value=5
      )

    catatan_kaki = st.text_area(
        "Catatan Kondisi Kaki / Fisik",
        placeholder="Contoh: Betis kanan agak tegang, perlu stretching ekstra.",
    )

    submit_lari = st.form_submit_button("Simpan Data Lari")

    if submit_lari:
      st.success(
          f"Berhasil menyimpan data {jenis_lari} sejauh {jarak_km} KM dengan"
          f" elevasi +{elevasi_gain}m!"
      )

# ==========================================
# 3. MENU: CATAT STRENGTH (TANPA ALAT)
# ==========================================
elif menu == "💪 Catat Strength (Tanpa Alat)":
  st.subheader("Catat Latihan Strength di Rumah")
  st.markdown("Pilih dan catat menu latihan sesuai jenis metriknya:")

  tanggal_str = st.date_input("Tanggal Strength", datetime.date.today())

  tab_waktu, tab_repetitif = st.tabs(
      ["⏱️ Berbasis Waktu (Durasi)", "🔢 Berbasis Repetitif (Hitungan)"]
  )

  with tab_waktu:
    st.markdown("### Latihan Berbasis Waktu")
    plank = st.checkbox("Plank (Target: 3 Set x 45-60 detik)")
    side_plank = st.checkbox(
        "Side Plank (Target: 3 Set x 30-45 detik per sisi)"
    )
    durasi_total_waktu = st.number_input(
        "Estimasi Durasi Total Sesi Waktu (Menit)", min_value=1, value=15
    )

  with tab_repetitif:
    st.markdown("### Latihan Repetitif (Kaki, Core, & Stabilitas)")
    bulgarian = st.checkbox(
        "Bulgarian Split Squat (Target: 3 Set x 10-12 reps/kaki)"
    )
    s_l_rdl = st.checkbox(
        "Single-Leg Romanian Deadlift (Target: 3 Set x 10 reps/kaki)"
    )
    calf_raises = st.checkbox("Calf Raises (Target: 3 Set x 20 reps)")
    lunges = st.checkbox("Walking Lunges (Target: 3 Set x 16 langkah)")
    glute_bridge = st.checkbox("Glute Bridges (Target: 3 Set x 15 reps)")
    bird_dog = st.checkbox("Bird-Dog (Target: 3 Set x 10 reps/sisi)")
    durasi_total_rep = st.number_input(
        "Estimasi Durasi Total Sesi Repetitif (Menit)", min_value=1, value=20
    )

  catatan_strength = st.text_area(
      "Catatan Strength",
      placeholder="Contoh: Otot paha terasa kuat, keseimbangan membaik.",
  )

  if st.button("Simpan Data Strength"):
    st.success("Data latihan strength harian berhasil dicatat!")

# ==========================================
# 4. MENU: KALENDER & TARGET RACE
# ==========================================
elif menu == "🏁 Kalender & Target Race":
  st.subheader("Jadwal Target Race Musim 2027")

  st.markdown("""
    * **Race 1 (Juni 2027):** MSR 20K (Elevasi 2.290m+) ATAU DCR 25K (Elevasi 2.330m+)
    * **Race 2 / A-Race (September 2027):** BDG100 Kategori 42K *(Puncak Target Musim Ini)*
    * **Race 3 (Desember 2027):** SLU Kategori 30K atau 50K *(Ditentukan berdasarkan hasil evaluasi pasca BDG100)*
    """)

  st.info(
      "🔍 **Decision Matrix SLU:** Modul evaluasi otomatis akan aktif setelah"
      " Anda menginput data hasil *finish* dan pemulihan dari BDG100 di bulan"
      " September 2027."
  )
