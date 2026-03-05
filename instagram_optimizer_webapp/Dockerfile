FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY Instagram_Analytics.csv .
COPY setup.sh .

# Create .streamlit directory and config
RUN mkdir -p ~/.streamlit && \
    echo "[server]\nheadless = true\nport = 8501\nenableCORS = false\nenableXsrfProtection = true\n\n[theme]\nprimaryColor = \"#E1306C\"\nbackgroundColor = \"#FFFFFF\"\nsecondaryBackgroundColor = \"#f0f2f6\"\ntextColor = \"#262730\"\nfont = \"sans serif\"\n\n[logger]\nlevel = \"warning\"\n\n[client]\nshowErrorDetails = false" > ~/.streamlit/config.toml

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run the app
CMD ["streamlit", "run", "app.py"]
