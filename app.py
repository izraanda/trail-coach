import datetime
import pandas as pd
import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Trail Running Personal Coach", page_icon="🏃‍♂️", layout="wide"
)

# Inisialisasi Database Memori Sementara di Sesi
if "df_lari" not in st.session_state:
  st.session_state.df_lari = pd.DataFrame(
      columns=[
          "Tanggal",
          "Kategori",
          "Jarak (KM)",
          "Durasi (Min)",
          "Elevation (m+)",
          "RPE",
          "Catatan",
      ]
  )

if "df_strength" not in st.session_state:
  st.session_state.df_strength = pd.DataFrame(
      columns=[
          "Tanggal",
          "Jenis Sesi",
          "Menu Dilakukan",
          "Durasi (Min)",
          "Catatan",
      ]
  )

# Judul Aplikasi
st.title("🏔️ Trail Running Personal Coach & Log")
st.markdown(
    "*Aplikasi pelacak latihan pribadi untuk persiapan MSR/DCR 2027, BDG100, &"
    " SLU.*"
)

# Sidebar Menu Navigasi
st.sidebar.header("Navigasi Menu")
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    [
        "📊 Dashboard Utama",
        "📝 Catat Lari (Workout Log)",
        "💪 Catat Strength (Tanpa Alat)",
        "📈 Rekapitulasi & Riwayat",
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
      new_data = {
          "Tanggal": str(tanggal_lari),
          "Kategori": jenis_lari,
          "Jarak (KM)": jarak_km,
          "Durasi (Min)": durasi_menit,
          "Elevation (m+)": elevasi_gain,
          "RPE": rpe,
          "Catatan": catatan_kaki,
      }
      st.session_state.df_lari = pd.concat(
          [st.session_state.df_lari, pd.DataFrame([new_data])],
          ignore_index=True,
      )
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

  list_terpilih = []

  with tab_waktu:
    st.markdown("### Latihan Berbasis Waktu")
    p1 = st.checkbox("Plank (Target: 3 Set x 45-60 detik)")
    p2 = st.checkbox("Side Plank (Target: 3 Set x 30-45 detik per sisi)")
    if p1:
      list_terpilih.append("Plank")
    if p2:
      list_terpilih.append("Side Plank")
    durasi_total_waktu = st.number_input(
        "Estimasi Durasi Sesi Waktu (Menit)", min_value=1, value=15
    )

  with tab_repetitif:
    st.markdown("### Latihan Repetitif (Kaki, Core, & Stabilitas)")
    r1 = st.checkbox(
        "Bulgarian Split Squat (Target: 3 Set x 10-12 reps/kaki)"
    )
    r2 = st.checkbox(
        "Single-Leg Romanian Deadlift (Target: 3 Set x 10 reps/kaki)"
    )
    r3 = st.checkbox("Calf Raises (Target: 3 Set x 20 reps)")
    r4 = st.checkbox("Walking Lunges (Target: 3 Set x 16 langkah)")
    r5 = st.checkbox("Glute Bridges (Target: 3 Set x 15 reps)")
    r6 = st.checkbox("Bird-Dog (Target: 3 Set x 10 reps/sisi)")

    if r1:
      list_terpilih.append("Bulgarian Split Squat")
    if r2:
      list_terpilih.append("Single-Leg RDL")
    if r3:
      list_terpilih.append("Calf Raises")
    if r4:
      list_terpilih.append("Walking Lunges")
    if r5:
      list_terpilih.append("Glute Bridges")
    if r6:
      list_terpilih.append("Bird-Dog")

    durasi_total_rep = st.number_input(
        "Estimasi Durasi Sesi Repetitif (Menit)", min_value=1, value=20
    )

  catatan_strength = st.text_area(
      "Catatan Strength",
      placeholder="Contoh: Otot paha terasa kuat, keseimbangan membaik.",
  )

  if st.button("Simpan Data Strength"):
    total_durasi = durasi_total_waktu + durasi_total_rep
    menu_str = (
        ", ".join(list_terpilih) if list_terpilih else "Latihan Umum Selesai"
    )
    new_str_data = {
        "Tanggal": str(tanggal_str),
        "Jenis Sesi": "Bodyweight Strength",
        "Menu Dilakukan": menu_str,
        "Durasi (Min)": total_durasi,
        "Catatan": catatan_strength,
    }
    st.session_state.df_strength = pd.concat(
        [st.session_state.df_strength, pd.DataFrame([new_str_data])],
        ignore_index=True,
    )
    st.success("Data latihan strength harian berhasil dicatat!")

# ==========================================
# 4. MENU: REKAPITULASI & RIWAYAT
# ==========================================
elif menu == "📈 Rekapitulasi & Riwayat":
  st.subheader("📈 Rekapitulasi Total Latihan")

  # Ringkasan Angka (Metrik Total)
  total_jarak = (
      st.session_state.df_lari["Jarak (KM)"].sum()
      if not st.session_state.df_lari.empty
      else 0.0
  )
  total_elevasi = (
      st.session_state.df_lari["Elevation (m+)"].sum()
      if not st.session_state.df_lari.empty
      else 0
  )
  total_sesi_lari = len(st.session_state.df_lari)
  total_sesi_strength = len(st.session_state.df_strength)

  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.metric(label="Total Jarak Lari", value=f"{total_jarak:.2f} KM")
  with col2:
    st.metric(label="Total Elevation Gain", value=f"+{total_elevasi} m")
  with col3:
    st.metric(label="Total Sesi Lari", value=f"{total_sesi_lari} Sesi")
  with col4:
    st.metric(label="Total Sesi Strength", value=f"{total_sesi_strength} Sesi")

  st.divider()

  # Tabel Riwayat Lari
  st.markdown("### 🏃‍♂️ Riwayat Sesi Lari")
  if not st.session_state.df_lari.empty:
    st.dataframe(st.session_state.df_lari, use_container_width=True)
  else:
    st.info(
        "Belum ada data lari yang dicatat. Silakan isi di menu *Catat Lari*."
    )

  st.markdown("### 💪 Riwayat Sesi Strength Rumah")
  if not st.session_state.df_strength.empty:
    st.dataframe(st.session_state.df_strength, use_container_width=True)
  else:
    st.info(
        "Belum ada data strength yang dicatat. Silakan isi di menu *Catat"
        " Strength*."
    )

# ==========================================
# 5. MENU: KALENDER & TARGET RACE
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
