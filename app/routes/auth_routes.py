from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.models import UserRegister, Token
from app.auth import get_password_hash, verify_password, create_access_token

router = APIRouter()

@router.api_route("/register", methods=["GET","POST"])
def register(user: UserRegister, db=Depends(get_db)):
    existing = db.execute("SELECT * FROM users WHERE username = ? OR email = ?", (user.username, user.email)).fetchone()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_pwd = get_password_hash(user.password)
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)", 
                   (user.username, user.email, hashed_pwd))
    db.commit()
    return {"message": "User registered successfully"}

@router.api_route("/login", methods=["GET", "POST"])
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = db.execute("SELECT * FROM users WHERE username = ?", (form_data.username,)).fetchone()
    if not user or not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user['username']})
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"access_token": access_token, "token_type": "bearer", "username": user['username']}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out successfully"}