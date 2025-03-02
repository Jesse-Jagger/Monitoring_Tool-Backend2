# Server Monitoring Website Documentation

## Introduction

The **Server Monitoring Website** is a web application designed to track the uptime and downtime of registered servers. It provides real-time status updates, historical tracking, and alert notifications when a server goes down. The system consists of a Django backend and a React frontend, utilizing Celery for background tasks and Redis for caching.

---

## Features

### **1. Backend (Django & Django REST Framework)**

- User authentication using JWT (JSON Web Token)
- RESTful API for managing servers and monitoring data
- Periodic server status checks using Celery
- Database storage for server status history
- Email and SMS alerts for server downtime
- WebSockets for real-time updates
- Admin Users for this website

### **2. Frontend (React-Vite & Bootstrap)**

- User authentication and session management
- Interactive dashboard displaying different server statuses
- Real-time graphs and gauges for monitoring
- Ability to add, edit, and remove servers
- Notification system for alerts
- Reports on downtimes and being able to download in .csv and excel formats.
- Should be able to log out.
- Admin page that shows the User on the website

### **3. Background Tasks (Celery & Redis)**

- Scheduled periodic health checks for servers
- Email and SMS notifications when a server is down
- Redis caching for improved performance and reduced database queries

### **4. Role-Based Permissions**

The application implements Role-Based Access Control (RBAC) to ensure that users have access only to the features and data necessary for their responsibilities. Below are the permissions for each role:

#### Feature Access Matrix

| Features      	      |  Admin  | IT Staff | Developer | Customer Engagement | Flexipay Support| Ebanking Support |
| ---------------------   | ------- | -------- | --------- | ------------------- | --------------- | ---------------- |
| User Management	      |   ✅   |    ✅	|    ✅	  |         ❌	       |         ❌     |        ✅        |
| Server Management	      |   ✅	  |    ✅    |    ✅	  |         ❌	       |         ❌     |        ✅        |
| Real-Time Server Status |   ✅	  |    ✅	|    ✅	  |         ✅	       |         ✅     |        ✅        |
| Server Logs	          |   ✅	  |    ✅	|    ✅	  |         ❌	       |         ❌     |        ✅        |
| Alerts	              |   ✅	  |    ✅	|    ✅	  |         ✅	       |         ✅     |        ✅        |
| Reports	              |   ✅	  |    ✅	|    ✅	  |         ✅	       |         ✅     |        ✅        |
| Admin Dashboard	      |   ✅	  |    ✅	|    ✅	  |         ❌	       |         ❌     |        ✅        |
| System Settings	      |   ✅	  |    ✅	|    ✅	  |         ❌	       |         ❌     |        ✅        |
| API Access	          |   ✅	  |    ❌	|    ✅	  |         ❌	       |         ❌     |        ❌        |
| Codebase Access	      |   ✅	  |    ❌	|    ✅	  |         ❌	       |         ❌     |        ❌        |

#### Summary

- Admins & Developers have full access to all features.

- IT Staff & Ebanking Support can manage servers, logs, alerts, reports and system settings access excluding API and Codebase Access.

- Customer Engagement & Flexipay Support have limited access focused on real-time monitoring and alerts.

---

## Technology Stack

| Component  | Technology Used                                |
| ---------- | ---------------------------------------------- |
| Frontend   | React-Vite, Bootstrap, WebSockets                   |
| Backend    | Django, Django REST Framework                  |
| Database   | PostgreSQL (Production) / SQLite (Development) |
| Task Queue | Celery                                         |
| Caching    | Redis                                          |
| Deployment | Docker, AWS/DigitalOcean/Vercel/GCC            |

---

## Project Structure

```
server_monitor/
├── backend/
│   ├── manage.py
│   ├── server_monitor/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── monitoring/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   ├── users/
│   │   ├── authentication.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   |    ├── Navbar.jsx
│   │   |    ├── Sidebar.jsx
│   │   ├── pages/
│   │   |    ├── Login.jsx
│   │   |    ├── Dashboard.jsx
│   │   |    ├── Reports.jsx
│   │   |    ├── Servers.jsx
│   │   |    ├── Alerts.jsx
│   │   |    ├── Settings.jsx
│   │   |    ├── Admin.jsx
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
├── docker-compose.yml
├── README.md
```

---

## Backend Implementation

### **1. Setting Up Django Project**

```bash
django-admin startproject server_monitor
cd server_monitor
python manage.py startapp monitoring
```

---

## Frontend Implementation (React)

### **1. Setting Up the React Project**

```bash
npx create-react-app monitor-frontend
cd monitor-frontend
npm install axios react-bootstrap recharts jwt-decode
```


## Authentication (JWT)

- **Backend:** Use Django **djangorestframework-simplejwt**
- **Frontend:** Store JWT token in **localStorage**
- **Refresh token** support for long-lived sessions

---

## Deployment

### **Backend Deployment**

- Use **Docker** to containerize Django API
- Deploy on **AWS/DigitalOcean** with PostgreSQL
- Use **Celery & Redis** with Supervisor for background tasks

### **Frontend Deployment**

- Deploy React app on **Vercel or Netlify**
- Use **NGINX as a reverse proxy** for the Django API

---

## Additional Features

✅ **Real-time updates** using WebSockets
✅ **Advanced visualizations** with Grafana
✅ **SMS alerts** via Twilio
✅ **Monitoring API integration** for external services

---

## Conclusion

This documentation outlines the complete architecture and implementation of the Server Monitoring Website. The system ensures real-time tracking, reliable alerts, and an intuitive dashboard for users. Future enhancements can include AI-based failure prediction, advanced logging, and third-party API integrations.
