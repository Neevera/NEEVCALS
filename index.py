import os

from flask import Flask, render_template
from api.bodyindex import body_bp
from api.usia import usia_bp
from api.konv import konv_bp
from api.pph21 import pph21_bp
from api.chatbot import chatbot_bp

# 3. PENGATURAN FOLDER AGAR FLASK TIDAK NYASAR DI VERCEL
# Memberitahu Flask untuk mundur satu langkah keluar dari folder 'api'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

# 4. Inisialisasi Flask dengan jalur folder yang benar
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'CHANGE_ME_TO_A_SECRET')


@app.route('/')
def main_page():
    return render_template('homepage.html')

#daftarkan blueprint
app.register_blueprint(body_bp, url_prefix='/bmi')
app.register_blueprint(usia_bp, url_prefix='/usia')
app.register_blueprint(konv_bp, url_prefix='/konverter')
app.register_blueprint(pph21_bp, url_prefix='/pajak')
app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
