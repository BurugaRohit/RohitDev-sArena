from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'some_secret'
mail = Mail(app)

#Gmail setting
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rohitdevsarena@gmail.com'
app.config['MAIL_PASSWORD'] = 'rohipra@70'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacts', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']
        mobilenumber = request.form['mobilenumber']
        msg = Message(sender='email', recipients = ['rohitdevsarena@gmail.com'] )
        msg.body = ("Username = {}\nMobile_number = {}\nE-mail = {}\nMessage = {}".format(username,mobilenumber,email,message))
        mail.send(msg)
        flash('Hola! Your Details Sent to Rohit - keep ツ', 'primary')
    return redirect(url_for('home'))

if __name__ == '__main__':

    app.run(debug=True)
