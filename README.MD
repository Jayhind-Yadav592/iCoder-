# iCoder 📝

> This Ultimate Coding Companion - A Modern Blogging Platform for Developers

![iCoder Banner](https://via.placeholder.com/1200x400/667eea/ffffff?text=iCoder+-+Where+Developers+Share+Knowledge)

[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About

**iCoder** is a modern, feature-rich blogging platform designed specifically for developers and tech enthusiasts. Share your coding journey, tutorials, and technical insights with a vibrant community of fellow developers.

### Why iCoder?

- 📝 **Clean & Intuitive Interface** - Focus on writing, not fighting with the UI
- 💬 **Engaging Discussions** - Nested comments and reply system
- 🎨 **Beautiful Design** - Professional, modern, and responsive
- 🔍 **Powerful Search** - Find content quickly and efficiently
- 👥 **Community Driven** - Connect with developers worldwide

---

## ✨ Features

### Core Features
- ✅ **User Authentication** - Secure login/signup with Django auth
- ✅ **Blog Management** - Create, edit, and delete blog posts
- ✅ **Rich Text Editor** - Write formatted content with ease
- ✅ **Comment System** - Nested comments with replies
- ✅ **Search Functionality** - Advanced search across posts
- ✅ **View Counter** - Track post popularity
- ✅ **Category Filtering** - Organize content by topics
- ✅ **Responsive Design** - Works seamlessly on all devices

### Advanced Features
- 🎨 **Dynamic Avatars** - Unique user avatars based on username
- 🏷️ **Tags & Categories** - Easy content organization
- 📱 **Mobile Optimized** - Perfect experience on phones and tablets
- 🔔 **Notifications** - Success/error messages for user actions
- ⚡ **Fast Performance** - Optimized database queries

---

## 🛠️ Tech Stack

### Backend
- **Django 6.0** - High-level Python web framework
- **Python 3.14** - Programming language
- **SQLite** - Database (can be switched to PostgreSQL)

### Frontend
- **HTML5 & CSS3** - Structure and styling
- **Bootstrap 5.3** - Responsive CSS framework
- **JavaScript (ES6+)** - Dynamic interactions
- **Font Awesome** - Icon library

### Additional Libraries
- **Django Humanize** - Natural time formatting
- **Pillow** - Image processing (if using thumbnails)

---

## 🚀 Installation

### Prerequisites
```bash
- Python 3.8 or higher
- pip (Python package manager)
- Git
```

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/icoder.git
cd icoder
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Step 6: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 📖 Usage

### Creating a Blog Post

1. **Login** to your account
2. Navigate to **Admin Panel** (`/admin`)
3. Go to **Posts** → **Add Post**
4. Fill in:
   - Title
   - Content (supports HTML)
   - Slug (URL-friendly)
   - Author name
5. Click **Save**

### Managing Comments

- Users must be logged in to comment
- Comments support nested replies
- Admin can moderate from admin panel

### Search Functionality

- Use the search bar in navigation
- Search by:
  - Post title
  - Content
  - Author name

---

## 📁 Project Structure
```
icoder/
│
├── blog/                      # Main blog app
│   ├── migrations/           # Database migrations
│   ├── templatetags/         # Custom template filters
│   │   ├── __init__.py
│   │   └── extras.py        # get_user_image, get_val filters
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── models.py            # Post, Comment, Contact models
│   ├── urls.py              # Blog URL patterns
│   └── views.py             # View functions
│
├── home/                      # Main home app
│   ├── migrations/           # Database migrations    
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── models.py            # Contact models
│   ├── urls.py              # home URL patterns
│   └── views.py  
|        
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   ├──blog/
│   |   ├── blogHome.html    # Blog listing
│   |   ├── blogPost.html    # Single post detail
│   ├── home/
│       ├── home.html         # Home page
|       ├── about.html        # About page
|       ├── contact.html      # Contact page
|       |── serach.html       # serach page
|
├── static/                   # Static files
│   └── img/
│       ├── user1.png        # User avatars
│       ├── user2.png
│       └── ...
│
├── iCoder/                   # Project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
│
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

---

## 🔧 Configuration

### Settings.py Important Configurations
```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media Files (for uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 🎨 Customization

### Changing Color Scheme

Edit `static/css/style.css` or inline styles:
```css
/* Primary gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to your colors */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

### Adding New Pages

1. Create view in `blog/views.py`
2. Add URL pattern in `blog/urls.py`
3. Create template in `templates/`

### User Avatars

Images are automatically assigned based on username hash:
- Located in: `static/img/user1.png` to `user6.png`
- Replace with your own images (keep same names)

---

## 🐛 Troubleshooting

### Common Issues

**Issue: Static files not loading**
```bash
python manage.py collectstatic --clear
```

**Issue: Template filter error**
```bash
# Ensure templatetags/__init__.py exists
# Restart server after creating filters
```

**Issue: Database errors**
```bash
# Reset migrations
python manage.py migrate --run-syncdb
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Write descriptive commit messages
- Add comments for complex logic
- Test before submitting PR

---

## 📝 Requirements
```txt
Django==6.0
Pillow==10.0.0
```

Save as `requirements.txt`

---

## 🎯 Roadmap

### Upcoming Features

- [ ] User profiles with bio
- [ ] Email notifications
- [ ] Social media integration
- [ ] Code syntax highlighting
- [ ] Markdown support
- [ ] Draft posts
- [ ] Post scheduling
- [ ] Analytics dashboard
- [ ] RSS feed
- [ ] API endpoints

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
```
MIT License

Copyright (c) 2026 iCoder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author

**JAYHIND YADAV**

- GitHub: [@Jayhind-Yadav592](https://github.com/Jayhind-Yadav592)
- LinkedIn: [Jayhind Yadav](https://www.linkedin.com/in/jayhind-yadav-54ab3b33a)
- Email: jayhind01022003gmail.com

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists
- [Bootstrap](https://getbootstrap.com/) - Build responsive websites
- [Font Awesome](https://fontawesome.com/) - Icon library
- [Unsplash](https://unsplash.com/) - Free images

---

## 📞 Support

If you found this helpful, please ⭐ star this repository!
