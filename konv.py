from flask import Blueprint, render_template, request
konv_bp = Blueprint('konv', __name__)


@konv_bp.route('/konversi', methods=["GET", "POST"])
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