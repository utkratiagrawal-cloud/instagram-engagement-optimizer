# 🚀 Quick Start Guide

## Running the App Locally

### Step 1: Install Python
Ensure you have Python 3.8+ installed on your system.

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📋 First Time Setup (Detailed)

### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### macOS/Linux
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🧭 Navigation

Once the app is running:

1. **📊 Homepage** – Explore the purpose and benefits of the tool
2. **📊 Dataset Overview** – View data statistics and structure
3. **📈 Engagement Analysis** – Interactive visualizations of engagement patterns
4. **🔥 Engagement Heatmap** – Visual heatmap of hour × day combinations
5. **🎯 Recommendation Tool** – Get personalized posting recommendations
6. **ℹ️ About** – Learn about the technology and deployment options

---

## 🎛️ Using the Recommendation Tool

1. Navigate to **🎯 Recommendation Tool** tab
2. Use the sidebar filters to select:
   - **Content Category** (optional)
   - **Media Type** (optional)
3. View your personalized recommendations:
   - Best posting hour
   - Best posting day
   - Top 3 recommended hours
   - Top 3 recommended days
4. Get actionable insights and next steps

---

## 💡 Pro Tips

- **Clear Cache**: If visualizations don't update, clear the cache via menu (☰) → "Clear cache"
- **Full Screen**: Click the expand icon on any chart for fullscreen view
- **Export Data**: Use browser developer tools to save chart images
- **Multiple Users**: The app is stateless, so multiple users can use it simultaneously

---

## 📧 Troubleshooting

### App won't start
```bash
# Check Python version
python --version

# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### CSV file not found
- Verify `Instagram_Analytics.csv` is in the same folder as `app.py`
- Check the file name (case-sensitive on Linux/Mac)

### Port already in use
```bash
streamlit run app.py --server.port 8502
```

---

## 🌐 Deploying to the Cloud

See **README.md** for detailed deployment instructions for:
- Streamlit Community Cloud (Free)
- Render
- HuggingFace Spaces
- Heroku (Paid)

---

## 📞 Support

For issues or feature requests, refer to the main README.md file.

Happy analyzing! 🎉
