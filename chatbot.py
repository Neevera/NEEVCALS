from flask import Blueprint, render_template, request, session, redirect, url_for
from groq import Groq
import os

chatbot_bp = Blueprint('chatbot', __name__)
api_key_groq = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key_groq)

@chatbot_bp.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    
    system_instruction = {
        "role": "system", 
        "content": ''' ###
.'''
    }

    # 1. Inisialisasi riwayat pesan HANYA dengan obrolan saja
    if 'messages' not in session:
        session['messages'] = [
            {"role": "assistant", "content": "Halo! Aku NeevAI, asisten AI yang dirancang buat nemenin kamu. Ada yang pengen kamu tanyain ga?"}
        ]

    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip()
        
        if user_input:
            messages = session['messages']
            
            # 2. Masukkan pesan user ke list
            messages.append({"role": "user", "content": user_input})
            
            try:
                # 3. GABUNGKAN system prompt dengan riwayat pesan saat memanggil API
                messages_to_send = [system_instruction] + messages
                
                response = client.chat.completions.create(
                    messages=messages_to_send,
                    model="llama-3.3-70b-versatile"
                )
                
                # 4. Ambil teks balasan AI
                ai_reply = response.choices[0].message.content
                
                # 5. Masukkan balasan AI ke list session
                messages.append({"role": "assistant", "content": ai_reply})
                
            except Exception as e:
                messages.append({"role": "assistant", "content": f"Duh, server AI lagi ada kendala, tunggu bentar yaa: {str(e)}"})

            # 6. Simpan list terbaru kembali ke session (Sekarang ukurannya sangat kecil & aman!)
            session['messages'] = messages
            session.modified = True
            
        return redirect(url_for('chatbot.chatbot') + '#bottom')

    # 7. Siapkan data untuk ditampilkan ke HTML (Logika tetap sama)
    chat_history_untuk_html = []
    
    for msg in session.get('messages', []):
        sender = "bot" if msg['role'] == "assistant" else "user"
        text_html = msg['content'].replace('\n', '<br>')
        chat_history_untuk_html.append({"sender": sender, "text": text_html})

    return render_template('chatbot.html', chat_history=chat_history_untuk_html)

@chatbot_bp.route('/reset')
def reset_chat():
    session.pop('messages', None)
    return redirect(url_for('chatbot.chatbot'))
