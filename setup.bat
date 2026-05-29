@echo off
echo ============================================
echo   Gruha Alankara - Environment Setup
echo ============================================
python -m venv venv
call venv\Scripts\activate
pip install -r backend\requirements.txt
echo.
echo Seeding database...
cd backend
python seed.py
echo.
echo ============================================
echo   Setup complete! Run: run.bat
echo ============================================
pause
