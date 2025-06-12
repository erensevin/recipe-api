# Recipe Scraper API

A simple and secure FastAPI-based web service that scrapes recipe data from various cooking websites. The API extracts recipe titles and ingredients from provided URLs with built-in authentication for secure access. 

## Supported Websites

This API uses the [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) library, which supports over 500+ recipe websites including:
- AllRecipes
- Food Network
- Epicurious
- BBC Good Food
- And many more...

## Quick Start

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd recipe-api
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```bash
   AUTH_USERNAME=your_username
   AUTH_PASSWORD=your_password
   ```

4. **Run the server**:
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET /
Welcome endpoint that provides basic API information.

**Response:**
```json
{
  "message": "Welcome to the Recipe Scraper API!"
}
```

### POST /scrape (Protected)
Scrapes recipe data from a provided URL.

**Authentication:** Basic Auth required

**Request Body:**
```json
{
  "url": "https://example-recipe-website.com/recipe-page"
}
```

**Successful Response:**
```json
{
  "title": "Delicious Chocolate Cake",
  "ingredients": [
    "2 cups all-purpose flour",
    "1 cup sugar",
    "1/2 cup cocoa powder",
    "..."
  ]
}
```

**Error Response:**
```json
{
  "error": "Website not implemented for scraping yet"
}
```

## Usage Examples

### Using curl

```bash
# Basic request with authentication
curl -u your_username:your_password \
  -X POST "http://localhost:8000/scrape" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.allrecipes.com/recipe/example"}'
```

### Using Python requests

```python
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8000/scrape"
auth = HTTPBasicAuth("your_username", "your_password")
data = {"url": "https://www.allrecipes.com/recipe/example"}

response = requests.post(url, json=data, auth=auth)
recipe = response.json()
print(f"Recipe: {recipe['title']}")
```

### Using JavaScript (fetch)

```javascript
const url = 'http://localhost:8000/scrape';
const auth = btoa('your_username:your_password');

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Basic ${auth}`
  },
  body: JSON.stringify({
    url: 'https://www.allrecipes.com/recipe/example'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `AUTH_USERNAME` | Username for basic authentication | Yes |
| `AUTH_PASSWORD` | Password for basic authentication | Yes |

### Security

- **Never commit the `.env` file** to version control
- Use strong, unique passwords for production
- Consider using environment-specific credentials for different deployment stages

## Error Handling

The API handles several types of errors:

- **Authentication Errors (401)**: Invalid or missing credentials
- **Configuration Errors (500)**: Missing environment variables
- **Scraping Errors**: Website not supported or scraping failed
- **General Errors**: Network issues, invalid URLs, etc.

## Development

### Project Structure

```
recipe-api/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (not in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

### Running in Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Adding to .gitignore

Make sure to add the following to your `.gitignore`:

```
.env
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
```

## License

This project is open source and available under the [MIT License](LICENSE).
