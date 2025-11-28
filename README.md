# Job_Board_Platform_Backend

# **Job Board Backend**

A robust backend system built to power a modern Job Board platform with secure authentication, role-based access control, optimized job search, and comprehensive API documentation.

---

## 🚀 **Overview**

This project is a real-world backend engineering case study designed to simulate building a production-ready API for a Job Board.
It covers role management, job posting workflows, user authentication, and high-performance search capabilities.

---

## 📌 **Features**

### **🔐 Role-Based Authentication (JWT)**

* Secure login & registration
* Admin and User role separation
* Protected routes with permission enforcement

### **📄 Job Posting Management**

* Create, edit, delete, and view job listings
* Categorize jobs by industry, type, and location
* Pagination and sorting for large datasets

### **🎯 Optimized Job Search**

* Fast filtering by category, location, and job type
* PostgreSQL indexing to speed up queries
* Clean and efficient query patterns

### **📚 API Documentation**

Accessible Swagger UI:

```
/api/docs
```

---

## 🛠️ **Technologies Used**

| Technology             | Purpose                        |
| ---------------------- | ------------------------------ |
| **Django**             | Backend framework              |
| **PostgreSQL**         | Main database                  |
| **JWT**                | Authentication & authorization |
| **Swagger (drf-yasg)** | API documentation              |

---

## ⚙️ **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone github.com/qwabena37/job-board-backend.git
cd job-board-backend
```

### **2. Create Virtual Environment**

```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**

Create a `.env` file:

```
SECRET_KEY=your_secret_key
DATABASE_NAME=jobboard
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### **5. Run Migrations**

```bash
python manage.py migrate
```

### **6. Start Server**

```bash
python manage.py runserver
```

---

## 📁 **Project Structure**

```
jobboard-backend/
│
├── apps/
│   ├── accounts/         # Authentication & roles
│   ├── jobs/             # Job posting management
│   ├── applications/     # Job applications
│
├── config/               # Django project settings
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🔑 **API Endpoints Summary**

### **Auth**

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /auth/register | Register new user      |
| POST   | /auth/login    | Login & return JWT     |
| GET    | /auth/me       | Get authenticated user |

### **Jobs**

| Method | Endpoint   | Description        |
| ------ | ---------- | ------------------ |
| GET    | /jobs      | List jobs          |
| POST   | /jobs      | Create job (Admin) |
| GET    | /jobs/{id} | Retrieve job       |
| PUT    | /jobs/{id} | Update job (Admin) |
| DELETE | /jobs/{id} | Delete job (Admin) |

### **Categories**

| Method | Endpoint         | Description             |
| ------ | ---------------- | ----------------------- |
| GET    | /categories      | List categories         |
| POST   | /categories      | Create category (Admin) |
| DELETE | /categories/{id} | Delete category (Admin) |

### **Applications**

| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| POST   | /jobs/{id}/apply | User applies                |
| GET    | /applications    | Admin-only job applications |

---

## ⚡ **Database Optimization**

* Added indexes to:

  * `title`
  * `location`
  * `job_type`
  * `category`
* Optimized queries using:

  * `select_related()`
  * `prefetch_related()`
  * filtered lookups

---

## 🧪 **Running Tests**

```bash
python manage.py test
```

---

## 📄 **API Documentation**

Swagger UI available at:

```
/api/docs
```

Includes schemas, parameter descriptions, and response samples for all endpoints.

---

## 📝 **Git Workflow**

### Initial Setup

```
feat: set up Django project with PostgreSQL
```

### Feature Development

```
feat: implement job posting and filtering APIs
feat: add role-based authentication for admins and users
feat: add job application endpoints
```

### Performance Optimization

```
perf: optimize job search queries with indexing
```

### Documentation

```
feat: integrate Swagger for API documentation
docs: update README with setup instructions
```

---

## 📦 **Deployment**

Deploy using:

* Render
* Railway
* Heroku
* AWS / EC2
* Docker (optional)

Ensure environment variables and PostgreSQL database are configured.

---

## 📜 **License**

This project is open-source under the MIT License.

---


