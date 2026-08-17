import sys
import os

# Add backend directory to sys.path
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app import app, db
from models import User, Furniture
from werkzeug.security import generate_password_hash
from seed import FURNITURE

# Initialize database tables and seed data for serverless environment
with app.app_context():
    try:
        db.create_all()
        if not User.query.filter_by(email='demo@gruha.com').first():
            db.session.add(User(username='Demo User', email='demo@gruha.com',
                                password_hash=generate_password_hash('demo123')))
        if Furniture.query.count() == 0:
            for name, cat, tags, price, img, desc in FURNITURE:
                db.session.add(Furniture(name=name, category=cat, style_tags=tags,
                                         price=price, image_url=img, description=desc))
        db.session.commit()
    except Exception as e:
        print(f"Error seeding DB: {e}")

# Export app for Vercel WSGI/Serverless execution
app_handler = app
