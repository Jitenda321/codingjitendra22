from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root@host:1234/codingthunders'
db = SQLAlchemy(app)
class Contacts(db.Model):
    srno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(20), nullable = False)
    phone_no = db.Column(db.String(20),nullable = False)
    mess = db.Column(db.String(80), nullable = False)
    date = db.Column(db.String(12), nullable =True)

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template("about.html")
@app.route("/contact", methods = ['GET','POST'])
def contacts():
    if(request.method == 'POST'):
        # '''Add etry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        phone = request.form.get('phone')

        entry = Contacts(name = name , phone_num = phone , mess= message, date =datetime.now(),email = email)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")
app.run(debug = True)