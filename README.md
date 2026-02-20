# Smart Service Request Portal

## Overview
Smart Service Request Portal is a full-stack web application that allows users to create, view, and manage service requests. The portal provides a simple token-based login for demo purposes, a user-friendly dashboard to create and track requests, and an update mechanism for request status.  

## Problem
Many organizations struggle to track service requests efficiently. Manual tracking leads to lost requests, delays, and lack of transparency.  

## Problem Statement
Create a web-based portal that allows:  
- Users to submit service requests with detailed information  
- Admins or clients to view all requests  
- Users to update request status seamlessly without backend authentication complexity  

## Solution
A simple, interactive web portal with:  
- Token-based login (demo)  
- Request creation form  
- Dashboard showing all requests  
- Ability to update request status in real time  
- SQLite backend for storing request data  

## Features
- Token-based Login:Enter `admin` to access dashboard  
- Create Requests:Fill out title, category, description, priority, name, email  
- View All Requests:Table view with ID, title, status,action  
- Update Status:Change request status to Open, In Progress, or Resolved  
- Real-time Updates:Dashboard refreshes after status update  

## How to Run the Project 

Step 1 — Clone the Project
1. Make sure Git is installed on your machine  
2. Open a terminal / command prompt and run:  
```bash
git clone https://github.com/Niveditha-Pannala/smart-service-request-portal.git
3. Navigate into the backend folder

Step-2 - Run the backend server:
uvicorn main:app --reload
Backend will run at:[http://127.0.0.1:8000/]
Open API docs at: [http://127.0.0.1:8000/docs] to test endpoints (POST /requests, GET /requests, PUT /requests/{id})
Keep this terminal open while using the frontend.

Step-3 - Open the Frontend
Navigate to frontend folder:
cd../frontend
python -m http.server 5500
-Open a browser and go to : [http://127.0.0.1:5500/] (make sure backend is running)

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






