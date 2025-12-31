# jpXcode Auto Clicker V.1 🖱️⚡

![Visitors](https://komarev.com/ghpvc/?username=jpXproject&color=00ff88)
[![Instagram](https://img.shields.io/badge/Instagram-@jpxproject-E4405F?logo=instagram&logoColor=white)](https://instagram.com/jepanx)
[![Threads](https://img.shields.io/badge/Threads-@jepanx-4B0082?logo=threads&logoColor=white)](https://www.threads.com/@jepanx)
[![Facebook](https://img.shields.io/badge/Facebook-jpXproject-1877F2?logo=facebook&logoColor=white)](https://facebook.com/jepanx.id)
[![Tiktok](https://img.shields.io/badge/Tiktok-Binary[X]code-663399?logo=tiktok&logoColor=white)](https://tiktok.com/@oneal___)
[![Lynk.id](https://img.shields.io/badge/lynk.id-jpxcode-90EE90?logo=lynk&logoColor=green)](https://lynk.id/jpxcode)

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows)

Aplikasi auto clicker profesional berbasis Python untuk Windows dengan fitur lengkap dan antarmuka yang user-friendly. Sempurna untuk automation, gaming, testing, dan produktivitas.

## 📸 Screenshot

```
┌─────────────────────────────────────┐
│     jpXcode Auto Clicker v1.0       │
├─────────────────────────────────────┤
│  ⚙️ Interval Klik                   │
│  🖱️ Opsi Klik                        │
│  🔄 Pengulangan                     │
│  📍 Posisi Kursor                    │
│  ⌨️ Hotkey                          │
│  🎬 Rekam & Putar Ulang             |
└─────────────────────────────────────┘
```

## ✨ Fitur Utama

### 🎯 Kontrol Klik yang Presisi
- **Interval Kustom**: Atur waktu jeda dalam jam, menit, detik, atau milidetik
- **Opsi Tombol**: Pilih klik kiri, kanan, atau tengah
- **Jenis Klik**: Tunggal, ganda, atau tiga kali klik
- **Kecepatan Tinggi**: Mendukung interval hingga 1 milidetik

### 🔄 Mode Pengulangan Fleksibel
- **Unlimited Mode**: Klik terus menerus hingga dihentikan manual
- **Limited Mode**: Tentukan jumlah klik yang spesifik
- **Real-time Counter**: Monitor jumlah klik yang telah dilakukan

### 📍 Positioning Cerdas
- **Dynamic Position**: Klik pada posisi kursor saat ini
- **Fixed Position**: Klik pada koordinat layar yang telah ditentukan
- **Position Capture**: Ambil posisi kursor dengan mudah menggunakan timer 3 detik

### ⌨️ Hotkey Support
- **Default Hotkey**: F6 untuk start/stop
- **Customizable**: Ubah hotkey sesuai preferensi Anda
- **Background Operation**: Bekerja bahkan saat aplikasi di latar belakang

### 🎬 Record & Playback
- **Smart Recording**: Rekam urutan klik dan gerakan mouse yang kompleks
- **Playback Perfect**: Putar ulang rekaman dengan timing yang akurat
- **Save/Load**: Simpan dan muat rekaman untuk digunakan kapan saja
- **Format JSON**: Rekaman disimpan dalam format yang mudah diedit

### 🚀 Portabel & Ringan
- **No Installation**: Jalankan langsung tanpa instalasi
- **Single Executable**: Satu file .exe portabel
- **Low Resource**: Penggunaan CPU dan RAM yang minimal
- **No Dependencies**: Tidak perlu install Python di komputer target

## 📋 Requirements

### Untuk Menjalankan Source Code:
- Python 3.7 atau lebih tinggi
- Windows 7/8/10/11

### Untuk Menjalankan Executable:
- Windows 7/8/10/11
- Tidak perlu instalasi tambahan

## 🔧 Instalasi & Setup

### Opsi 1: Menggunakan Executable (Recommended)

1. **Download** file `jpXcode_AutoClicker.exe` dari [Releases](../../releases)
2. **Jalankan** file executable
3. **Selesai!** Aplikasi siap digunakan

### Opsi 2: Menjalankan dari Source Code

1. **Clone repository:**
```bash
git clone https://github.com/jpXproject/jpxcode-autoclicker.git
cd jpxcode-autoclicker
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Jalankan aplikasi:**
```bash
python jpxcode_autoclicker.py
```

### Opsi 3: Build Sendiri dari Source

1. **Install PyInstaller:**
```bash
pip install pyinstaller
```

2. **Build executable:**
```bash
pyinstaller --onefile --windowed --name="jpXcode_AutoClicker" jpxcode_autoclicker.py
```

3. **Output** ada di folder `dist/`

## 📦 Dependencies

```
pyautogui>=0.9.53
keyboard>=0.13.5
mouse>=0.7.1
Pillow>=9.0.0
```

## 🎮 Cara Menggunakan

### 1️⃣ Konfigurasi Dasar

**Set Interval Klik:**
- Masukkan nilai untuk jam, menit, detik, atau milidetik
- Contoh: 100 milidetik = 10 klik per detik

**Pilih Opsi Klik:**
- Pilih tombol mouse (Kiri/Kanan/Tengah)
- Pilih jenis klik (Tunggal/Ganda/Tiga Kali)

**Set Pengulangan:**
- Pilih "Ulangi tanpa batas" untuk auto-click kontinyu
- Atau pilih "Jumlah tertentu" dan masukkan angka

### 2️⃣ Mengatur Posisi

**Untuk Posisi Dinamis:**
- Pilih "Lokasi kursor saat ini"
- Klik akan mengikuti posisi kursor Anda

**Untuk Posisi Tetap:**
- Pilih "Lokasi spesifik"
- Klik "Ambil Posisi" dan arahkan kursor dalam 3 detik
- Atau masukkan koordinat X dan Y secara manual

### 3️⃣ Menggunakan Hotkey

- Tekan **F6** (default) untuk memulai/menghentikan auto-click
- Klik "Ubah Hotkey" untuk mengatur tombol custom
- Hotkey bekerja di background

### 4️⃣ Rekam & Putar Ulang

**Merekam:**
1. Klik "Mulai Rekam" atau tekan **F7**
2. Lakukan klik dan gerakan mouse yang ingin direkam
3. Tekan **F7** lagi untuk menghentikan

**Memutar Ulang:**
1. Klik "Putar Ulang" untuk mengeksekusi rekaman
2. Gunakan "Simpan" untuk menyimpan ke file
3. Gunakan "Muat" untuk membuka rekaman sebelumnya

## 🎯 Use Cases

### 🎮 Gaming
- Auto farming di game
- Repetitive clicking tasks
- Resource gathering automation

### 💼 Productivity
- Testing aplikasi dengan input repetitif
- Form filling automation
- Data entry tasks

### 🧪 Testing & Development
- UI/UX stress testing
- Click simulation untuk QA
- Performance testing

### 🎨 Design & Creative
- Batch processing dengan clicks
- Tool automation di software design
- Workflow optimization

## ⚠️ Disclaimer

- **Gunakan dengan Bijak**: Aplikasi ini dibuat untuk tujuan produktivitas dan testing
- **Tanggung Jawab Pengguna**: Penggunaan untuk cheating dalam game online atau aktivitas yang melanggar ToS adalah tanggung jawab pengguna
- **Legal Compliance**: Pastikan penggunaan aplikasi sesuai dengan hukum dan peraturan yang berlaku
- **Anti-Virus Warning**: Beberapa antivirus mungkin mendeteksi auto-clicker sebagai suspicious. Ini false positive karena sifat aplikasi yang mensimulasikan input

## 🐛 Troubleshooting

### Aplikasi tidak bisa klik di game tertentu
- Beberapa game memiliki anti-cheat yang memblokir input simulasi
- Coba jalankan aplikasi sebagai Administrator

### Hotkey tidak bekerja
- Pastikan tidak ada aplikasi lain yang menggunakan hotkey yang sama
- Coba ubah hotkey ke tombol lain

### Executable terdeteksi sebagai virus
- Ini adalah false positive yang umum terjadi pada auto-clicker
- Anda bisa build sendiri dari source code untuk memastikan keamanan

### Error saat recording
- Pastikan memiliki permission untuk monitoring mouse events
- Jalankan sebagai Administrator jika diperlukan

## 🤝 Contributing

Kontribusi sangat diterima! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Changelog

### Version 1.0.0 (2026-01-01)
- ✨ Initial release
- ✅ Full feature implementation
- 🎨 Modern UI design
- 📦 Portable executable build
- 📖 Complete documentation

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

## 👨‍💻 Author

**jpXproject**

Jika Anda suka project ini, jangan lupa kasih ⭐ ya!

## 🔗 Links

- 📧 **Support**: [Contact via Lynk.id](https://lynk.id/jpxcode/s/47zdmje5gd8m)
- 🐛 **Bug Reports**: [GitHub Issues](../../issues)
- 💡 **Feature Requests**: [GitHub Discussions](../../discussions)
- 📖 **Documentation**: [Wiki](../../wiki)

## 💖 Support

Jika aplikasi ini bermanfaat untuk Anda:

- ⭐ Star repository ini
- 🔄 Share ke teman-teman
- 📱 Follow social media kami untuk update terbaru
- ☕ Support development via [Lynk.id](https://lynk.id/jpxcode/s/47zdmje5gd8m)

---

<div align="center">

**Made with ❤️ by jpXproject**

*Empowering productivity through automation*

![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>
