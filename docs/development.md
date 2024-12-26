# Developer Documentation 💻

Technical documentation for developers who want to contribute to or modify the Birthday Card Generator.

## Project Structure

```
Bdays/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore rules
├── LICENSE            # MIT License
├── README.md          # Project overview
├── docs/              # Documentation files
├── static/
│   ├── style.css      # CSS styles
│   └── script.js      # JavaScript functions
└── templates/
    ├── index.html     # Main page template
    └── templates.html # Template preview page
```

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Email**: SMTP via Gmail
- **Styling**: Custom CSS with gradients
- **Dependencies**: See requirements.txt

## Core Components

### 1. Flask Routes (`app.py`)

```python
@app.route('/')
def index():
    # Renders main page
    return render_template('index.html', templates=TEMPLATES)

@app.route('/templates')
def view_templates():
    # Renders template preview page
    return render_template('templates.html', templates=TEMPLATES)

@app.route('/preview', methods=['POST'])
def preview_card():
    # Handles card preview generation
    # Returns JSON response with card data

@app.route('/send_email', methods=['POST'])
def send_email():
    # Handles email sending
    # Returns success/error response
```

### 2. Template System

Templates are defined in `app.py`:
```python
TEMPLATES = [
    {
        "message": "Template message with [NAME] placeholder",
        "background": "CSS background class",
        "design": "Design identifier"
    },
    # More templates...
]
```

### 3. Email System

- Uses SMTP protocol
- Supports HTML emails
- Includes error handling
- Configurable via environment variables

## Development Guidelines

### 1. Code Style

- Follow PEP 8 for Python code
- Use 4 spaces for indentation
- Keep functions focused and small
- Add docstrings to functions

### 2. Adding New Templates

1. Add template to `TEMPLATES` list:
```python
{
    "message": "New message with [NAME]",
    "background": "bg-new-class",
    "design": "new-design"
}
```

2. Add corresponding CSS in `style.css`:
```css
.bg-new-class {
    background: linear-gradient(...);
}
```

### 3. Error Handling

- Use try-except blocks for external operations
- Return meaningful error messages
- Log errors appropriately
- Handle both client and server errors

### 4. Testing

Manual testing points:
1. Template rendering
2. Email sending
3. Name personalization
4. Error scenarios
5. Mobile responsiveness

## Security Considerations

1. **Environment Variables**:
   - Never commit .env file
   - Use secure credentials
   - Rotate passwords regularly

2. **Input Validation**:
   - Sanitize user inputs
   - Validate email addresses
   - Prevent XSS attacks

3. **Email Security**:
   - Use App Passwords
   - Implement rate limiting
   - Validate email addresses

## Performance Optimization

1. **Frontend**:
   - Minimize DOM manipulation
   - Use event delegation
   - Optimize CSS selectors

2. **Backend**:
   - Cache templates
   - Optimize database queries
   - Use async operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow code style guidelines
4. Write clear commit messages
5. Submit a pull request

## Deployment

1. **Requirements**:
   - Python 3.8+
   - SMTP access
   - Environment variables set

2. **Steps**:
   ```bash
   git clone https://github.com/VincentBlackdot/Bdays.git
   cd Bdays
   pip install -r requirements.txt
   # Set up .env file
   python app.py
   ```

## Future Enhancements

1. **Features**:
   - User accounts
   - Template favorites
   - Scheduling
   - Custom designs

2. **Technical**:
   - API endpoints
   - Database integration
   - Image generation
   - Template editor
