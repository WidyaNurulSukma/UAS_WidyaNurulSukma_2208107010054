# 📝 Intelligent Email Writer for Students

Aplikasi berbasis Web yang memungkinkan mahasiswa membuat email secara otomatis dan profesional dengan bantuan teknologi Large Language Model (LLM) dari Google Gemini API.

## 📦 Fitur Utama

* **Multi-kategori Email**: Akademik, Skripsi, Magang, dll.
* **Pilihan Gaya Penulisan**: formal, netral, atau santai.
* **Dukungan Dua Bahasa**: Bahasa Indonesia dan Inggris.
* **Komponen Poin Utama**: Masukkan poin-poin utama yang ingin disampaikan dalam email.
* **Contoh Email**: Opsi untuk menggunakan email sebelumnya sebagai referensi.
* **Hasil Profesional**: Menghasilkan email yang profesional, jelas, dan padat secara otomatis.

## 📷 Pratinjau Aplikasi

![image](https://github.com/user-attachments/assets/85ee0ec0-af66-45c8-bc60-95ed5c6f8685)

## Hasil Generate Email

![image](https://github.com/user-attachments/assets/4cc9b341-e6ce-4862-862a-1c4c548d5eb3)4

**Subjek: Permohonan Izin Tidak Dapat Menghadiri Perkuliahan**

**Yth. Bapak/Ibu [Gelar Dosen] [Nama Dosen],**

Dengan hormat,

Melalui email ini, saya, Widya, mahasiswa [Program Studi] [Angkatan] dengan ini bermaksud memohon izin untuk tidak dapat menghadiri perkuliahan [Nama Mata Kuliah] selama 3 (tiga) hari, terhitung mulai tanggal [Tanggal Mulai] hingga [Tanggal Selesai], dikarenakan [Alasan singkat dan jelas, contoh: sakit/keperluan keluarga/dll. Jika alasan sensitif, bisa disebutkan "ada keperluan mendesak"].

Saya menyadari pentingnya kehadiran dalam perkuliahan dan saya akan berusaha semaksimal mungkin untuk mengejar materi yang tertinggal, baik secara mandiri maupun dengan berdiskusi dengan teman sekelas. Apabila diperlukan, saya siap untuk memberikan surat keterangan atau bukti pendukung lainnya.

Atas perhatian dan izin yang Bapak/Ibu berikan, saya mengucapkan terima kasih.

Hormat saya,

Widya
[NIM]

[Nomor Telepon (opsional)]


## 📁 Struktur Proyek

```
intelligent\_email\_writer/
├── .env                     # Berisi API Key Gemini
├── app.py                  # Frontend dengan Streamlit
├── backend/
│   └── main.py             # Backend API menggunakan FastAPI
├── requirements.txt        # Dependensi backend
├── requirements\_frontend.txt # Dependensi frontend (opsional)

```

## ⚙️ Instalasi dan Menjalankan Proyek

### 1. Kloning Repository

```bash
git clone https://github.com/WidyaNurulSukma/UAS_WidyaNurulSukma_2208107010054.git
cd UAS_WidyaNurulSukma_2208107010054
```

### 2. Setup dan Jalankan Backend (FastAPI)

```bash
# Buat dan aktifkan environment
python3 -m venv env
source env/bin/activate   # Linux/macOS
# ATAU
env\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Setup API Key (salin dari .env.example)
cp .env.example .env
# Edit file .env dan masukkan API key Anda

# Jalankan server
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Setup dan Jalankan Frontend (Streamlit)

Buka terminal baru:

```bash
# Pastikan sudah berada di direktori project
# Aktifkan environment jika belum
source env/bin/activate   # Linux/macOS
# ATAU
env\Scripts\activate      # Windows

# Install dependensi frontend
pip install -r requirements_frontend.txt

# Jalankan aplikasi
streamlit run app.py
```

## 🔐 Mendapatkan API Key Gemini

1. Kunjungi [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Login dengan akun Google Anda
3. Klik Create API Key
4. Copy API key dan simpan ke dalam file `.env` di root project dengan format:

```
GEMINI_API_KEY=your_api_key_here
```

## 📬 Cara Penggunaan

1. Buka browser dan akses `http://localhost:8501`
2. Pilih kategori email dan gaya penulisan
3. Masukkan informasi penerima, subjek, dan poin-poin penting
4. Jika perlu, tambahkan contoh email sebelumnya sebagai referensi
5. Klik tombol "Buat Email"
6. Email hasil generate akan ditampilkan di halaman aplikasi
7. Anda dapat menyalin hasilnya dengan tombol "Salin ke Clipboard"

## 📋 API Endpoints

- `POST /generate/`: Endpoint utama untuk menghasilkan email
- `GET /health`: Endpoint untuk health check

## 🤝 Kontribusi

Proyek ini terbuka untuk kontribusi. Jika Anda memiliki ide untuk perbaikan atau fitur baru, silakan buat pull request atau issue.

## 📄 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 🙏 Acknowledgments

- Google Gemini API untuk teknologi AI
- Streamlit dan FastAPI untuk kerangka kerja pengembangan
- kontributor dan penguji



