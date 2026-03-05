#!/bin/bash

# Streamlit configuration setup for cloud deployment
mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = \$PORT
enableCORS = false
enableXsrfProtection = true

[theme]
primaryColor = \"#E1306C\"
backgroundColor = \"#FFFFFF\"
secondaryBackgroundColor = \"#f0f2f6\"
textColor = \"#262730\"
font = \"sans serif\"

[logger]
level = \"warning\"

[client]
showErrorDetails = false
" > ~/.streamlit/config.toml
