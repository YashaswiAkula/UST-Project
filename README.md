# 🎫 Customer Support Ticketing System

A **role-based customer support ticketing system** built using **FastAPI** and **Tkinter**, designed to manage customer issues efficiently by tracking tickets, assigning support staff, and monitoring resolution progress.

---

## 📌 Project Description

The **Customer Support Ticketing System** enables organizations to handle customer issues in a structured and transparent manner.  
It supports ticket lifecycle management, priority handling, role-based access control, and analytics — providing a complete end-to-end support workflow.

---

## 🎯 Objectives

- Implement complete ticket lifecycle management
- Handle priority and status transitions
- Apply robust exception handling
- Enforce role-based access control
- Provide analytics and reporting endpoints

---

## 🛠 Tools & Technologies

| Category | Technology |
|--------|------------|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Frontend | Tkinter (Desktop UI) |
| Database | SQLite |
| Authentication | JWT (Cookie-based) |
| ORM | SQLAlchemy |
| Testing | pytest |
| Version Control | Git |

---

## 👥 User Roles & Capabilities

### 🛡 Admin
- Manage users
- Assign tickets
- Update ticket status
- View analytics and reports

### 🧑‍🔧 Helper
- View assigned tickets
- Update ticket status
- Add internal comments

### 👤 Customer
- Create tickets
- View own tickets
- Add comments

---

## ✨ Key Features

### 🎫 Ticket Management
- Ticket creation and updates
- Priority handling
- Status transitions (Open → In Progress → Resolved → Closed)

### 🧑‍💼 Role-Based Access
- Separate dashboards for Admin, Helper, and Customer
- Permission-based access enforcement

### 💬 Comment System
- Public comments (customer-visible)
- Internal comments (staff-only)
- Ticket-wise discussion history

### 📊 Analytics & Reporting
- Ticket statistics
- Staff performance tracking
- Resolution progress insights

### 🔐 Authentication & Security
- JWT-based authentication (cookie-based)
- Secure session handling
- Logout functionality

### 🎨 User Interface
- Dark-themed Tkinter UI
- Desktop-friendly experience
- Clean and intuitive navigation

---
```md
## 🗂 Project Structure

```bash
PROJECT-CUSTOMER-TICKET/
├── app/
│   ├── app.py
│   ├── auth.py
│   ├── users.py
│   ├── allocation.py
│   ├── analytics.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── permissions.py
│   ├── demo_roles.py
│   └── tickets.db
│
├── frontend/
│   ├── main.py
│   ├── api_client.py
│   ├── theme.py
│   ├── utils.py
│   ├── auth_ui.py
│   ├── admin_ui.py
│   ├── helper_ui.py
│   ├── customer_ui.py
│   └── comments_ui.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_tickets.py
│   └── test_comments.py
│
├── requirements.txt
└── README.md
```

## ▶️ How to Run the Project

### 🔹 Backend (FastAPI)

```bash
uvicorn app.app:app --reload
```
### Swagger API Docs:
```bash
(http://127.0.0.1:8000/docs)
```
### 🔹 Frontend (Tkinter Desktop App)
```bash
python frontend/main.py
```
### 🧪 Testing

### Run automated tests using:
```bash
pytest tests/
```

