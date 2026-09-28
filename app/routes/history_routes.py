from fastapi import APIRouter, Depends
from app.auth import get_current_user_from_cookie
from app.database import get_db

router = APIRouter()

@router.get("/api/history")
def get_history(current_user=Depends(get_current_user_from_cookie), db=Depends(get_db)):
    records = db.execute("SELECT * FROM recommendations WHERE user_id = ? ORDER BY created_at DESC", (current_user['id'],)).fetchall()
    return {"history": [dict(r) for r in records]}