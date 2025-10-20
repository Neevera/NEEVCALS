from flask import Flask, render_template, request
from datetime import date # Impor kelas date dari modul datetime
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('homepage.html')

@app.route('/cek_usia', methods=['GET', 'POST'])
def usia():
        # Inisialisasi variabel di awal fungsi
    hasil_usia = None
    pesan_tambahan = ""
 
    
    if request.method == 'POST':
        try:
            tahun_lahir_str = request.form.get('tahun')
            bulan_lahir_str = request.form.get('bulan')
            tanggal_lahir_str = request.form.get('tanggal')

            if not all([tahun_lahir_str, bulan_lahir_str, tanggal_lahir_str]):
                pesan_tambahan = "Please fill in all fields (year, month, date)."
                return render_template('main.html', usia=hasil_usia, pesan=pesan_tambahan)

            tahun_lahir = int(tahun_lahir_str)
            bulan_lahir = int(bulan_lahir_str)
            tanggal_lahir = int(tanggal_lahir_str)

        except ValueError:
            pesan_tambahan = "Please enter valid numbers for year, month, and date."
            return render_template('main.html', usia=hasil_usia, pesan=pesan_tambahan)

        # Dapatkan tanggal hari ini secara dinamis
        hari_ini = date.today()
        tahun_sekarang = hari_ini.year
        bulan_sekarang = hari_ini.month
        tanggal_sekarang = hari_ini.day

        # Validasi tanggal lahir menggunakan datetime
        try:
            tanggal_obj_lahir = date(tahun_lahir, bulan_lahir, tanggal_lahir)
        except ValueError:
            pesan_tambahan = f"Birth date {tanggal_lahir}/{bulan_lahir}/{tahun_lahir} is invalid."
            return render_template('main.html', usia=hasil_usia, pesan=pesan_tambahan)

        if tanggal_obj_lahir > hari_ini:
            pesan_tambahan = "The year of birth must not exceed the current year."
            return render_template('main.html', usia=hasil_usia, pesan=pesan_tambahan)

        # Perhitungan usia yang lebih akurat
        hasil_usia = tahun_sekarang - tanggal_obj_lahir.year
        # Cek apakah ulang tahun tahun ini sudah lewat atau belum
        # Jika bulan sekarang lebih kecil dari bulan lahir, ATAU
        # jika bulan sama tapi tanggal sekarang lebih kecil dari tanggal lahir
        if (bulan_sekarang, tanggal_sekarang) < (tanggal_obj_lahir.month, tanggal_obj_lahir.day):
            hasil_usia -= 1
        
        # Pesan ulang tahun
        if bulan_sekarang == tanggal_obj_lahir.month and tanggal_sekarang == tanggal_obj_lahir.day:
            if hasil_usia == 0: # Jika baru lahir hari ini
                 pesan_tambahan = "Welcome to the world! You've just been born today."
            else:
                 pesan_tambahan = f"Anyways, Wishing you a happy {hasil_usia}th birthday!"


        return render_template('usia.html', usia=hasil_usia, pesan=pesan_tambahan)

    # Untuk GET request atau jika method bukan POST
    return render_template('usia.html', usia=hasil_usia, pesan=pesan_tambahan) # Menggunakan variabel yang sudah diinisialisasi


@app.route('/bodyindex', methods=['GET', 'POST'])
def body():
    pesan_tambahan = ""
    if request.method == 'POST':
        
        tinggi_badan_str = request.form.get('tinggi')
        berat_badan_str = request.form.get('berat')
        
        tinggi_badan = int(tinggi_badan_str)
        berat_badan = int(berat_badan_str)
        x = tinggi_badan - 110
        y = berat_badan - x
        selisih_plus = y + (-y - y)
        selisih_minus  = y - 10
        if 0 <= y <= 10:
            pesan_tambahan = "Mantap! Badan kamu ideal"
        elif 11 <= y <= 15:
            pesan_tambahan = f"Kamu sedikit ideal, Sedikit kurangin berat badan aja at least kurangin {selisih_minus} (Kg) aja udah cukup"
        elif y < -5:
            pesan_tambahan = f"Duh! Kamu terlalu kurus, bulking sampai punya badan yang ideal ya, Tambahin {selisih_plus} (Kg) lagi buat dapet badan ideal"
        elif y > 15:
            pesan_tambahan = f"Yah! Kamu terlalu gemuk, diet sampai kamu punya badan ideal ya, Kurangin {selisih_minus} (Kg) lagi buat dapet badan ideal "
        elif -5 <= y <= 0 :
            pesan_tambahan = f"Kamu sedikit ideal, Sedikit tambahin berat badan aja at least tambahin {selisih_plus} (Kg) aja udah cukup"
        else:
            pesan_tambahan = "Error"
        
        return render_template('bodyindex.html', pesan= pesan_tambahan)

    return render_template('bodyindex.html', pesan= pesan_tambahan)   



@app.route('/konversi', methods=["GET", "POST"])
def konvers():
    hasil = None
    error = None
    pilihan_terpilih = None
    angka_input = None

    if request.method == "POST":
        pilihan = request.form.get("pilihan")
        angka_str = request.form.get("angka")
        pilihan_terpilih = pilihan # Simpan pilihan untuk ditampilkan kembali di form
        angka_input = angka_str # Simpan input angka untuk ditampilkan kembali

        try:
            if not angka_str:
                error = "Type number!"
            elif pilihan == "debin":
                angka = int(angka_str)
                hasil_konversi = bin(angka)[2:]
                hasil = f"{angka}(dec) = {hasil_konversi}(bin)"
            elif pilihan == "dehex":
                angka = int(angka_str)
                hasil_konversi = hex(angka)[2:].upper()
                hasil = f"{angka}(dec) = {hasil_konversi}(hex)"
            elif pilihan == "deoct":
                angka = int(angka_str)
                hasil_konversi = oct(angka)[2:]
                hasil = f"{angka}(dec) = {hasil_konversi}(oct)"

            elif pilihan == "bindec":
                angka = int(angka_str, 2)
                hasil = f"{angka_str}(bin) = {angka}(dec)"
            elif pilihan == "binhex":
                angka_dec = int(angka_str, 2)
                hasil_konversi = hex(angka_dec)[2:].upper()
                hasil = f"{angka_str}(bin) = {hasil_konversi}(hex)"
            elif pilihan == "binoct":
                angka_dec = int(angka_str, 2)
                hasil_konversi = oct(angka_dec)[2:]
                hasil = f"{angka_str}(bin) = {hasil_konversi}(oct)"

            elif pilihan == "hexdec":
                angka = int(angka_str, 16)
                hasil = f"{angka_str.upper()}(hex) = {angka}(dec)"
            elif pilihan == "hexbin":
                angka_dec = int(angka_str, 16)
                hasil_konversi = bin(angka_dec)[2:]
                hasil = f"{angka_str.upper()}(hex) = {hasil_konversi}(bin)"
            elif pilihan == "hexoct":
                angka_dec = int(angka_str, 16)
                hasil_konversi = oct(angka_dec)[2:]
                hasil = f"{angka_str.upper()}(hex) = {hasil_konversi}(oct)"

            elif pilihan == "ocdec":
                # Perbaikan: gunakan angka_str bukan ocdec
                angka = int(angka_str, 8)
                hasil = f"{angka_str}(oct) = {angka}(dec)"
            elif pilihan == "ocbin":
                angka_dec = int(angka_str, 8)
                hasil_konversi = bin(angka_dec)[2:]
                hasil = f"{angka_str}(oct) = {hasil_konversi}(bin)"
            elif pilihan == "ochex":
                angka_dec = int(angka_str, 8)
                hasil_konversi = hex(angka_dec)[2:].upper()
                hasil = f"{angka_str}(oct) = {hasil_konversi}(hex)"
            else:
                error = "Invalid conversion choice."

        except ValueError:
            error = f"The input for '{angka_str}' was invalid. Please enter a valid number!"
        except Exception as e:
            error = f"Error: {e}"

    return render_template("konv.html", hasil=hasil, error=error, pilihan_terpilih=pilihan_terpilih, angka_input=angka_input)  
    
    

if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0', port = 5001)

