import psycopg2

DB_HOST = "localhost"
DB_NAME = "login_db"  # Atau nama database PostgreSQL Anda
DB_USER = "postgres"    # User default PostgreSQL
DB_PASS = "admin123" # Password PostgreSQL Anda

conn = None
cursor = None

try:
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    cursor = conn.cursor()
    print("Koneksi ke database PostgreSQL berhasil dibuat di db.py!")

except psycopg2.Error as e:
    print(f"Error saat koneksi ke database PostgreSQL di db.py: {e}")
    # Tangani error atau keluar dari aplikasi jika koneksi gagal

# Jangan lupa tambahkan conn.commit() setelah operasi INSERT/UPDATE/DELETE
# Dan conn.close() saat aplikasi mati.