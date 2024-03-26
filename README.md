Document Management System

This is a document management system built using Django and Django REST Framework. It provides APIs for managing documents, including creating, updating, deleting, and sharing documents with others.

Features
User authentication: Users can sign up and log in to the system.
Document CRUD operations: Users can create, read, update, and delete documents.
Document sharing: Users can share documents with others and manage access to documents accordingly.

Installation

1. Clone the repository:
    https://github.com/nishan002/document_management.git

2. Create a virtual environment
    python3 -m venv venv
    source venv/bin/activate #for mac
    source venv/Script/activate #for windows

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Run the development server:
    python manage.py runserver

API Endpoints

User Authentication

POST /api/user/register/: Sign up a new user.
POST /api/user/login/: Log in an existing user.

Document Management

GET /api/documents/: List all documents.
POST /api/documents/: Create a new document.
GET /api/documents/<document_id>/: Retrieve a document.
PUT /api/documents/<document_id>/: Update a document.
DELETE /api/documents/<document_id>/: Delete a document.

Document Access Control

PUT /api/documents/<document_id>/access/: Add or update access for a document.

Authentication

Token-based authentication is used for API requests.
Include the authentication token in the Authorization header of your requests: Authorization: Token YOUR_TOKEN.


