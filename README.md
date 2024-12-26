# Birthday Card Generator 🎉

A Flask-based web application that generates personalized birthday cards with beautiful designs and sends them via email.

## Features ✨

- 🎨 Random selection from multiple card designs
- 📝 Personalized messages with recipient's name
- 📧 Email sending capability
- 🖼️ Download cards as images
- 👀 Live preview of all templates
- 🎯 Responsive design
- ✨ Beautiful animations and gradients

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/VincentBlackdot/Bdays.git
cd Bdays
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Gmail credentials:
```
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASSWORD=your_app_password
```

4. Set up Gmail App Password:
   - Go to your [Google Account Settings](https://myaccount.google.com/)
   - Navigate to Security
   - Enable 2-Step Verification if not already enabled
   - Under 2-Step Verification, find "App passwords"
   - Generate a new App Password for Mail
   - Use this password in your .env file

## Usage 💻

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Features:
   - View all templates at `/templates`
   - Generate personalized cards
   - Send cards via email
   - Download cards as images

## Project Structure 📁

```
Bdays/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── style.css      # CSS styles
│   └── script.js      # JavaScript functions
├── templates/
│   ├── index.html     # Main page
│   └── templates.html # Template preview page
└── .env              # Environment variables (not in repo)
```

## Templates 🎨

The application includes five different templates with:
- Unique background gradients
- Custom animations
- Different design elements (stars, balloons, etc.)
- Personalized message placement

## Security 🔒

- Environment variables for sensitive data
- Gmail App Password for secure authentication
- .gitignore to prevent sensitive data exposure

## Contributing 🤝

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Documentation 📖

Detailed documentation is available in the `docs` directory:

- [Installation Guide](docs/installation.md) - How to set up the project
- [User Guide](docs/usage.md) - How to use the application
- [Developer Guide](docs/development.md) - Technical documentation
- [API Documentation](docs/api.md) - API endpoints and usage

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author ✍️

Vincent Siame

## Acknowledgments 🙏

- Flask framework
- Bootstrap for styling
- Font Awesome for icons
- Google Fonts for typography
