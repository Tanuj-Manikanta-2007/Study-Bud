# StudyBud 📚

A Django-based study room discussion platform where users can create, join, and participate in topic-based chat rooms for collaborative learning and discussions. 💬✨

## ✨ Features

### 👤 User Management
- 📝 User registration and authentication
- 🎯 User profiles with activity history
- 🔐 Login/Logout functionality

### 🏠 Study Rooms
- ➕ Create discussion rooms with specific topics
- 🔍 Browse and search rooms by topic, name, or description
- 🚪 Join rooms as a participant
- 💬 Real-time messaging within rooms
- ✏️ Edit and delete your own rooms
- 👥 View room participants

### 💭 Messaging
- 📮 Post messages in study rooms
- 🗑️ Delete your own messages
- 📊 View recent activity feed
- 📜 Message history tracking

### 🏷️ Topics
- 📂 Organize rooms by topics
- 🎯 Filter rooms by topic categories
- 📋 View all available topics

## 🛠️ Technologies Used

- **Backend:** Django 5.2.8 🐍
- **Database:** Postgres SQL 💾
- **Frontend:** HTML, CSS, JavaScript 🎨
- **Authentication:** Django's built-in authentication system 🔒

## 📦 Installation

### ✅ Prerequisites
- Python 3.8 or higher 🐍
- pip (Python package manager) 📦

### 🚀 Setup Steps

1. **📥 Clone the repository**
   ```bash
   cd studybud
   ```

2. **🔧 Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **⚡ Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **📚 Install dependencies**
   ```bash
   pip install django
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
studybud/
├── base/                   # Main application
│   ├── api/               # REST API endpoints
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── admin.py          # Admin panel configuration
│   ├── forms.py          # Django forms
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   └── views.py          # View functions
├── studybud/             # Project settings
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── templates/            # Global templates
├── static/              # Static files (CSS, JS, images)
├── db.sqlite3           # SQLite database if you want ot use sqlite or postgres is my choice
└── manage.py            # Django management script
```

## 📖 Usage

### 👨‍🎓 For Users

1. **🔐 Register/Login**
   - Create an account or login with existing credentials
   - Navigate to `/register/` or `/login/`

2. **🔍 Browse Rooms**
   - View all available study rooms on the home page
   - Use the search bar to filter rooms by topic, name, or description

3. **➕ Create a Room**
   - Click "Create Room" (requires login)
   - Fill in room name, topic, and description
   - Submit to create your study room

4. **🚪 Join a Room**
   - Click on any room to enter
   - Send messages to participate in discussions
   - You'll automatically be added as a participant

5. **⚙️ Manage Your Content**
   - Edit or delete your own rooms
   - Delete your own messages
   - View your profile and activity history

### 👨‍💼 For Admins

1. 🔑 Access the admin panel at `/admin/`
2. 🛡️ Manage users, rooms, topics, and messages
3. 📊 Monitor platform activity and content

## 🗄️ Database Models

### 🏠 Room
- 👤 Host (User)
- 🏷️ Topic
- 📝 Name
- 📄 Description
- 👥 Participants (Many-to-Many with User)
- ⏰ Created/Updated timestamps

### 💬 Message
- 👤 User
- 🏠 Room
- 📝 Body (text content)
- ⏰ Created/Updated timestamps

### 🏷️ Topic
- 📝 Name

## 🛣️ URL Routes

- 🏠 `/` - Home page with room listings
- 🚪 `/room/<id>/` - Individual room view
- 👤 `/profile/<id>/` - User profile
- ➕ `/create-room/` - Create new room
- ✏️ `/update-room/<id>/` - Edit room
- 🗑️ `/delete-room/<id>/` - Delete room
- 🔐 `/login/` - User login
- 👋 `/logout/` - User logout
- 📝 `/register/` - User registration
- 🗑️ `/delete-message/<id>/` - Delete message

## 🔒 Security Notes

⚠️ **Important:** This project contains development settings that should be changed for production:

- 🔑 Change the `SECRET_KEY` in `settings.py`
- 🐛 Set `DEBUG = False` in production
- 🌐 Configure `ALLOWED_HOSTS` appropriately
- 💾 Use a production-grade database (PostgreSQL, MySQL)
- 📂 Set up proper static file serving
- 🔒 Enable HTTPS
- 🛡️ Implement additional security measures (CSRF, XSS protection, etc.)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 🎉

## 📄 License

This project is open source and available for educational purposes. 📖

## 📬 Contact

For questions or support, please open an issue in the repository. 💌

---

**Happy Learning! 📚✨🚀**
