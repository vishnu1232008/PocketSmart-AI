# PocketSmart AI
Your Smart Budget & Recommendation Assistant.

## Setup Instructions
1. Create virtual environment: `python -m venv venv`
2. Activate: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Add your Gemini API Key to the `.env` file.
5. Run application: `uvicorn app.main:app --reload`
6. Open browser at `http://127.0.0.1:8000`