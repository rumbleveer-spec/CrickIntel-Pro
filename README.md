# 🏏 CrickIntel Pro

> AI-Powered Cricket Intelligence & Analysis Platform

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://crickintel-pro.example.com)
[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-3.0-green)](https://flask.palletsprojects.com/)

## ✨ Features

- 📊 **Live Match Tracking** - Real-time cricket match updates
- 🎯 **AI Predictions** - Machine learning powered match predictions
- 👤 **Player Analytics** - Comprehensive player statistics & performance analysis
- 📈 **Historical Data** - Access to extensive cricket databases
- 🌐 **Modern UI** - Beautiful, responsive interface

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Cricket API Key ([Get it from CricAPI](https://cricapi.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/rumbleveer-spec/CrickIntel-Pro.git
cd CrickIntel-Pro

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your CRICKET_API_KEY

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser!

## 🎯 Deployment

### Hostinger Deployment

1. **Upload Files**
   ```bash
   # Via FTP or File Manager
   - Upload all files to public_html/
   ```

2. **Setup Python Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure .htaccess** (auto-created)

4. **Set Environment Variables** in Hostinger control panel

5. **Start Application**
   ```bash
   gunicorn app:app --bind 0.0.0.0:8000
   ```

### Heroku Deployment

```bash
heroku create your-app-name
git push heroku main
heroku config:set CRICKET_API_KEY=your_key_here
heroku open
```

## 📁 Project Structure

```
CrickIntel-Pro/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── .env.example          # Environment variables template
├── templates/
│   └── index.html        # Main web interface
├── static/               # CSS, JS, images
└── README.md            # This file
```

## 🔧 Configuration

Edit `.env` file:

```env
CRICKET_API_KEY=your_actual_api_key
FLASK_ENV=production
SECRET_KEY=random_secret_key_here
```

## 📊 API Endpoints

- `GET /` - Main dashboard
- `GET /api/live-matches` - Fetch live matches
- `POST /api/match-prediction` - Get AI predictions
- `GET /api/player-stats?player_id=XXX` - Player statistics

## 🤝 Contributing

Contributions welcome! Open issues or submit PRs.

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- [CricAPI](https://cricapi.com) for cricket data
- Flask team for awesome framework
- Open source community

---

**Made with ❤️ for Cricket Fans**

[Live Demo](https://crickintel-pro.example.com) • [Report Bug](https://github.com/rumbleveer-spec/CrickIntel-Pro/issues) • [Request Feature](https://github.com/rumbleveer-spec/CrickIntel-Pro/issues)
