from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'YOUR_GMAIL_USERNAME'  #Gmail
app.config['MAIL_PASSWORD'] = 'YOUR_GMAIL_PASSWORD'  #Gmail password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.secret_key = 'some_random_secret_key'

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/one')
def page_one():
    return render_template('one.html')

@app.route('/two')
def page_two():
    return render_template('two.html')

@app.route('/three', methods=['GET', 'POST'])
def page_three():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        model = request.form['model']
        message_body = request.form['message']

        msg = Message('Mobile Repair Request', sender=email, recipients=['kubelelon@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nModel: {model}\n\n{message_body}"
        mail.send(msg)

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('page_three'))

    return render_template('three.html')

if __name__ == "__main__":
    app.run(debug=True)
