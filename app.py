import requests
import streamlit as st
from typing import List

API_URL = "http://localhost:8000/generate/"

st.set_page_config(
    page_title="Intelligent Email Writer", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Fungsi untuk menampilkan loading spinner saat menunggu response
def generate_with_spinner(payload):
    with st.spinner("Sedang membuat email... Harap tunggu"):
        try:
            # kirim request ke API
            response = requests.post(API_URL, json=payload, timeout=30)
            
            # cek status code
            response.raise_for_status()
            
            # ambil data dari response
            data = response.json()
            return data.get("generated_email", "– Tidak ada output –"), None
        except requests.exceptions.HTTPError as e:
            return None, f"Server Error {response.status_code}: {response.text}"
        except requests.exceptions.RequestException as e:
            return None, f"Gagal menghubungi server: {e}"

# Banner dan judul
st.title("📝 Intelligent Email Writer for Students")
st.markdown("""
    Aplikasi ini membantu mahasiswa membuat email profesional secara otomatis dengan bantuan AI.
    Cukup isi form berikut, dan email profesional akan dihasilkan dalam sekejap!
""")

# Gunakan container untuk styling yang lebih baik
with st.container():
    st.write("### 📋 Detail Email")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 1. kategori email
        category = st.selectbox(
            "Kategori Email",
            [
                "Akademik",
                "Bimbingan & Skripsi",
                "Magang / MBKM",
                "Beasiswa / Exchange",
                "Organisasi / Kepanitiaan",
                "Karier & Profesional",
                "Umum & Administratif"
            ]
        )
        
        # 3. subjek
        subject = st.text_input(
            "Subjek Email",
            placeholder="e.g., Permohonan Izin Tidak Hadir Kuliah"
        )
        
        # 5. bahasa
        language = st.selectbox(
            "Bahasa",
            ["Bahasa Indonesia", "Bahasa Inggris"]
        )
    
    with col2:
        # 2. penerima
        recipient = st.text_input(
            "Kepada",
            placeholder="e.g., Dosen Pembimbing, TU Fakultas, dst."
        )
        
        # 4. tone penulisan
        tone = st.selectbox(
            "Gaya/Tone Penulisan",
            ["Formal dan Sopan", "Santai namun Sopan", "Netral"]
        )
        
        # 6. tingkat urgensi (opsional)
        urgency = st.selectbox(
            "Tingkat Urgensi",
            ["Biasa", "Tinggi", "Rendah"]
        )

# 7. poin-poin utama (pisah baris baru)
st.write("### 📌 Konten Email")
points_input = st.text_area(
    "Poin-poin Utama Isi Email",
    placeholder="Tuliskan poin-poin penting, satu poin per baris",
    height=120
)
# ubah menjadi list
points = [p.strip() for p in points_input.split("\n") if p.strip()]

# 8. contoh email sebelumnya (opsional)
with st.expander("📩 Contoh Email Sebelumnya (Opsional)"):
    example = st.text_area(
        "Jika Anda memiliki contoh email sebelumnya, masukkan di sini untuk referensi",
        height=100
    )

# Tampilkan jumlah poin yang dimasukkan
if points:
    st.caption(f"✅ {len(points)} poin berhasil disiapkan")

# Tombol generate dengan warna dan ikon
generate_button = st.button("✉️ Buat Email", type="primary", use_container_width=True)

# Session state untuk menyimpan hasil
if "generated_email" not in st.session_state:
    st.session_state.generated_email = None

# generate email
if generate_button:
    if not (recipient and subject and points):
        st.error("Mohon isi paling tidak: Kepada, Subjek, dan Poin-poin isi email.")
    else:
        # susun payload
        payload = {
            "category": category,
            "recipient": recipient,
            "subject": subject,
            "tone": tone,
            "language": language,
            "urgency_level": urgency,
            "points": points,
            "example_email": example if example else None
        }

        # Proses pembuatan email dengan spinner
        email_result, error = generate_with_spinner(payload)
        
        if error:
            st.error(error)
        else:
            st.session_state.generated_email = email_result

# Tampilkan hasil jika ada
if st.session_state.generated_email:
    st.write("---")
    st.subheader("📄 Hasil Email")
    
    # Tambahkan opsi untuk menyalin ke clipboard
    st.code(st.session_state.generated_email, language="markdown")
    
    # Tombol untuk menyalin hasil
    st.download_button(
        label="📋 Salin ke Clipboard",
        data=st.session_state.generated_email,
        file_name="email.txt",
        mime="text/plain",
    )
    
    # Opsi reset
    if st.button("🔄 Buat Email Baru", type="secondary"):
        st.session_state.generated_email = None
        st.experimental_rerun()
        
# Footer
st.write("---")
st.caption("© 2023 Intelligent Email Writer | Dibuat dengan ❤️ untuk membantu mahasiswa")