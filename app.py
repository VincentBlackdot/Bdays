from flask import Flask, render_template, request, jsonify, send_file
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv('EMAIL_USER')
SENDER_PASSWORD = os.getenv('EMAIL_PASSWORD')

def validate_email_config():
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        return False, "Email configuration is missing. Please set up EMAIL_USER and EMAIL_PASSWORD in .env file"
    return True, "Email configuration is valid"

# HTML email template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .birthday-card {{
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            font-family: Arial, sans-serif;
            color: white;
            margin: 20px auto;
            max-width: 600px;
        }}
        .message {{
            font-size: 24px;
            line-height: 1.5;
            margin: 20px 0;
        }}
        .bg-primary {{ background: linear-gradient(135deg, #4e54c8, #8f94fb); }}
        .bg-success {{ background: linear-gradient(135deg, #43a047, #66bb6a); }}
        .bg-info {{ background: linear-gradient(135deg, #0288d1, #4fc3f7); }}
        .bg-warning {{ background: linear-gradient(135deg, #fb8c00, #ffa726); }}
        .bg-danger {{ background: linear-gradient(135deg, #e53935, #ef5350); }}
    </style>
</head>
<body>
    <div class="birthday-card {background}">
        <div class="message">
            {message}
        </div>
    </div>
</body>
</html>
"""

# Birthday card templates with background colors and designs
TEMPLATES = [
    {
        "message": "Dear [NAME], wishing you a fantastic birthday filled with joy and laughter! 🎉",
        "background": "bg-primary",
        "design": "stars"
    },
    {
        "message": "Happy Birthday [NAME]! May your special day be as wonderful as you are! 🎂",
        "background": "bg-success",
        "design": "balloons"
    },
    {
        "message": "Hey [NAME]! Happy Birthday! Here's to another year of amazing adventures! 🎈",
        "background": "bg-info",
        "design": "confetti"
    },
    {
        "message": "To [NAME], sending you the warmest birthday wishes on your special day! 🎊",
        "background": "bg-warning",
        "design": "cake"
    },
    {
        "message": "Dearest [NAME], have a magical birthday filled with unforgettable moments! ✨",
        "background": "bg-danger",
        "design": "gifts"
    }
]

def get_personalized_message(template, name, custom_note=""):
    message = template["message"].replace("[NAME]", name)
    if custom_note:
        message += f"\n\n{custom_note}"
    return {
        "message": message,
        "background": template["background"],
        "design": template["design"]
    }

def send_birthday_email(recipient_email, message_data):
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Happy Birthday! 🎉"
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email

        # Create HTML version of the message
        html_content = HTML_TEMPLATE.format(
            message=message_data["message"].replace("\n", "<br>"),
            background=message_data["background"]
        )
        
        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))

        # Connect to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        return True, "Email sent successfully!"
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    return render_template('index.html', templates=TEMPLATES)

@app.route('/templates')
def view_templates():
    return render_template('templates.html', templates=TEMPLATES)

@app.route('/preview', methods=['POST'])
def preview_card():
    data = request.get_json()
    name = data.get('name', '')
    custom_note = data.get('custom_note', '')
    
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    template = random.choice(TEMPLATES)
    message = get_personalized_message(template, name, custom_note)
    return jsonify(message)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    custom_note = data.get('custom_note', '')
    
    if not all([name, email]):
        return jsonify({'error': 'Name and email are required'}), 400
    
    is_valid, message = validate_email_config()
    if not is_valid:
        return jsonify({'error': message}), 500
    
    template = random.choice(TEMPLATES)
    message = get_personalized_message(template, name, custom_note)
    
    success, result = send_birthday_email(email, message)
    if success:
        return jsonify({'message': result})
    else:
        return jsonify({'error': f'Failed to send email: {result}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
