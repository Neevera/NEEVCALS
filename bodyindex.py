from flask import Blueprint, render_template, request
body_bp = Blueprint('bodyindex', __name__)


@body_bp.route('/body', methods=['GET', 'POST'])
def body():
    pesan_tambahan = ""
    if request.method == 'POST':
        try:
            tinggi_badan_str = request.form.get('tinggi')
            berat_badan_str = request.form.get('berat')
            
            tinggi_badan = int(tinggi_badan_str)
            berat_badan = int(berat_badan_str)
            
            x = tinggi_badan - 110
            y = berat_badan - x
            
            # Perbaikan logika selisih_plus dan selisih_minus agar lebih jelas
            if y < 0: # Terlalu kurus
                selisih_plus = abs(y) # Berapa kg yang harus ditambah
            else: # Terlalu gemuk atau ideal
                selisih_plus = 0

            if y > 10: # Terlalu gemuk
                selisih_minus = y - 10 # Berapa kg yang harus dikurangi
            else: # Terlalu kurus atau ideal
                selisih_minus = 0

            if 0 <= y <= 10:
                pesan_tambahan = "Mantap! Badan kamu ideal"
            elif y > 10:
                pesan_tambahan = f"Yah! Kamu terlalu gemuk, diet sampai kamu punya badan ideal ya, Kurangin {selisih_minus} (Kg) lagi buat dapet badan ideal."
            else: # y < 0
                pesan_tambahan = f"Duh! Kamu terlalu kurus, bulking sampai punya badan yang ideal ya, Tambahin {selisih_plus} (Kg) lagi buat dapet badan ideal."
        except ValueError:
            pesan_tambahan = "Input tidak valid. Harap masukkan angka untuk tinggi dan berat badan."
        except Exception as e:
            pesan_tambahan = f"Terjadi kesalahan: {e}"
    return render_template('bodyindex.html', pesan= pesan_tambahan)