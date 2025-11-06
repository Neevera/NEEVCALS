from flask import Blueprint, render_template, request
from datetime import date # Impor kelas date dari modul datetime
usia_bp = Blueprint('usia', __name__)


@usia_bp.route('/cek_usia', methods=['GET', 'POST'])
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
                return render_template('usia.html', usia=hasil_usia, pesan=pesan_tambahan)

            tahun_lahir = int(tahun_lahir_str)
            bulan_lahir = int(bulan_lahir_str)
            tanggal_lahir = int(tanggal_lahir_str)

        except ValueError:
            pesan_tambahan = "Please enter valid numbers for year, month, and date."
            return render_template('usia.html', usia=hasil_usia, pesan=pesan_tambahan)

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
            return render_template('usia.html', usia=hasil_usia, pesan=pesan_tambahan)

        if tanggal_obj_lahir > hari_ini:
            pesan_tambahan = "The year of birth must not exceed the current year."
            return render_template('usia.html', usia=hasil_usia, pesan=pesan_tambahan)

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