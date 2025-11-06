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
            elif 11 <= y <= 15:
                pesan_tambahan = f"Kamu sedikit Ideal (Sedikit Kurangin Berat Badan Aja) at least kurangin {selisih_minus} kg aja udah cukup"
            elif y < -5:
                pesan_tambahan = f"Duh! Kamu Terlalu Kurus, Bulking Sampai Punya Badan Yang Ideal, Tambahin {selisih_plus} kg lagi buat dapet badan ideal"
            elif y > 15:
                pesan_tambahan = f"Yah! Kamu Terlalu Gemuk, Diet Ya Sampai Kamu Punya Badan Ideal, Kurangin {selisih_minus} kg lagi buat dapet badan ideal"
            elif -5 <= y <= 0 :
                pesan_tambahan = f"Kamu sedikit Ideal (Sedikit Tambahin Berat Badan Aja) at least tambahin {selisih_plus} kg aja udah cukup"
            else: #
                pesan_tambahan = f""
        except ValueError:
            pesan_tambahan = "Input tidak valid. Harap masukkan angka untuk tinggi dan berat badan."
        except Exception as e:
            pesan_tambahan = f"Terjadi kesalahan: {e}"
    return render_template('bodyindex.html', pesan= pesan_tambahan)
