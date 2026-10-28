import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Pastikan database terinisialisasi jika belum ada
    db_path = app.config['DATABASE_PATH']
    if not os.path.exists(db_path):
        with app.app_context():
            from app.db import init_db, seed_db
            print("Inisialisasi database dan seed data demo pertama kali...")
            init_db()
            seed_db()
            print("Database siap digunakan!")

    port = int(os.environ.get('PORT', 5000))
    print(f"Server COLLEST berjalan di http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=app.config.get('DEBUG', True))
