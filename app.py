from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_gmail@gmail.com'         # <-- your Gmail address
app.config['MAIL_PASSWORD'] = 'your-app-password'            # <-- your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'your_gmail@gmail.com'   # <-- your Gmail address

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if not name or not email or not message:
        flash('All fields are required.', 'error')
        return redirect(url_for('home') + '#contact')
    try:
        msg = Message(f'Portfolio Contact from {name}',
                      recipients=['your_gmail@gmail.com'])  # <-- your Gmail address
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        print(e)  # For debugging
        flash('An error occurred while sending your message. Please try again later.', 'error')
    return redirect(url_for('home') + '#contact')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume/<filename>')
def resume(filename):
     return send_from_directory('static/resume', filename)

@app.route('/extra curricular activities')
def achievements():
    return render_template('achievements.html')

@app.route('/educationalqualification')    
def educationalqualification():
    return render_template('education.html')

if __name__ == '__main__':
    app.run(debug=True) 