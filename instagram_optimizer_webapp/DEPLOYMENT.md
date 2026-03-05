# 🚀 Deployment Guide

Complete instructions for deploying the Instagram Engagement Time Optimizer to various cloud platforms.

## 📊 Comparison Table

| Platform | Cost | Setup Time | Performance | Recommended |
|----------|------|-----------|-------------|------------|
| **Streamlit Cloud** | Free | 2 min | Fast | ⭐⭐⭐⭐⭐ |
| **HuggingFace Spaces** | Free | 3 min | Fast | ⭐⭐⭐⭐⭐ |
| **Render** | Free-$7/mo | 5 min | Good | ⭐⭐⭐⭐ |
| **Heroku** | Paid ($7-50/mo) | 5 min | Good | ⭐⭐⭐ |
| **Docker (Local)** | Free | 5 min | Excellent | ⭐⭐⭐⭐ |

---

## 1️⃣ Streamlit Community Cloud (RECOMMENDED)

**Best For:** Free, instant deployment with zero configuration  
**Setup Time:** 2 minutes  
**Cost:** Free  

### Steps:

1. **Create GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/instagram-optimizer.git
   git push -u origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Click "Sign in" and authenticate with GitHub
   - Click "New app"

3. **Configure Deployment**
   - Repository: Select your GitHub repo
   - Branch: `main`
   - File path: `app.py`
   - Advanced settings: (leave default)

4. **Deploy**
   - Click "Deploy"
   - Wait 30-60 seconds
   - App is live at `https://YOUR_USERNAME-instagram-optimizer.streamlit.app`

5. **Share Your App**
   - Copy the URL and share with anyone
   - No account needed to view

---

## 2️⃣ HuggingFace Spaces (EASIEST)

**Best For:** Quick deployment, community-focused  
**Setup Time:** 3 minutes  
**Cost:** Free  

### Steps:

1. **Create HuggingFace Account**
   - Go to https://huggingface.co
   - Sign up or log in

2. **Create New Space**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `instagram-optimizer`
   - Space type: **Streamlit**
   - Visibility: **Public**

3. **Upload Files**
   - Click "Files" tab
   - Click "Add file"
   - Upload:
     - `app.py`
     - `Instagram_Analytics.csv`
     - `requirements.txt`

4. **Auto Deploy**
   - HuggingFace automatically runs `app.py`
   - App is live after 1-2 minutes

5. **Create README.md**
   - Update README in the Space description
   - Add badges and information

---

## 3️⃣ Render

**Best For:** Flexible deployment with custom configurations  
**Setup Time:** 5 minutes  
**Cost:** Free tier available  

### Steps:

1. **Push to GitHub** (if not already done)
   ```bash
   git push -u origin main
   ```

2. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Select `instagram-optimizer` repository

4. **Configure Service**
   ```
   Name: instagram-optimizer
   Environment: Python 3
   Region: Choose closest to you
   Branch: main
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --logger.level=error
   Instance Type: Free (if available)
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment
   - App URL: `https://instagram-optimizer-xxxx.onrender.com`

6. **Keep App Alive** (Free tier)
   - Free tier apps spin down after 15 min inactivity
   - Upgrade to paid plan for continuous running

---

## 4️⃣ Heroku (Legacy Platform)

**⚠️ Note:** Heroku removed free tier in November 2022  
**Best For:** Traditional CI/CD workflows  
**Setup Time:** 5 minutes  
**Cost:** $7-50/month minimum  

### Steps (if using paid Heroku):

1. **Install Heroku CLI**
   ```bash
   npm install -g heroku
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **View App**
   ```bash
   heroku open
   ```

---

## 5️⃣ Docker (Local Deployment)

**Best For:** Full control, containerized environment  
**Setup Time:** 5 minutes  
**Cost:** Free (local) or $5-50/month (cloud)  

### Using Docker Locally:

```bash
# Build image
docker build -t instagram-optimizer .

# Run container
docker run -p 8501:8501 instagram-optimizer

# Access at http://localhost:8501
```

### Using Docker Compose:

```bash
# Start service
docker-compose up

# Stop service
docker-compose down
```

### Deploy Docker to Cloud:

**Option A: Docker Hub + Cloud Run (Google)**
```bash
# Build and push to Docker Hub
docker build -t yourusername/instagram-optimizer .
docker push yourusername/instagram-optimizer

# Deploy to Google Cloud Run
gcloud run deploy instagram-optimizer \
  --image yourusername/instagram-optimizer \
  --platform managed \
  --port 8501
```

**Option B: AWS ECR + ECS**
```bash
# Create ECR repository
aws ecr create-repository --repository-name instagram-optimizer

# Build and push
docker build -t instagram-optimizer .
docker tag instagram-optimizer:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/instagram-optimizer:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/instagram-optimizer:latest
```

---

## 🔒 Environment Variables

For sensitive data (if needed), create `.env` file (don't commit):

```ini
# .env (NEVER commit this file!)
DATABASE_URL=postgresql://user:password@host/db
API_KEY=your_api_key_here
SECRET_KEY=your_secret_key
```

### Using Secrets on Deployment Platforms:

**Streamlit Cloud:**
- Sidebar → Settings → Secrets → Add environment variables

**Render:**
- Service Settings → Environment → Add secret files

**HuggingFace Spaces:**
- Space Settings → Secrets → Add secret

**Heroku:**
```bash
heroku config:set DATABASE_URL=postgresql://...
```

---

## 📊 Monitoring & Maintenance

### View Logs

**Streamlit Cloud:**
- Logs appear in real-time in the app interface

**Render:**
```bash
# View logs
render logs --service instagram-optimizer
```

**Heroku:**
```bash
heroku logs --tail
```

**Docker:**
```bash
docker logs instagram-optimizer
```

### Performance Optimization

1. **Enable Caching**
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv(...)
   ```

2. **Increase Memory Limits**
   - Render: Upgrade to higher tier
   - Heroku: Use Professional dyno
   - Docker: Allocate more memory

3. **CDN for Static Files**
   - Streamlit Cloud: Built-in
   - Render: Built-in
   - Docker: Use nginx reverse proxy

---

## 🆘 Troubleshooting

### App won't deploy
```bash
# Check requirements.txt syntax
pip install -r requirements.txt

# Verify Python version (3.8+)
python --version

# Check for circular imports
python -m py_compile app.py
```

### Slow performance
- Check dataset size
- Enable Streamlit caching
- Upgrade to paid tier for better resources
- Optimize data processing

### Port conflicts
```bash
# Change port locally
streamlit run app.py --server.port 8502

# Or configure in .streamlit/config.toml
```

### Dataset not found
- Verify file exists in same directory as app.py
- Check file path is relative: `Instagram_Analytics.csv`
- For cloud: ensure file is committed to git

---

## 📈 Scaling Strategy

**Development:**
- Run locally with `streamlit run app.py`
- Test with Docker: `docker-compose up`

**Production (Small):**
- Use Streamlit Cloud (free)
- Monitor usage on dashboard

**Production (Medium):**
- Use Render or HuggingFace (free tier)
- Consider upgrade for better uptime

**Production (Large):**
- Use paid Render plan
- Add custom domain
- Enable analytics

---

## 🎯 Best Practices

1. **Version Control**
   ```bash
   git tag v1.0.0
   git push --tags
   ```

2. **Keep Secrets Safe**
   - Never commit `.env` files
   - Use platform-specific secret management

3. **Monitor Performance**
   - Check deployment logs regularly
   - Monitor error rates
   - Track user feedback

4. **Testing Before Deploy**
   ```bash
   streamlit run app.py
   # Test all features locally first
   git push origin develop  # to staging
   git push origin main  # to production
   ```

5. **Update Dependencies**
   ```bash
   pip list --outdated
   pip install -U streamlit pandas numpy
   pip freeze > requirements.txt
   ```

---

## 📞 Support

- **Streamlit Community:** https://discuss.streamlit.io
- **Render Docs:** https://render.com/docs
- **HuggingFace Help:** https://huggingface.co/help
- **Docker Docs:** https://docs.docker.com

---

## Summary

| Scenario | Recommended |
|----------|------|
| "I want instant, free deployment" | Streamlit Cloud |
| "I want community contributions" | HuggingFace Spaces |
| "I want more customization" | Render |
| "I want containerized setup" | Docker |
| "I need enterprise solutions" | Docker + Kubernetes |

**Get started now!** 🚀 Choose your platform and deploy in minutes.
