from flask import Flask, render_template, request, redirect, url_for, session
from db import cursor

app = Flask(__name__)
app.secret_key = 'secret123'

# ... bagian import dan app.secret_key ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password'] # Ini password plain text dari form

        # Ambil user dari database berdasarkan username saja
        # Ubah query Anda dari 'password=%s' menjadi hanya mengambil user berdasarkan username
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone() # user akan berupa tuple (id, username, email, hashed_password, created_at)

        if user:
            # Sekarang, ambil password yang disimpan dari database (user[3] karena hashed_password adalah kolom keempat, index 3)
            stored_password = user[3]

            # Untuk PENGUJIAN AWAL, jika Anda memasukkan plain text 'password_plain_text' ke DB
            # Maka Anda bisa membandingkan password yang dimasukkan dengan yang disimpan.
            if password == stored_password: # HANYA UNTUK PENGUJIAN PLAIN TEXT!
                session['username'] = username
                return redirect(url_for('dashboard'))
            else:
                return "login gagal (password salah)"
        else:
            return "login gagal (username tidak ditemukan)"
    return render_template('login.html')

# ... sisa kode Anda ...

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Halo, {session['username']}! Ini dashboard kamu."
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
