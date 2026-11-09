# ==========================================
# 2. MENU: CATAT LARI (DIPISAH 6 JENIS LARI)
# ==========================================
elif menu == "📝 Catat Lari (Workout Log)":
  st.subheader("📝 Catat Sesi Lari Berdasarkan Jenisnya")
  st.markdown("Pilih tab di bawah ini sesuai dengan jenis lari yang Anda lakukan:")

  tab_easy, tab_speed, tab_long, tab_trail = st.tabs(
      [
          "🟢 Easy & Recovery Run",
          "⚡ Tempo & Interval",
          "🏃‍♂️ Long Run",
          "⛰️ Trail Run",
      ]
  )

  # --- TAB 1: EASY & RECOVERY RUN ---
  with tab_easy:
    st.markdown("### Catat Easy Run / Recovery Run")
    st.markdown(
        "*Intensitas rendah/sangat rendah untuk pemulihan dan bangun"
        " aerobik.*"
    )

    with st.form("form_easy_recovery"):
      tgl_er = st.date_input("Tanggal Latihan", datetime.date.today())
      jenis_er = st.selectbox(
          "Pilih Sub-Kategori", ["Easy Run (Lari Santai)", "Recovery Run"]
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
      submit_er = st.form_submit_button("Simpan Data Easy/Recovery Run")

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
    st.markdown("*Latihan kecepatan, VO2Max, dan ambang batas laktat.*")

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
              "Contoh: 5 x 400m interval cepat dengan jog pemulihan di"
              " antaranya."
          ),
      )
      submit_sp = st.form_submit_button("Simpan Data Speed Work")

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
    st.markdown("*Fokus pada ketahanan (endurance) jarak/waktu di akhir pekan.*")

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
          placeholder=(
              "Contoh: Uji coba minum 2 gel energi, kaki terasa stabil sampai"
              " kilometer ke-14."
          ),
      )
      submit_lr = st.form_submit_button("Simpan Data Long Run")

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
        st.success("Berhasil menyimpan data Long Run!")

  # --- TAB 4: TRAIL RUN ---
  with tab_trail:
    st.markdown("### Catat Trail Run (Lari Lintas Alam)")
    st.markdown(
        "*Sesi spesifik elevasi tinggi untuk persiapan MSR/DCR & BDG100.*"
    )

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
          placeholder=(
              "Contoh: Latihan power hiking di tanjakan ekstrem, paha depan"
              " terasa lelah saat turunan."
          ),
      )
      submit_tr = st.form_submit_button("Simpan Data Trail Run")

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
        st.success("Berhasil menyimpan data Trail Run!")
 