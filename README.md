# 🎓 COLLEST — Campus Event Platform

> **Tagline:** One Platform, Every Event Need.  
> **Brand Concept:** *Connect, Link, and Streamline*  
> **Mata Kuliah:** Algoritma & Dasar Pemrograman  

![COLLEST Brand Guide](app/static/images/collest-brand-guide.jpg)

COLLEST adalah platform digital kampus terintegrasi yang dirancang untuk mempermudah seluruh kebutuhan penyelenggaraan event mahasiswa dalam satu tempat: mulai dari rekrutmen panitia, pencarian vendor, perencanaan anggaran & Harga Tiket Masuk (HTM), jadwal rundown sekuensial, stand booth UMKM, hingga pendaftaran mitra vendor resmi.

---

## 🎨 1. Brand Identity & Design System

Aplikasi dibangun mengacu pada identitas visual resmi COLLEST:
- **Primary Blue (`#2F80ED`)**: Kepercayaan, inovasi, dan kemajuan (Warna dominan platform).
- **Accent Orange (`#FF8A3D`)**: Semangat, kreativitas, dan antusiasme (Aksen highlight & CTA).
- **Light Blue (`#E6F0FF`)**: Kesegaran, kebersihan, dan kemudahan antarmuka.
- **Dark Blue (`#0F2D5B`)**: Profesionalisme, fokus, dan stabilitas (Heading & teks utama).
- **White (`#FFFFFF`)**: Kesederhanaan dan keterbukaan (Background permukaan).

Logo resmi COLLEST berbentuk pita heksagonal isometrik huruf **"C"** dengan lipatan oranye di bagian bawah dan bintang berpendar di tengahnya, melambangkan sinergi dan keberhasilan penyelenggaraan acara kampus.

---

## 🚀 2. Fitur Utama Platform

### 📢 1. Event Recruitment
- Pencarian dan filter event kampus berdasarkan kategori, lokasi/kampus, dan status pendaftaran.
- Tampilan detail komprehensif: deskripsi acara, tujuan, penyelenggara, divisi, dan jobdesk spesifik per posisi.
- Transparansi hak & kewajiban: syarat pendaftaran, kuota yang tersisa secara *real-time*, serta rincian benefit dan honorarium (jika tidak ada honor, ditampilkan *"Belum diinformasikan"* tanpa janji palsu).
- Formulir pendaftaran terstruktur dengan validasi input, pencegahan duplikasi NIM pada event yang sama, serta penerbitan Kode Registrasi unik (`EVT-XXXXXX`) berstatus awal `submitted`.
- Menu **Pendaftaran Saya** untuk mahasiswa memantau status seleksi berkas.

### 🏪 2. Find Vendors
- Pencarian vendor terverifikasi kampus berdasarkan kategori (Katering, Sound System, Percetakan/Banner, Dekorasi, Dokumentasi, Merchandise, Logistik) dan batas anggaran.
- Model harga fleksibel:
  1. **Harga per unit** (contoh: Nasi Box Rp18.000/porsi).
  2. **Harga paket** (contoh: Paket Sound Seminar Rp1.800.000/hari).
  3. **Quotation Required** (jasa kustom tanpa manipulasi ke Rp 0 palsu).
- Tombol satu klik *"Pasang di Planner"* untuk memasukkan jasa vendor ke kalkulator anggaran.
- Formulir pengajuan penawaran (*Inquiry*) dengan status awal `inquiry_submitted`.

### 📊 3. Event Planner Workspace (Kalkulator HTM & Rundown)
- **Kalkulasi Biaya:** Pemisahan transparan antara biaya vendor, biaya operasional, dan komponen *quotation*.
- **Kalkulator Titik Impas HTM (Breakeven):** Rumus matematika pembagian total biaya dengan target peserta tiket berbayar (lengkap dengan proteksi pembagian nol).
- **Simulasi Profit / Margin:** Menghitung rekomendasi harga tiket berdasarkan target keuntungan persentase (%) dan pendapatan tambahan sponsor.
- **Sequential Rundown Generator:** Algoritma penyusunan jadwal waktu sekuensial otomatis berdasarkan jam mulai dan durasi aktivitas dalam menit.
- **Penyimpanan Draft:** Menyimpan seluruh rancangan rencana event ke database lokal SQLite.

### 🛍️ 4. UMKM & Event Booth
- Eksplorasi kesempatan membuka stand jualan di event kampus (stand berbayar maupun stand eksibisi gratis).
- Detail spesifikasi stand: ukuran booth, fasilitas (daya listrik, meja, lampu, Wi-Fi), target pengunjung, dan aturan tenant.
- **Kalkulator Kelayakan Usaha Booth:** Menghitung total modal (biaya sewa stand + modal produk/HPP + biaya operasional lapangan) versus estimasi omzet untuk memproyeksikan laba bersih dan margin keuntungan bagi mahasiswa wirausaha.
- Pengajuan permohonan stand dengan status `pending_review`.

### 📲 5. Vendor Registration & WhatsApp Generator
- Formulir pendaftaran bisnis mandiri untuk calon vendor luar atau mitra kampus.
- Pembuatan Kode Registrasi unik (`VND-XXXXXX`) dan penyimpanan data pendaftaran berstatus `pending_review`.
- Generator template pesan WhatsApp resmi untuk admin COLLEST sesuai format baku PRD dengan encode URL instan. Menampilkan instruksi jelas bahwa membuka WhatsApp tidak sama dengan pesan terkirim.

### 💳 6. Simulasi Pembayaran Prototype
- Simulasi alur pembayaran tagihan stand booth event berbayar (`pending` &rarr; `paid_simulated` atau `failed_simulated`).
- Dilengkapi nomor referensi pembayaran unik (`SIM-PAY-XXXXXX`) dan penegasan bahwa fitur ini murni simulasi lokal akademik tanpa gateway berbayar atau uang riil.

### 🛡️ 7. Autentikasi & Multi-Role Authorization
- Autentikasi berbasis sesi Flask dengan pengacakan password menggunakan *Werkzeug SHA-256 password hashing*.
- Manajemen 4 peran pengguna:
  - **Mahasiswa (Student):** Eksplorasi event, pendaftaran panitia, pencarian vendor, pengajuan stand booth, dan simulasi planner.
  - **Penyelenggara (Organizer):** Mengelola event, menyeleksi pelamar panitia (*accepted / rejected / under_review*), dan menyetujui pengajuan stand booth UMKM.
  - **Mitra Vendor:** Mengelola profil bisnis, katalog paket layanan, dan menanggapi *inquiry* penawaran harga.
  - **Platform Admin:** Moderasi menyeluruh, verifikasi akun penyelenggara & vendor yang berstatus `pending`, serta pengawasan data.

---

## 🧠 3. Konsep IPO (Input, Process, Output)

Sesuai materi mata kuliah **Algoritma dan Dasar Pemrograman**, seluruh logika inti aplikasi didokumentasikan berdasarkan siklus IPO:

### A. Perhitungan Biaya Vendor
- **Input:** Model harga (`unit` / `package` / `quotation`), harga satuan/paket, kuantitas, biaya tambahan.
- **Process:** 
  $$\text{Subtotal} = \text{Harga} \times \text{Kuantitas}$$
  $$\text{Total} = \text{Subtotal} + \text{Biaya Tambahan}$$
  Jika model `quotation`, sistem memberi flag `quotation_required = True` tanpa mengubah harga menjadi Rp 0.
- **Output:** Rincian estimasi biaya dan label status quotation.

### B. Kalkulator Anggaran & HTM Impas (Breakeven)
- **Input:** Daftar biaya (vendor + operasional), target tiket berbayar, target margin (%), pendapatan ekstra sponsor.
- **Process:**
  $$\text{Total Biaya} = \sum \text{Biaya Vendor} + \sum \text{Biaya Operasional}$$
  $$\text{HTM Impas} = \lceil \frac{\text{Total Biaya}}{\text{Target Tiket Berbayar}} \rceil \quad (\text{Proteksi: } \text{Jika Tiket} \le 0 \Rightarrow \text{HTM} = \text{None})$$
  $$\text{Rekomendasi HTM} = \text{HTM Impas} \times (1 + \frac{\text{Margin}}{100})$$
  $$\text{Estimasi Laba} = (\text{Rekomendasi HTM} \times \text{Target Tiket}) + \text{Sponsor} - \text{Total Biaya}$$
- **Output:** Angka HTM impas, rekomendasi harga tiket, total estimasi omzet, dan proyeksi laba/rugi.

### C. Sequential Rundown Generator
- **Input:** Jam mulai acara format `HH:MM`, daftar nama aktivitas beserta durasi (menit), PIC, batas jam akhir (opsional).
- **Process:**
  $$T_{\text{mulai}}^{(1)} = \text{Jam Mulai}$$
  $$T_{\text{selesai}}^{(i)} = T_{\text{mulai}}^{(i)} + \Delta t_i$$
  $$T_{\text{mulai}}^{(i+1)} = T_{\text{selesai}}^{(i)}$$
  Cek apakah waktu selesai akhir melewati batas toleransi maksimal.
- **Output:** Urutan jadwal kegiatan terformat dengan durasi kumulatif.

### D. Pendaftaran Kepanitiaan Event
- **Input:** Event ID, Posisi ID, Nama, NIM, Prodi, Semester, Kontak, Motivasi, Pengalaman, Persetujuan Aturan.
- **Process:** Validasi kelengkapan, verifikasi status event aktif, cek batas waktu pendaftaran, verifikasi sisa kuota posisi, cek duplikasi NIM pada event yang sama, generate kode unik `EVT-XXXXXX`, simpan ke SQLite.
- **Output:** Bukti pendaftaran dan status `submitted`.

---

## 📁 4. Struktur Folder Project

```text
Collest/
├── app/
│   ├── __init__.py             # Application factory & Jinja filters
│   ├── config.py               # Konfigurasi sistem & nomor WhatsApp admin
│   ├── db.py                   # Koneksi SQLite, inisialisasi skema & seed data
│   ├── schema.sql              # DDL 15 tabel relasional SQLite
│   ├── services.py             # Modul algoritma & IPO kalkulasi mandiri
│   ├── auth.py                 # Blueprint autentikasi & role protection
│   ├── routes_main.py          # Blueprint rute halaman publik
│   ├── api.py                  # Blueprint RESTful API JSON (Fetch API)
│   ├── dashboard.py            # Blueprint dashboard Admin, Organizer, Vendor
│   ├── templates/
│   │   ├── base.html           # Template induk navbar, logo, footer, flash
│   │   ├── index.html          # Halaman beranda utama
│   │   ├── recruitment.html    # Halaman Event Recruitment & modal posisi
│   │   ├── vendors.html        # Halaman Find Vendors & Event Planner
│   │   ├── umkm.html           # Halaman UMKM & Booth dengan kalkulator
│   │   ├── vendor_register.html# Halaman pendaftaran vendor & WA generator
│   │   ├── my_registrations.html # Halaman riwayat pendaftaran mahasiswa
│   │   ├── auth/
│   │   │   ├── login.html      # Halaman login
│   │   │   ├── register.html   # Halaman registrasi akun
│   │   │   └── status_notice.html # Halaman pemberitahuan status pending
│   │   └── dashboard/
│   │       ├── admin.html      # Dashboard moderasi Admin
│   │       ├── organizer.html  # Dashboard Penyelenggara Event
│   │       └── vendor.html     # Dashboard Mitra Vendor
│   └── static/
│       ├── css/
│       │   └── style.css       # Design tokens & stylesheet resmi COLLEST
│       ├── js/
│       │   ├── main.js         # Helper global, toast, fetch API wrapper
│       │   ├── recruitment.js  # Interaktivitas pencarian & form seleksi
│       │   ├── vendors.js      # Interaktivitas vendor & kalkulator HTM/rundown
│       │   ├── umkm.js         # Interaktivitas booth & simulasi pembayaran
│       │   └── vendor_register.js # Onboarding vendor & link WhatsApp
│       └── images/
│           ├── logo.svg        # Logo vektor resmi COLLEST
│           ├── logo-icon.svg   # Favicon logo heksagonal
│           └── collest-brand-guide.jpg # Aset panduan brand
├── instance/
│   └── collest.db              # Database SQLite lokal (dibuat saat runtime)
├── tests/
│   ├── conftest.py             # Fixture testing pytest
│   ├── test_services.py        # Pengujian algoritma & logika IPO
│   └── test_api_and_routes.py  # Pengujian rute, API, validasi & role auth
├── .env.example                # Contoh konfigurasi environment
├── .gitignore                  # File pengabaian git
├── requirements.txt            # Dependensi Python
├── run.py                      # Skrip eksekusi server Flask lokal
└── README.md                   # Dokumentasi lengkap proyek
```

---

## 💻 5. Panduan Instalasi & Menjalankan Aplikasi

### Prasyarat
- Python 3.10 atau versi lebih baru terpasang di sistem.

### Langkah 1: Clone / Masuk ke Direktori Project
```bash
cd c:\Users\fitri\OneDrive\Documents\Matkul\Algoritma\Tugas\Collest
```

### Langkah 2: Buat & Aktifkan Virtual Environment
**Pada Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Langkah 3: Install Dependensi
```bash
pip install -r requirements.txt
```

### Langkah 4: Inisialisasi Database & Seed Data Demo
Database akan otomatis terinisialisasi saat pertama kali aplikasi dijalankan. Anda juga dapat melakukan reset manual kapan saja dengan perintah:
```bash
python -c "from app import create_app; from app.db import init_db, seed_db; app = create_app(); ctx = app.app_context(); ctx.push(); init_db(); seed_db(); print('Database berhasil direset!')"
```

### Langkah 5: Jalankan Server Flask
```bash
python run.py
```
Akses platform melalui browser pada alamat: **`http://127.0.0.1:5000`**

---

## 🔑 6. Akun Demo Lokal untuk Pengujian Role

Untuk kemudahan pengujian fitur autentikasi dan otorisasi, telah disediakan akun demo fiktif bawaan:

| Peran (Role) | Email Login | Password Demo | Status Akun | Hak Akses Utama |
|---|---|---|---|---|
| **Platform Admin** | `admin@collest.id` | `AdminPass123!` | `approved` | Akses penuh Panel Moderasi Admin, verifikasi akun & vendor |
| **Penyelenggara Event** | `organizer@bem.univ.ac.id` | `OrgPass123!` | `approved` | Kelola event, seleksi pelamar panitia, review permohonan booth |
| **Organizer (Pending)** | `hima.ilkom@univ.ac.id` | `HimaPass123!` | `pending` | Uji coba pembatasan akses sebelum disetujui Admin |
| **Mitra Vendor** | `vendor.kitchen@gmail.com` | `VendorPass123!` | `approved` | Akses Dashboard Vendor, kelola layanan, respon penawaran harga |
| **Vendor (Pending)** | `creative.sound@gmail.com` | `SoundPass123!` | `pending` | Uji coba peninjauan akun mitra bisnis |
| **Mahasiswa (Student)** | `mahasiswa@student.univ.ac.id` | `StudentPass123!` | `approved` | Akses menu Pendaftaran Saya, daftar panitia & stand UMKM |

---

## 🧪 7. Menjalankan Automated Tests (Pytest)

Pengujian otomatis mencakup seluruh logika kalkulasi bisnis, pencegahan pembagian nol, validasi batas waktu & kuota, pencegahan pendaftaran ganda NIM, proteksi hak akses per role, dan simulasi pembayaran:

```bash
python -m pytest -v
```

Hasil pengujian otomatis:
```text
============================= test session starts =============================
collected 20 items

tests/test_api_and_routes.py::test_public_pages_accessible PASSED        [  5%]
tests/test_api_and_routes.py::test_get_events_api PASSED                 [ 10%]
tests/test_api_and_routes.py::test_event_detail_with_divisions_and_positions PASSED [ 15%]
tests/test_api_and_routes.py::test_event_registration_success PASSED     [ 20%]
tests/test_api_and_routes.py::test_event_registration_duplicate_nim_rejected PASSED [ 25%]
tests/test_api_and_routes.py::test_event_registration_closed_event_rejected PASSED [ 30%]
tests/test_api_and_routes.py::test_vendor_inquiry_flow PASSED            [ 35%]
tests/test_api_and_routes.py::test_booth_application_and_simulated_payment PASSED [ 40%]
tests/test_api_and_routes.py::test_auth_and_dashboard_role_protection PASSED [ 45%]
tests/test_api_and_routes.py::test_pending_organizer_blocked_from_dashboard PASSED [ 50%]
tests/test_services.py::test_calculate_vendor_cost_unit PASSED           [ 55%]
tests/test_services.py::test_calculate_vendor_cost_package PASSED        [ 60%]
tests/test_services.py::test_calculate_vendor_cost_quotation PASSED      [ 65%]
tests/test_services.py::test_calculate_event_financials_with_paid_attendees PASSED [ 70%]
tests/test_services.py::test_calculate_event_financials_zero_attendees_guard PASSED [ 75%]
tests/test_services.py::test_generate_rundown_sequential PASSED          [ 80%]
tests/test_services.py::test_generate_rundown_exceeds_warning PASSED     [ 85%]
tests/test_services.py::test_calculate_booth_profit PASSED               [ 90%]
tests/test_services.py::test_generate_vendor_whatsapp_message PASSED     [ 95%]
tests/test_services.py::test_generate_registration_code PASSED           [100%]

============================= 20 passed in 22.77s =============================
```

---

## 🔒 8. Keterbatasan Prototype & Catatan Deployment

1. **Database SQLite Lokal:** Digunakan untuk kemudahan demonstrasi lokal tanpa dependensi server eksternal. Untuk tahap produksi, arsitektur aplikasi telah dirancang agar mudah dimigrasikan ke PostgreSQL/MySQL menggunakan variabel lingkungan `DATABASE_URL`.
2. **Simulasi Transaksi:** Tidak mengintegrasikan penyedia payment gateway berbayar pihak ketiga. Alur pembayaran menggunakan metode simulasi internal untuk membuktikan konsep alur pemesanan dan verifikasi kas masuk.
3. **Pesan WhatsApp:** Aplikasi menggunakan skema tautan resmi `https://wa.me/{phone}?text={encoded}`. Pengguna diarahkan membuka aplikasi WhatsApp secara manual untuk memastikan kepatuhan privasi dan tidak membebani biaya API pesan berbayar.
