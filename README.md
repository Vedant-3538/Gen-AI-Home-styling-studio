🛋️ GenAI Home Styling Studio

A comprehensive full-stack web application that empowers users to reimagine their home interiors. By uploading a photo of a room, users receive personalized, budget-constrained interior design recommendations powered by Generative AI. The platform also features a multilingual AI voice assistant, augmented reality (AR) furniture visualization, and an integrated booking system for conversational commerce.

## 🌟 Features

### 🤖 AI-Powered Design
* **Room Analysis:** Upload photos of your room for instant architectural and design analysis.
* **Generative AI Recommendations:** Uses Google Gemini API to generate personalized styling suggestions based on budget, room type, and preferred style.
* **Smart Validation:** Integrates OpenCV and Pillow to preprocess uploads and validate that images are actual room interiors before running expensive GenAI inference.

### 🎙️ Multilingual Voice Assistant
* **AI Design Buddy:** An interactive chatbot that assists with design choices.
* **Voice Integration (STT/TTS):** Powered by the Sarvam AI API to support voice commands and responses.
* **Regional Languages:** Seamlessly converse in English, Hindi, and Marathi.

### 🛋️ Smart Furniture & Booking
* **Conversational Commerce:** The AI chatbot recommends tailored furniture based on room aesthetics and allows users to seamlessly book/purchase items directly within the chat interface.
* **AR Visualization:** A structured portal for viewing suggested furniture in Augmented Reality.
* **Dynamic Catalog:** Automatically adapts and creates AI-suggested furniture items into the database.

### 👤 User Management
* **Secure Authentication:** Flask-Login based secure user sessions with Werkzeug password hashing.
* **Interactive Dashboard:** Track past design analyses, manage furniture bookings, and view generated recommendations.

## 🏗️ Architecture

### Backend (Flask)
* **Framework:** Flask 
* **Database:** SQLite with SQLAlchemy ORM
* **Authentication:** Flask-Login & Werkzeug Security
* **Server:** Gunicorn (for production)

### Frontend (HTML/CSS/JS)
* **Framework:** HTML5, Vanilla JavaScript, Jinja2 Templates
* **Styling:** Custom CSS with responsive layouts
* **Interactivity:** Dynamic fetch APIs for seamless chatbot and voice integration

### AI & ML Pipeline
* **Generative AI:** Google Gemini API for spatial and interior design reasoning
* **Voice AI:** Sarvam AI APIs for Text-to-Speech (TTS) and Speech-to-Text (STT)
* **Image Processing:** OpenCV and Pillow for pre-inference image validation

## 🚀 Quick Start

### Prerequisites
* Python 3.9+
* pip package manager
* Valid API Keys for Google Gemini and Sarvam AI

### Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/powar293/GenAI-Home-Styling-Studio.git
   cd GenAI-Home-Styling-Studio
   ```

2. **Backend Setup**
   Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Ensure your API keys are added to `config.py` or a `.env` file:
   * `GOOGLE_GEMINI_API_KEY`
   * `SARVAM_API_KEY`

4. **Initialize database**
   The application uses SQLite and will auto-create the database `app.db` on the first run.

5. **Start the application**
   ```bash
   python app.py
   ```
   *(Alternatively, run `run.bat` on Windows)*

6. **Access the application**
   Navigate to `http://localhost:5000` in your web browser.

## 📁 Project Structure

```text
GenAI-Home-Styling-Studio/
├── app.py                   # Main Flask application & routing
├── config.py                # Configuration and Environment settings
├── models.py                # SQLAlchemy Database models
├── ai_engine.py             # Core logic for GenAI, Voice, and Image Validation
├── requirements.txt         # Python dependencies
├── run.bat                  # Windows startup script
├── static/                  # CSS, JS, and image assets
├── templates/               # Jinja2 HTML templates
└── uploads/                 # Directory for user-uploaded room images
```

## 🔧 Configuration

### Environment Variables (.env or config.py)

```env
# API Keys
GOOGLE_GEMINI_API_KEY=your-gemini-api-key
SARVAM_API_KEY=your-sarvam-api-key

# App Configuration
SECRET_KEY=your-secure-secret-key
UPLOAD_FOLDER=uploads/
```

## 📊 API Endpoints

### Authentication
* `POST /api/register` - User registration
* `POST /api/login` - User login
* `GET /logout` - Terminate user session

### Design & Analysis
* `POST /api/analyze` - Upload image and generate AI interior design

### AI Buddy & Voice
* `POST /api/buddy/chat` - Interact with the AI design buddy
* `POST /api/voice/stt` - Process audio to text (Speech-to-Text)
* `POST /api/voice/tts` - Convert text response to audio (Text-to-Speech)

### Commerce & Bookings
* `POST /api/book` - Book an AI-suggested or catalog furniture item
* `POST /api/cancel-booking/<bid>` - Cancel an existing booking
* `GET /api/furniture` - Retrieve furniture catalog

## 🎨 Design System

### Colors
* **Primary:** Modern sleek accents
* **Backgrounds:** Clean, aesthetic minimalism to highlight room designs

### Typography
* **Font Family:** Modern Sans-Serif (e.g., Inter, Roboto) for high readability

## 🔒 Security

### Implemented Measures
* **Session Management:** Secure cookie-based auth via Flask-Login
* **Password Hashing:** Werkzeug security (pbkdf2:sha256)
* **SQL Injection Prevention:** SQLAlchemy ORM abstraction
* **File Upload Security:** Strict MIME type and extension validation (`.png`, `.jpg`, `.jpeg`, `.webp`)

## 🚀 Deployment

### Production Deployment
The application is configured with `gunicorn` in `requirements.txt` for production deployment.

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open-source. Please refer to the repository's LICENSE file for details.

## 🙏 Acknowledgments

* **Google Generative AI** - For empowering the design inference
* **Sarvam AI** - For robust multilingual voice capabilities
* **Flask Community** - Excellent web framework

## 📞 Support

For support or feature requests, please create an issue on GitHub.