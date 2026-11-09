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
        "Dashboard Utama",
        "Rencana Minggu Ini",
        "Catat Lari",
        "Catat Strength",
        "Rekapitulasi",
        "Kalender Race",
    ],
)

# ==========================================
# 1. MENU: DASHBOARD UTAMA
# ==========================================
if menu == "Dashboard Utama":
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
# 2. MENU: RENCANA MINGGU INI (AI COACH EVALUATION)
# ==========================================
elif menu == "Rencana Minggu Ini":
  st.subheader("🤖 AI Coach: Evaluasi & Rencana Minggu Ini")
  st.markdown(
      "Menu ini menganalisis hasil latihan Anda sebelumnya dan memberikan"
      " rekomendasi porsi latihan untuk pekan ini."
  )

  # Analisis Data Sebelumnya secara Otomatis
  total_sesi = len(st.session_state.df_lari)

  if total_sesi > 0:
    avg_rpe = st.session_state.df_lari["RPE"].mean()
    total_elev_mingguan = st.session_state.df_lari["Elevation (m+)"].sum()

    st.success(
        f"📊 **Evaluasi Performa Terakhir:** Berdasarkan {total_sesi} sesi lari"
        f" yang tercatat, rata-rata tingkat kelelahan (RPE) Anda berada di angka"
        f" **{avg_rpe:.1f}/10** dengan total akumulasi elevasi **+{total_elev_mingguan} m**."
    )

    if avg_rpe > 7.5:
      st.warning(
          "⚠️ **Catatan AI Coach:** Rata-rata tingkat kelelahan (RPE) Anda"
          " cukup tinggi minggu lalu. Disarankan untuk memperbanyak *Easy Run*"
          " atau menambah hari istirahat (*Recovery*) minggu ini agar terhindar"
          " dari *overtraining*."
      )
    else:
      st.info(
          "✨ **Catatan AI Coach:** Beban latihan Anda terpantau stabil dan"
          " terkontrol. Minggu ini Anda siap meningkatkan sedikit volume"
          " *Trail Run* atau *Long Run*."
      )
  else:
    st.info(
        "ℹ️ Belum ada data latihan tercatat. Mulailah mencatat sesi lari Anda"
        " agar AI Coach dapat memberikan evaluasi yang dipersonalisasi!"
    )

  st.divider()

  st.markdown("### 📋 Jadwal Rekomendasi Mingguan (AI Recommendation)")
  st.markdown(
      "Berikut adalah panduan struktur latihan yang direkomendasikan untuk"
      " Anda minggu ini:"
  )

  st.markdown("""
    * **Senin:** 🛌 *Rest Day* / Istirahat Total (Pemulihan otot pasca akhir pekan).
    * **Selasa:** 💪 *Strength Training* Rumah (Fokus Kaki & Eksentrik: Bulgarian Split Squat, Calf Raises) + 🟢 *Easy Run* (6-8 KM).
    * **Rabu:** ⚡ *Tempo / Interval Run* (Melatih kapasitas VO2Max & kecepatan jelajah).
    * **Kamis:** 💪 *Strength Training* Rumah (Fokus Core & Stabilitas: Plank, Side Plank, Glute Bridges).
    * **Jumat:** 🛌 *Recovery Run* Sangat Santai atau Istirahat.
    * **Sabtu:** ⛰️ *Trail Run / Long Run* (Fokus simulasi elevasi dan *power hiking* untuk persiapan MSR/DCR).
    * **Minggu:** 🚶 *Active Recovery* / Jalan santai ringan.
    """)

# ==========================================
# 3. MENU: CATAT LARI
# ==========================================
elif menu == "Catat Lari":
  st.subheader("Catat Sesi Lari")
  st.markdown("Pilih jenis lari dan masukkan detail latihan Anda di bawah ini:")

  with st.form("form_catat_lari"):
    tgl_lari = st.date_input("Tanggal Latihan", datetime.date.today())

    jenis_lari = st.selectbox(
        "Pilih Jenis Lari",
        [
            "Easy Run",
            "Recovery Run",
            "Tempo Run",
            "Interval Run",
            "Long Run",
            "Trail Run",
        ],
    )

    col1, col2 = st.columns(2)
    with col1:
      jarak_lari = st.number_input(
          "Jarak (KM)", min_value=0.0, format="%.2f", value=10.0
      )
      durasi_lari = st.number_input(
          "Durasi Moving Time (Menit)", min_value=1, value=60
      )
    with col2:
      elev_lari = st.number_input(
          "Elevation Gain (m+)", min_value=0, value=100
      )
      rpe_lari = st.slider(
          "Tingkat Capek / RPE (Skala 1-10)", min_value=1, max_value=10, value=5
      )

    catatan_lari = st.text_area(
        "Catatan Latihan / Kondisi Kaki",
        placeholder=(
            "Contoh: Latihan stabil, fokus penjagaan detak jantung atau"
            " tanjakan."
        ),
    )

    submit_lari = st.form_submit_button("Simpan Data Lari")

    if submit_lari:
      new_data = {
          "Tanggal": str(tgl_lari),
          "Kategori": jenis_lari,
          "Jarak (KM)": jarak_lari,
          "Durasi (Min)": durasi_lari,
          "Elevation (m+)": elev_lari,
          "RPE": rpe_lari,
          "Catatan": catatan_lari,
      }
      st.session_state.df_lari = pd.concat(
          [st.session_state.df_lari, pd.DataFrame([new_data])],
          ignore_index=True,
      )
      st.success(f"Berhasil menyimpan data {jenis_lari}!")

# ==========================================
# 4. MENU: CATAT STRENGTH
# ==========================================
elif menu == "Catat Strength":
  st.subheader("Catat Latihan Strength di Rumah")
  tanggal_str = st.date_input("Tanggal Strength", datetime.date.today())

  tab_waktu, tab_repetitif = st.tabs(
      ["Berbasis Waktu (Durasi)", "Berbasis Repetitif (Hitungan)"]
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
      "Catatan Strength", placeholder="Contoh: Otot paha terasa kuat."
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
    st.success("Data latihan strength berhasil dicatat!")

# ==========================================
# 5. MENU: REKAPITULASI
# ==========================================
elif menu == "Rekapitulasi":
  st.subheader("Rekapitulasi Total Latihan")

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
    st.metric(label="Total Sesi Lari", value=f"{total_sesi_sessi_lari} Sesi" if 'total_sesi_sessi_lari' else f"{total_sesi_lari} Sesi")
  with col4:
    st.metric(label="Total Sesi Strength", value=f"{total_sesi_strength} Sesi")

  st.divider()

  st.markdown("### Riwayat Sesi Lari")
  if not st.session_state.df_lari.empty:
    st.dataframe(st.session_state.df_lari, use_container_width=True)
  else:
    st.info("Belum ada data lari.")

  st.markdown("### Riwayat Sesi Strength Rumah")
  if not st.session_state.df_strength.empty:
    st.dataframe(st.session_state.df_strength, use_container_width=True)
  else:
    st.info("Belum ada data strength.")

# ==========================================
# 6. MENU: KALENDER RACE
# ==========================================
elif menu == "Kalender Race":
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
