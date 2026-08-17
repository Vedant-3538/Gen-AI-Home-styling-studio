import os

db_url = os.environ.get('DATABASE_URL')
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'gruha-alankara-secret-2024')
    SQLALCHEMY_DATABASE_URI = db_url or 'sqlite:///gruha.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyAOnfr3CzHP9s3i7u5rgqUGZ4i6L4bRPEk')
    SARVAM_API_KEY = os.environ.get('SARVAM_API_KEY', 'sk_tlnqgzth_CZqeWKV4bzznLtqcYETzkQUs')

