# Installation Guide 🚀

This guide will help you set up the Birthday Card Generator on your local machine.

## Prerequisites

- Python 3.8 or higher
- Git
- Gmail account
- pip (Python package manager)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VincentBlackdot/Bdays.git
cd Bdays
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Email Settings

1. **Enable 2-Step Verification in Gmail**:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2-Step Verification if not already enabled

2. **Generate App Password**:
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and your device
   - Copy the generated 16-character password

3. **Create Environment File**:
   - Create a `.env` file in the root directory
   - Add your Gmail credentials:
   ```
   EMAIL_USER=your_gmail@gmail.com
   EMAIL_PASSWORD=your_16_character_app_password
   ```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Troubleshooting

### Common Issues

1. **Email sending fails**:
   - Verify your Gmail credentials in `.env`
   - Ensure 2-Step Verification is enabled
   - Check if App Password is correct (no spaces)

2. **Dependencies installation fails**:
   - Upgrade pip: `python -m pip install --upgrade pip`
   - Install dependencies one by one to identify the problematic package

3. **Application won't start**:
   - Check if port 5000 is available
   - Verify Python version compatibility
   - Ensure all required files are present

### Getting Help

If you encounter any issues:
1. Check the [Issues](https://github.com/VincentBlackdot/Bdays/issues) page
2. Create a new issue with detailed information about your problem
3. Include error messages and your environment details
