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
# 2. MENU: CATAT LARI (DIPISAH BERDASARKAN JENIS)
# ==========================================
elif menu == "📝 Catat Lari (Workout Log)":
  st.subheader("📝 Catat Sesi Lari Berdasarkan Kategori")
  st.markdown(
      "Pilih tab di bawah ini sesuai dengan jenis sesi lari yang baru saja"
      " Anda lakukan:"
  )

  tab_easy, tab_interval, tab_trail = st.tabs(
      [
          "🟢 Easy Run / Recovery",
          "⚡ Interval / Tempo",
          "⛰️ Long Run / Trail Run (Elevasi)",
      ]
  )

  # --- TAB 1: EASY RUN ---
  with tab_easy:
    st.markdown("### Catat Easy / Recovery Run")
    with st.form("form_easy_run"):
      tgl_easy = st.date_input("Tanggal Easy Run", datetime.date.today())
      c_col1, c_col2 = st.columns(2)
      with c_col1:
        jarak_easy = st.number_input(
            "Jarak (KM)", min_value=0.0, format="%.2f", value=8.0
        )
        durasi_easy = st.number_input(
            "Durasi Moving Time (Menit)", min_value=1, value=45
        )
      with c_col2:
        elev_easy = st.number_input(
            "Elevation Gain (Opsional, m+)", min_value=0, value=50
        )
        rpe_easy = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=3
        )
      catatan_easy = st.text_area(
          "Catatan Sesi Easy Run",
          placeholder="Contoh: Kaki terasa ringan, detak jantung stabil.",
      )
      submit_easy = st.form_submit_button("Simpan Data Easy Run")

      if submit_easy:
        new_data = {
            "Tanggal": str(tgl_easy),
            "Kategori": "Easy Run",
            "Jarak (KM)": jarak_easy,
            "Durasi (Min)": durasi_easy,
            "Elevation (m+)": elev_easy,
            "RPE": rpe_easy,
            "Catatan": catatan_easy,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success("Sesi Easy Run berhasil dicatat!")

  # --- TAB 2: INTERVAL / TEMPO ---
  with tab_interval:
    st.markdown("### Catat Interval / Tempo Run (Speed Work)")
    with st.form("form_interval"):
      tgl_inter = st.date_input("Tanggal Interval / Tempo", datetime.date.today())
      i_col1, i_col2 = st.columns(2)
      with i_col1:
        jarak_inter = st.number_input(
            "Total Jarak (KM)", min_value=0.0, format="%.2f", value=6.0
        )
        durasi_inter = st.number_input(
            "Durasi Total (Menit)", min_value=1, value=40
        )
      with i_col2:
        elev_inter = st.number_input(
            "Elevation Gain (Opsional, m+)", min_value=0, value=30
        )
        rpe_inter = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=8
        )
      catatan_inter = st.text_area(
          "Detail Menu Interval / Catatan",
          placeholder=(
              "Contoh: 5 x 400m repetisi cepat, napas terengah-engah tapi"
              " konsisten."
          ),
      )
      submit_inter = st.form_submit_button("Simpan Data Interval")

      if submit_inter:
        new_data = {
            "Tanggal": str(tgl_inter),
            "Kategori": "Interval / Tempo",
            "Jarak (KM)": jarak_inter,
            "Durasi (Min)": durasi_inter,
            "Elevation (m+)": elev_inter,
            "RPE": rpe_inter,
            "Catatan": catatan_inter,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success("Sesi Interval / Tempo berhasil dicatat!")

  # --- TAB 3: LONG RUN / TRAIL RUN ---
  with tab_trail:
    st.markdown("### Catat Long Run / Trail Run (Simulasi Elevasi)")
    st.markdown(
        "*Sesi utama untuk persiapan MSR/DCR dan BDG100 (Fokus elevasi &"
        " tanjakan).* "
    )
    with st.form("form_trail"):
      tgl_trail = st.date_input("Tanggal Trail Run", datetime.date.today())
      t_col1, t_col2 = st.columns(2)
      with t_col1:
        jarak_trail = st.number_input(
            "Total Jarak (KM)", min_value=0.0, format="%.2f", value=15.0
        )
        durasi_trail = st.number_input(
            "Durasi Moving Time (Menit)", min_value=1, value=150
        )
      with t_col2:
        elev_trail = st.number_input(
            "Elevation Gain (Wajib Diisi, m+)", min_value=0, value=1000
        )
        rpe_trail = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=7
        )
      catatan_trail = st.text_area(
          "Catatan Jalur & Kondisi Fisik",
          placeholder=(
              "Contoh: Latihan power hiking di tanjakan curam, uji coba gel"
              " energi."
          ),
      )
      submit_trail = st.form_submit_button("Simpan Data Trail Run")

      if submit_trail:
        new_data = {
            "Tanggal": str(tgl_trail),
            "Kategori": "Long Run / Trail",
            "Jarak (KM)": jarak_trail,
            "Durasi (Min)": durasi_trail,
            "Elevation (m+)": elev_trail,
            "RPE": rpe_trail,
            "Catatan": catatan_trail,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success("Sesi Long / Trail Run berhasil dicatat!")

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
