import os

from flask import Flask, render_template
from bodyindex import body_bp
from usia import usia_bp
from konv import konv_bp
from pph21 import pph21_bp
from chatbot import chatbot_bp
app = Flask(__name__)
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
