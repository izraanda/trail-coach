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
# 2. MENU: CATAT LARI (6 JENIS LARI)
# ==========================================
elif menu == "Catat Lari":
  st.subheader("Catat Sesi Lari Berdasarkan Jenisnya")
  st.markdown("Pilih tab di bawah ini sesuai dengan jenis lari Anda:")

  tab_easy, tab_speed, tab_long, tab_trail = st.tabs(
      ["Easy & Recovery", "Tempo & Interval", "Long Run", "Trail Run"]
  )

  # --- TAB 1: EASY & RECOVERY RUN ---
  with tab_easy:
    st.markdown("### Catat Easy Run / Recovery Run")
    with st.form("form_easy_recovery"):
      tgl_er = st.date_input("Tanggal Latihan", datetime.date.today())
      jenis_er = st.selectbox(
          "Pilih Sub-Kategori", ["Easy Run", "Recovery Run"]
      )

      c1, c2 = st.columns(2)
      with c1:
        jarak_er = st.number_input(
            "Jarak (KM)", min_value=0.0, format="%.2f", value=8.0
        )
        durasi_er = st.number_input(
            "Durasi Moving Time (Menit)", min_value=1, value=45
        )
      with c2:
        elev_er = st.number_input(
            "Elevation Gain (Opsional, m+)", min_value=0, value=30
        )
        rpe_er = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=3
        )

      catatan_er = st.text_area(
          "Catatan Fisik / Kondisi Kaki",
          placeholder=(
              "Contoh: Kaki terasa segar, detak jantung stabil di Zona 2."
          ),
      )
      submit_er = st.form_submit_button("Simpan Easy/Recovery Run")

      if submit_er:
        new_data = {
            "Tanggal": str(tgl_er),
            "Kategori": jenis_er,
            "Jarak (KM)": jarak_er,
            "Durasi (Min)": durasi_er,
            "Elevation (m+)": elev_er,
            "RPE": rpe_er,
            "Catatan": catatan_er,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success(f"Berhasil menyimpan data {jenis_er}!")

  # --- TAB 2: TEMPO & INTERVAL ---
  with tab_speed:
    st.markdown("### Catat Tempo Run / Interval Run")
    with st.form("form_tempo_interval"):
      tgl_sp = st.date_input("Tanggal Latihan Speed", datetime.date.today())
      jenis_sp = st.selectbox(
          "Pilih Sub-Kategori", ["Tempo Run", "Interval Run"]
      )

      s1, s2 = st.columns(2)
      with s1:
        jarak_sp = st.number_input(
            "Total Jarak (KM)", min_value=0.0, format="%.2f", value=6.0
        )
        durasi_sp = st.number_input(
            "Durasi Total (Menit)", min_value=1, value=40
        )
      with s2:
        elev_sp = st.number_input(
            "Elevation Gain (Opsional, m+)", min_value=0, value=20
        )
        rpe_sp = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=8
        )

      catatan_sp = st.text_area(
          "Detail Menu & Catatan",
          placeholder=(
              "Contoh: 5 x 400m interval cepat dengan jog pemulihan."
          ),
      )
      submit_sp = st.form_submit_button("Simpan Speed Work")

      if submit_sp:
        new_data = {
            "Tanggal": str(tgl_sp),
            "Kategori": jenis_sp,
            "Jarak (KM)": jarak_sp,
            "Durasi (Min)": durasi_sp,
            "Elevation (m+)": elev_sp,
            "RPE": rpe_sp,
            "Catatan": catatan_sp,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success(f"Berhasil menyimpan data {jenis_sp}!")

  # --- TAB 3: LONG RUN ---
  with tab_long:
    st.markdown("### Catat Long Run (Lari Jarak Jauh)")
    with st.form("form_longrun"):
      tgl_lr = st.date_input("Tanggal Long Run", datetime.date.today())

      l1, l2 = st.columns(2)
      with l1:
        jarak_lr = st.number_input(
            "Jarak (KM)", min_value=0.0, format="%.2f", value=16.0
        )
        durasi_lr = st.number_input(
            "Durasi Moving Time (Menit)", min_value=1, value=120
        )
      with l2:
        elev_lr = st.number_input(
            "Elevation Gain (m+)", min_value=0, value=300
        )
        rpe_lr = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=6
        )

      catatan_lr = st.text_area(
          "Catatan Nutrisi & Fisik",
          placeholder="Contoh: Uji coba minum gel energi, kaki stabil.",
      )
      submit_lr = st.form_submit_button("Simpan Long Run")

      if submit_lr:
        new_data = {
            "Tanggal": str(tgl_lr),
            "Kategori": "Long Run",
            "Jarak (KM)": jarak_lr,
            "Durasi (Min)": durasi_lr,
            "Elevation (m+)": elev_lr,
            "RPE": rpe_lr,
            "Catatan": catatan_lr,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success("Berhasil menyimpan Long Run!")

  # --- TAB 4: TRAIL RUN ---
  with tab_trail:
    st.markdown("### Catat Trail Run (Lari Lintas Alam)")
    with st.form("form_trailrun"):
      tgl_tr = st.date_input("Tanggal Trail Run", datetime.date.today())

      tr1, tr2 = st.columns(2)
      with tr1:
        jarak_tr = st.number_input(
            "Jarak (KM)", min_value=0.0, format="%.2f", value=12.0
        )
        durasi_tr = st.number_input(
            "Durasi Moving Time (Menit)", min_value=1, value=150
        )
      with tr2:
        elev_tr = st.number_input(
            "Elevation Gain (Wajib, m+)", min_value=0, value=1200
        )
        rpe_tr = st.slider(
            "Tingkat Capek / RPE (1-10)", min_value=1, max_value=10, value=8
        )

      catatan_tr = st.text_area(
          "Catatan Jalur & Uji Coba Downhill",
          placeholder="Contoh: Power hiking di tanjakan ekstrem.",
      )
      submit_tr = st.form_submit_button("Simpan Trail Run")

      if submit_tr:
        new_data = {
            "Tanggal": str(tgl_tr),
            "Kategori": "Trail Run",
            "Jarak (KM)": jarak_tr,
            "Durasi (Min)": durasi_tr,
            "Elevation (m+)": elev_tr,
            "RPE": rpe_tr,
            "Catatan": catatan_tr,
        }
        st.session_state.df_lari = pd.concat(
            [st.session_state.df_lari, pd.DataFrame([new_data])],
            ignore_index=True,
        )
        st.success("Berhasil menyimpan Trail Run!")

# ==========================================
# 3. MENU: CATAT STRENGTH
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
# 4. MENU: REKAPITULASI
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
    st.metric(label="Total Sesi Lari", value=f"{total_sesi_lari} Sesi")
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
# 5. MENU: KALENDER RACE
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
