# TRAR HR Consulting Web Application

Flask-based dynamic web application with a tree-structured service component model, designed for deployment on GoDaddy cPanel using Passenger WSGI.

## Features

- Home, About, Services, Contact tabs
- Dynamic component pages from JSON tree data
- Responsive templates and static assets
- 1920x1080 SVG HR consulting images (high definition)
- cPanel Passenger deployment files included

## Project Structure

- app/
  - routes/
  - content/pages.json
  - templates/
  - static/
- passenger_wsgi.py
- startup.py
- requirements.txt
- .htaccess

## Local Run

1. Create venv and install dependencies.
2. Run:

```bash
python startup.py
```

Then open http://127.0.0.1:5000.

## GoDaddy cPanel Deployment

1. In cPanel, create a Python Application (Setup Python App).
2. Choose Python 3.11 (or closest available).
3. Set Application Root to public_html (or your desired folder).
4. Upload project files to the Application Root.
5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Ensure [passenger_wsgi.py](passenger_wsgi.py) exists at app root.
7. Update [.htaccess](.htaccess) placeholders:
   - Replace USERNAME with your cPanel username.
   - Verify PassengerPython points to your virtualenv binary path in cPanel.
8. Restart app from cPanel Python App dashboard.

## Notes

- The SVG assets are production-ready placeholders and can be replaced with branded photography.
- All tab labels and component tree data can be edited in app/content/pages.json.
