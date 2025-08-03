# 🧠 Learning Hub – A Django + Tailwind Project

Welcome to **Learning Hub**, a modern and responsive Django application built for showcasing frontend and DevOps integration. It includes interactive projects like a Todo App, Calculator, Music Player, Weather App, Password Generator, and more — all built with Django + Tailwind CSS + JavaScript.

<br>

## 🚀 Features

- 🔐 Custom Login & Signup system  
- 📄 User Profile page (view, edit, upload photo)  
- 🎨 Tailwind CSS + DaisyUI + GSAP + Barba.js  
- 📧 Contact form with email support  
- 🔁 Browser reload support  
- 📦 Fully Dockerized (no database required)

<br>

## 🧰 Tech Stack

- **Backend:** Django 5.x  
- **Frontend:** Tailwind CSS, DaisyUI, GSAP, Swiper, Barba.js  
- **Email:** Django email backend  
- **Dev Tools:** Docker, docker-compose

<br>

## 🐳 Run with Docker

> ⚠️ No database is required for this project.

### 🔧 Build & Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/djangobasicapp.git
cd djangobasicapp

# Build and run
docker-compose up --build
The app will be live at: http://localhost:8000

🗃️ Project Structure
djangobasicapp/
│
├── project1tweet/         # Main Django app
│   ├── templates/         # All HTML files
│   ├── static/            # JS, CSS, images
│   ├── views.py           # Views (Login, Signup, Projects)
│   └── urls.py
│
├── Dockerfile             # Docker setup
├── docker-compose.yml
├── requirements.txt
└── README.md


🛠️ Available Projects
✅ Todo App
🧮 Calculator
🎵 Music Player
🎨 Color Background Changer
🔐 Password Generator
☁️ Weather App
💰 Expense Tracker
🧲 Cursor Animation
✉️ Contact Form

Form submissions send email using Django’s configured SMTP backend. You can configure it in settings.py:
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "your@email.com"
EMAIL_HOST_PASSWORD = "yourpassword"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "your@email.com"
CONTACT_EMAIL = "your@email.com"

🔒 Authentication

Login / Signup with Django
Profile page includes:
Profile picture
Edit name & email
Logout
Email verification (customizable)

💡 DevOps Notes
Uses lightweight image with:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
You can replace this with gunicorn for production
Supports live reloading with django-browser-reload

📦 Future Enhancements
2FA Login
Light/Dark Theme Toggle
Profile picture upload via Cloudinary/S3
SQLite/PostgreSQL support

🤝 Contributing
Contributions are welcome! Fork the repository and submit a pull request.

📄 License
This project is open source and available under the MIT License.

---

Let me know if you also want the `Dockerfile` and `docker-compose.yml` again, or a production setup guide.

