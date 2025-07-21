# My Professional Portfolio (Flask)

A professional portfolio website built with Flask. Features a modern design, About and Projects pages, and a functional contact form.

## Features

- Home, About, and Projects pages
- Responsive, modern design
- Contact form (sends email via Flask-Mail)

## Setup

1. **Clone the repository**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Configure email settings:**
   - Edit `app.py` and set your email, password, and secret key in the configuration section.
4. **Run the app:**
   ```
   python app.py
   ```
   Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Deployment

- Use a production server like Gunicorn or uWSGI for deployment.
- Set `debug=False` in `app.py` for production.
- Use environment variables for sensitive config (email, secret key).
- Deploy on platforms like Heroku, PythonAnywhere, or your own VPS.

---

Feel free to customize the content and design to match your professional profile!
