# 🌐 Kumpulan Web Tools & Chatbot NeevAI

Halo! Selamat datang di repo project Web Tools serbaguna. 

Project ini adalah aplikasi berbasis web yang dibikin pakai framework **Flask** (Python). Di dalamnya nggak cuma ada satu fitur, tapi kumpulan berbagai macam *tools* yang kepakai banget buat sehari-hari sampai buat tugas kuliah anak IT. Oh iya, di web ini juga ada asisten AI pintar yang siap diajak ngobrol!

*(Catatan: Tampilan web-nya pakai HTML/CSS yang ditaruh di folder `templates` dan `static`, tapi repo ini fokus ke logika *backend* Python-nya).*

---

## ✨ Fitur-fitur Kece di Dalamnya

* 🤖 **Chatbot NeevAI (`chatbot.py`):** Asisten AI ramah yang ditenagai oleh model canggih `Llama-3.3-70b-versatile` lewat API Groq. Bisa diajak ngobrol santai, nanya tugas, sampai curhat.
* ⚖️ **Kalkulator BMI / Body Index (`bodyindex.py`):** Tools buat ngecek apakah berat badan kamu udah ideal, kurang, atau harus diet. Nanti bakal dikasih tau kurang/lebih berapa kilonya!
* 🔢 **Konverter Bilangan (`konv.py`):** Fitur wajib buat anak IT atau anak jaringan. Bisa ubah-ubah angka Desimal, Biner, Oktal, sampai Hexadesimal secara otomatis.
* 💰 **Kalkulator Pajak PPh 21 (`pph21.py`):** Bingung ngitung potongan pajak gaji? Tinggal masukin gaji bulanan sama status tanggungan, sistem bakal ngitungin total Penghasilan Kena Pajak (PKP) sampai rincian pajak per bulannya.
* 🎂 **Kalkulator Usia (`usia.py`):** Hitung umur kamu secara akurat (tahun) berdasarkan tanggal lahir. Kalau pas banget kamu lagi ulang tahun pas buka web ini, bakal ada ucapan spesialnya lho!

---

## 📂 Kenalan Sama Isi File-nya

Biar gampang navigasinya, ini penjelasan simpel buat file-file Python yang ada di project ini:

* `index.py` ➔ **Pusat Kendali (Main Router).** Ini adalah file utama yang nyambungin semua fitur di atas ke halaman web. Dia yang ngatur kalau user buka `/bmi` perginya ke mana, kalau buka `/chatbot` perginya ke mana.
* File-file *Blueprint* (Fitur Utama):
    * `chatbot.py` ➔ Otak dari asisten NeevAI. Di sini diatur sifat AI-nya dan cara dia nyambung ke server Groq.
    * `bodyindex.py` ➔ Isinya rumus matematika buat ngitung selisih tinggi dan berat badan.
    * `konv.py` ➔ Tempatnya logika konversi (*built-in function* Python kayak `bin()`, `hex()`, `oct()`).
    * `pph21.py` ➔ Isinya aturan baku PTKP dan persentase tarif pajak berjenjang.
    * `usia.py` ➔ Logika buat nyocokin tanggal lahir kamu sama tanggal hari ini pakai `datetime`.
* `requirements.txt` ➔ Daftar "alat tempur" atau *library* tambahan yang wajib di-install biar aplikasinya jalan (kayak Flask, Groq, dll).

---

## 🚀 Cara Install & Jalanin di Laptop Kamu

Pengen nyoba jalanin web ini di komputermu sendiri? Gampang banget, ikutin langkah ini:

### 1. Install Alat Tempur
Buka terminal / Command Prompt di folder project ini, terus ketik perintah ini buat nginstall Flask dan teman-temannya:
```bash
pip install -r requirements.txt
