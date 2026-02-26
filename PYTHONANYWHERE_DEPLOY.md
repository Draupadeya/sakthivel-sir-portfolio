# PythonAnywhere Deployment Guide

This guide will help you deploy your Django portfolio to PythonAnywhere.

## Prerequisites
- PythonAnywhere account created: https://www.pythonanywhere.com/user/phanindrakilambi/
- GitHub repository ready: https://github.com/Draupadeya/sakthivel-sir-portfolio

## Deployment Steps

### Step 1: Clone Repository on PythonAnywhere
1. Go to PythonAnywhere and click **Bash console**
2. Run the following commands:
```bash
cd ~
git clone https://github.com/Draupadeya/sakthivel-sir-portfolio.git portfolio
cd portfolio
```

### Step 2: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.11 portfolio_env
pip install -r requirements.txt
```

### Step 3: Create .env File
```bash
nano .env
```
Add the following (generate a new SECRET_KEY):
```
SECRET_KEY=USE_A_SECURE_RANDOM_STRING_HERE
DEBUG=False
```
To generate a secure key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Then press Ctrl+O, Enter, Ctrl+X to save in nano.

### Step 4: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 7: Create Web App on PythonAnywhere
1. Go to **Web** tab in PythonAnywhere
2. Click **Add a new web app**
3. Choose **Manual configuration** (not "Web framework")
4. Choose **Python 3.11**
5. Click **Next**

### Step 8: Configure WSGI File
1. In the Web tab, you'll see a path like: `/var/www/phanindrakilambi_pythonanywhere_com_wsgi.py`
2. Click to edit this file
3. Replace the entire content with:

```python
import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = '/home/phanindrakilambi/portfolio'
sys.path.insert(0, project_dir)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 9: Configure Static Files
In the Web tab under "Static files":
1. URL: `/static/`
2. Directory: `/home/phanindrakilambi/portfolio/staticfiles`

Add another one:
1. URL: `/media/`
2. Directory: `/home/phanindrakilambi/portfolio/media`

### Step 10: Reload Web App
1. Click the green **Reload** button in the Web tab
2. Visit: `https://phanindrakilambi.pythonanywhere.com`
3. Your portfolio should now be live!

### Step 11: Admin Access
- Visit: `https://phanindrakilambi.pythonanywhere.com/admin/`
- Login with the superuser credentials you created in Step 6
- Edit your portfolio content from the Admin interface

## Troubleshooting

**Site shows 500 error:**
- Check error logs in PythonAnywhere Web tab
- Ensure .env file exists in the portfolio directory
- Run `python manage.py collectstatic --noinput` again

**Static files not loading:**
- Verify paths in Web tab match your actual directories
- Run `python manage.py collectstatic --noinput` again
- Check file permissions: `chmod -R 755 /home/phanindrakilambi/portfolio/staticfiles`

**Database errors:**
- Ensure migrations were run: `python manage.py migrate`
- Delete db.sqlite3 and re-migrate if needed

## File Structure on PythonAnywhere
```
/home/phanindrakilambi/portfolio/
├── portfolio/               (Django project folder)
├── home/                    (Django app)
├── templates/               (HTML templates)
├── static/                  (CSS, JS, images)
├── staticfiles/             (Collected static files for production)
├── db.sqlite3               (Database)
├── manage.py
├── requirements.txt
├── .env                     (Your environment variables - NOT in git)
└── .gitignore
```

## Updating Your Portfolio
To push updates from your local machine:
1. Make changes locally
2. Commit and push to GitHub:
```bash
git add .
git commit -m "Update portfolio content"
git push origin main
```
3. On PythonAnywhere bash console:
```bash
cd ~/portfolio
git pull origin main
python manage.py collectstatic --noinput
```
4. Reload the web app from the Web tab

Your changes will be live!
