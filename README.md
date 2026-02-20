Smart Service Request Portal

A full-stack service request portal that allows users to create service requests, view all requests, and update their status.

Features

1. Login
   - Enter token: `admin`

2. Create Service Requests
   - Fields: Title, Category, Description, Priority, Requester Name, Requester Email

3. View All Requests
   - Displays all requests
   - Columns: ID, Title, Status, Action

4. Update Status
   - Change status to: Open, In Progress, Resolved
   - Updates reflected immediately in the dashboard

5. Frontend & Backend
   - Frontend: HTML, CSS, JavaScript
   - Backend: Python (FastAPI/Flask) + SQLite

## How to Run the Project 

Step 1 — Clone the Project
1. Make sure Git is installed on your machine  
2. Open a terminal / command prompt and run:  
```bash
git clone https://github.com/Niveditha-Pannala/smart-service-request-portal.git
3. Navigate into the backend folder

Step-2 - Run the backend server:
uvicorn main:app --reload
Backend will run at: http://127.0.0.1:8000/
Open API docs at: http://127.0.0.1:8000/docs to test endpoints (POST /requests, GET /requests, PUT /requests/{id})
Keep this terminal open while using the frontend.

Step-3 - Open the Frontend
Navigate to frontend folder:
cd../frontend
python -m http.server 5500
-Open a browser and go to : http://127.0.0.1:5500/ (make sure backend is running)

Step-4 -Enter token: admin
Click Login
Dashboard appears with Create Request and All Requests sections.

Step 5 — Create a Service Request
Fill in all fields:
Title
Category
Description
Priority
Name
Email
Click Create Request
Request will appear in All Requests table.

Step 6 — Update Request Status
Click Update Status in Action column
Select new status: Open, In Progress, or Resolved
Click Update
A confirmation popup appears
Dashboard refreshes to show updated status

-- Notes for Clients
Backend must be running while using frontend
Backend URL: http://127.0.0.1:8000/
Frontend URL: http://127.0.0.1:5500/
Database is local SQLite, all data is stored on client’s machine
Token-based login is for demo purposes only



