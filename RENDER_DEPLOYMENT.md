# Render + Supabase Deployment Guide

## Step-by-Step Setup

### 1. Create Supabase Account & Database
1. Go to https://supabase.com
2. Sign up and create a new project
3. Wait for database to initialize
4. Go to **Settings > Database** to find your connection string
5. Copy the PostgreSQL connection URL (looks like: `postgresql://postgres:password@host.supabase.co:5432/postgres`)
6. Save this - you'll need it for Render environment variables

### 2. Create Render Account & Web Service
1. Go to https://render.com
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**
4. Connect your GitHub repository
5. Fill in the configuration:

**Basic Settings:**
- **Name**: `codecrux` (or your project name)
- **Environment**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn portfolio.wsgi:application`

### 3. Add Environment Variables in Render
In the Render dashboard, go to **Environment**:

```
SECRET_KEY=<generate a new Django secret key>
DEBUG=False
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@YOUR_HOST.supabase.co:5432/postgres
ALLOWED_HOSTS=your-app-name.onrender.com
```

**To generate a SECRET_KEY**, run this locally:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 4. Deploy
Click **"Create Web Service"** - Render will:
1. Pull your code from GitHub
2. Run `build.sh` (collects static files, runs migrations)
3. Start the Django server with gunicorn
4. Your app will be live at `https://your-app-name.onrender.com`

### 5. Important Notes

**Cold Start:**
- Free tier spins down after 15 minutes of inactivity
- First request takes ~30 seconds (cold start)
- Solution: Upgrade to paid tier (~$7/month) for always-on

**Deployments:**
- Every push to your main branch triggers automatic deployment
- Check deployment logs in Render dashboard if something fails

**Database:**
- Supabase free tier has 500MB storage
- Backups are automatic
- You can manage database via Supabase dashboard

**Static Files & Media:**
- WhiteNoise serves static files (CSS, JS, images)
- Media uploads will be stored in Supabase database as blobs or use external storage

### 6. Testing Locally (Optional)

To test with PostgreSQL locally before deploying:

```bash
# Install postgres locally or use Docker
# Set DATABASE_URL in .env
# Create .env with:
# DATABASE_URL=postgresql://user:password@localhost:5432/portfolio
# DEBUG=True

python manage.py migrate
python manage.py runserver
```

### 7. Troubleshooting

**"Module not found" errors:**
- Check requirements.txt has all dependencies
- Redeploy after updating requirements.txt

**Database connection fails:**
- Verify DATABASE_URL is correct in Supabase settings
- Check Supabase project is running (go to Supabase dashboard)
- Ensure IP is whitelisted (Supabase → Settings → Network)

**Static files not loading:**
- Run `python manage.py collectstatic` locally to verify
- Check STATIC_URL and STATIC_ROOT in settings.py

**Media files not working:**
- Consider using AWS S3 or similar for production media storage
- For now, storing in database works for small projects

## Quick Redeploy

After making changes locally:
```bash
git add .
git commit -m "Your changes"
git push origin main  # Render auto-deploys
```

## Next Steps

- Set up staging environment (optional but recommended)
- Configure custom domain
- Set up monitoring/alerts
- Implement feature flags for gradual rollout
