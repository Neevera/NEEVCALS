from flask import Blueprint, render_template, request

pph21_bp = Blueprint("pph21",__name__)

@pph21_bp.route("/pph21", methods=["GET", "POST"])
def hitung_pph21():
    hasil = None

    if request.method == "POST":
        try:
            # === Kalkulator Pajak Penghasilan ===
            gaji_bulanan = float(request.form["gaji_bulanan"])
            status = request.form["status"]

            # PTKP per tahun berdasarkan status
            ptkp_dict = {
                "1": 54000000,   
                "2": 58500000,   
                "3": 63000000,    
                "4": 67500000,    
                "5": 72000000     
            }

            ptkp = ptkp_dict.get(status, 54000000)

            # Hitung penghasilan tahunan
            penghasilan_tahunan = gaji_bulanan * 12

            output = []
            output.append("=== Kalkulator Pajak Penghasilan ===\n")
            output.append("--- Rincian Penghasilan ---")
            output.append(f"Gaji bulanan: Rp.{gaji_bulanan:,.0f}")
            output.append(f"Penghasilan Total Gaji Tahunan: Rp.{penghasilan_tahunan:,.0f}")
            output.append(f"Total Penghasilan Tidak Kena Pajak (PTKP) : Rp.{ptkp:,.0f}")

            # Hitung penghasilan kena pajak
            pkp = penghasilan_tahunan - ptkp
            if pkp <= 0:
                output.append("\nPenghasilan tidak kena pajak karena di bawah PTKP.")
                hasil = "\n".join(output)
                return render_template("pph21.html", hasil=hasil)

            output.append(f"\nPenghasilan Kena Pajak (PKP): Rp.{pkp:,.0f}\n")

            # Lapisan tarif 
            lapisan = [
                (60000000, 0.05),
                (250000000, 0.15),
                (500000000, 0.25),
                (5000000000, 0.30),
                (float("inf"), 0.35)
            ]

            # Hitung pajak
            sisa_pkp = pkp
            total_pajak = 0
            batas_bawah = 0

            output.append("--- Rincian Pajak per Lapisan ---")
            for batas_atas, tarif in lapisan:
                if sisa_pkp <= 0:
                    break

                lapisan_kena_pajak = min(sisa_pkp, batas_atas - batas_bawah)
                pajak_lapisan = lapisan_kena_pajak * tarif
                total_pajak += pajak_lapisan

                output.append(f"- Rp.{lapisan_kena_pajak:>15,.0f} × {tarif*100:.0f}% = Rp.{pajak_lapisan:,.0f}")

                sisa_pkp -= lapisan_kena_pajak
                batas_bawah = batas_atas

            # Hasil akhir
            output.append("\n--- Total Pajak ---")
            output.append(f"Total PPh Tahunan : Rp.{total_pajak:,.0f}")
            output.append(f"PPh Bulanan       : Rp.{total_pajak/12:,.0f}")

            hasil = "\n".join(output)
        except ValueError:
            hasil = "Input tidak valid. Harap masukkan angka untuk gaji bulanan."
        except Exception as e:
            hasil = f"Terjadi kesalahan: {e}"
    return render_template("pph21.html", hasil=hasil)
