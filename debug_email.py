import smtplib
from email.mime.text import MIMEText

# Test the exact same configuration as your Flask app
username = 'sangamithramailsamy@gmail.com'
password = 'ovay zueb uomo qrfo'

print("Testing Gmail connection...")
print(f"Username: {username}")
print(f"Password: {password}")

try:
    # Connect to Gmail
    print("Connecting to Gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("TLS started successfully")
    
    print("Attempting login...")
    server.login(username, password)
    print("✅ Login successful!")
    
    # Test sending email
    msg = MIMEText('This is a test email from your portfolio app.')
    msg['Subject'] = 'Portfolio Test Email'
    msg['From'] = username
    msg['To'] = username
    
    print("Sending test email...")
    server.send_message(msg)
    server.quit()
    print("✅ Email sent successfully! Check your inbox.")
    
except smtplib.SMTPAuthenticationError as e:
    print(f"❌ Authentication failed: {e}")
    print("This means your App Password is incorrect or not set up properly.")
    
except smtplib.SMTPException as e:
    print(f"❌ SMTP error: {e}")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    print(f"Error type: {type(e).__name__}") 