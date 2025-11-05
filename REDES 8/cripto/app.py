from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Gerar uma chave e instanciar o objeto Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html', key=key.decode())

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data_to_encrypt = request.form['data_to_encrypt']
    encrypted_data = cipher_suite.encrypt(data_to_encrypt.encode()).decode()
    return render_template('index.html', key=key.decode(), encrypted_data=encrypted_data)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        encrypted_data = request.form['encrypted_data']
        try:
            decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
        except Exception as e:
            decrypted_data = f"Erro na descriptografia: {str(e)}"
        return render_template('decrypt.html', decrypted_data=decrypted_data)
    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
