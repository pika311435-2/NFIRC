import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def send_email(message):
    sender_email = "your_gmail_username@gmail.com"  # Replace with your Gmail address
    sender_password = "your_gmail_password"  # Replace with your Gmail password or an app password
    receiver_email = "311435@gm.tntcsh.tn.edu.tw"

    msg = MIMEText(message)
    msg['Subject'] = "社團網頁訊息"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False

@app.route('/send_message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data['message']
    if send_email(message):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)
