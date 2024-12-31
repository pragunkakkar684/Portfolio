from flask import Flask,render_template,url_for,request,redirect,jsonify
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kakkarpragun.work@gmail.com'  
app.config['MAIL_PASSWORD'] = 'smkl vikx iuze bawk'  
app.config['MAIL_DEFAULT_SENDER'] = 'kakkarpragun.work@gmail.com'

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def services(page_name):
    return render_template(page_name)

# @app.route('/<string:html_page>')
# def portfo_details(html_page):
#     return render_template(html_page)

@app.route('/contact', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']

            msg = Message(
                subject=f"Portfolio Contact: {subject}",
                recipients=['kakkarpragun.work@gmail.com'],
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )

            mail.send(msg)
            return jsonify({'status': 'success', 'message': 'Your message has been sent successfully!'}), 200

        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)