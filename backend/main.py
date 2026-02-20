from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, HTTPException, Depends
from typing import List
from schemas import Request
import models
from database import cursor, conn
from pydantic import BaseModel

app = FastAPI(title="Smart Service Request Portal")

# Dummy token check
def check_token(token: str):
    if token != "admin":  # replace "admin" with your login token
        raise HTTPException(status_code=401, detail="Invalid token")
    return token
# Model to read JSON body
class StatusPayload(BaseModel):
    status: str


# ---------------------------
# CREATE A NEW REQUEST
# ---------------------------
@app.post("/request", response_model=dict)
def create_request(request: Request, token: str = Query(...)):

    if not token:
        raise HTTPException(status_code=401, detail="Token required")

    cursor.execute("""
        INSERT INTO requests
        (title, category, description, priority, name, email, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        request.title,
        request.category,
        request.description,
        request.priority,
        request.name,
        request.email,
        "Open"  # default status
    ))
    conn.commit()

    return {"message": "Request Created Successfully"}
# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------
# GET ALL REQUESTS
# ---------------------------
@app.get("/requests", response_model=List[dict])
def get_requests(token: str = Query(...)):

    if not token:
        raise HTTPException(status_code=401, detail="Token required")

    cursor.execute("SELECT * FROM requests")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "title": row[1],
            "category": row[2],
            "description": row[3],
            "priority": row[4],
            "name": row[5],
            "email": row[6],
            "status": row[7]
        })

    return data
@app.put("/requests/{request_id}/status")
def update_status(request_id: int, payload: StatusPayload, token: str = Depends(check_token)):
    new_status = payload.status
    cursor.execute("UPDATE requests SET status = ? WHERE id = ?", (new_status, request_id))
    conn.commit()
    return {"status": new_status}