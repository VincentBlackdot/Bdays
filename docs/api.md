# API Documentation 🔌

## Endpoints

### 1. Preview Card

```http
POST /preview
```

Generate a preview of a birthday card.

#### Request Body
```json
{
    "name": "string",
    "custom_note": "string (optional)"
}
```

#### Response
```json
{
    "message": "string",
    "background": "string",
    "design": "string"
}
```

#### Error Response
```json
{
    "error": "string"
}
```

### 2. Send Email

```http
POST /send_email
```

Send a birthday card via email.

#### Request Body
```json
{
    "name": "string",
    "email": "string",
    "custom_note": "string (optional)"
}
```

#### Response
```json
{
    "message": "string"
}
```

#### Error Response
```json
{
    "error": "string"
}
```

## Status Codes

- `200`: Success
- `400`: Bad Request
- `500`: Server Error

## Rate Limiting

- 100 requests per hour per IP
- Email sending limited to 50 per day

## Data Formats

### Template Object
```json
{
    "message": "string with [NAME] placeholder",
    "background": "CSS class name",
    "design": "design identifier"
}
```

### Error Object
```json
{
    "error": "Error description",
    "code": "Error code (optional)",
    "details": "Additional details (optional)"
}
```

## Examples

### Preview Card Request
```curl
curl -X POST http://localhost:5000/preview \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "custom_note": "Happy Birthday!"}'
```

### Send Email Request
```curl
curl -X POST http://localhost:5000/send_email \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com", "custom_note": "Happy Birthday!"}'
```

## Security

- HTTPS recommended for production
- API keys for future versions
- Input validation on all endpoints
- XSS protection implemented
- CORS policies enforced

## Error Handling

Common error responses:

1. Missing Required Fields
```json
{
    "error": "Name and email are required"
}
```

2. Invalid Email Format
```json
{
    "error": "Invalid email format"
}
```

3. Email Sending Failed
```json
{
    "error": "Failed to send email: detailed error message"
}
```

## Future API Features

1. **Authentication**:
   - API key support
   - OAuth integration
   - Rate limiting per API key

2. **New Endpoints**:
   - Custom template creation
   - Template management
   - User preferences
   - Analytics

3. **Enhanced Responses**:
   - Detailed success metrics
   - Preview images
   - Template suggestions
