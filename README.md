
# 🧠 Learning Hub - Django Web App

A modern and responsive Django web application built for learning and showcasing mini projects. Includes Tailwind CSS, user authentication, profile management, and Docker support.

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Django](https://img.shields.io/badge/Django-5.2-blue) ![Docker](https://img.shields.io/badge/Dockerized-Yes-blue)

---

## 🚀 Features

- 🌐 Multipage Django site (Projects, About, Contact)
- 🔐 User Authentication (Login, Signup, Logout)
- 👤 Profile Page with:
  - Avatar (auto-generated)
  - Editable Username and Email
  - Email verification
- 🎨 Fully responsive UI with **TailwindCSS + DaisyUI**
- ⚙️ Smooth UI/UX: GSAP, Swiper, Lenis, Barba.js
- 📦 Docker & Docker Compose Support
- 🛠 Mini Projects:
  - Todo App
  - Calculator
  - Cursor Animation
  - Password Generator
  - Color Changer
  - Music Player
  - Weather App
  - Expense Tracker

---

## 📁 Project Structure

```

djangobasicapp/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── project1tweet/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/
├── static/
└── ...

````

---

## 🐳 Docker Setup

### 1. Build the image
```bash
docker-compose build
````

### 2. Run the container

```bash
docker-compose up
```

Your app should be live at: `http://localhost:8000`

---

## 🧪 Local Development (without Docker)

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

---

## ⚙️ Tech Stack

* **Backend**: Django 5.x
* **Frontend**: Tailwind CSS, DaisyUI
* **Extras**: GSAP, Lenis, Swiper, Barba.js
* **Deployment**: Docker

---

## 🧑‍💻 Author

**Tanish Jain**

* [GitHub](https://github.com/05tanish)
* [LinkedIn](https://linkedin.com/in/tanish-jain-5b986828a)
* 📫 [tanishjain626@gmail.com](mailto:tanishjain626@gmail.com)

---

## 📄 License

This project is licensed under the MIT License.

```

---

Would you like me to create the file and push it to your project too, or do you want to copy-paste and save it yourself as `README.md` in the root of `djangobasicapp`?
```
