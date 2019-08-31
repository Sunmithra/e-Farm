from flask import Flask, render_template, request
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
membersdb = myclient["mem_details"]

usrtable = membersdb["users"]

log_table=membersdb["log_table"]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/buy_items")
def buy_items():
    return render_template('buy_items.html')

	
	
@app.route("/rent")
def product():
    return render_template('rent2.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/regib4")
def regib4():
    return render_template('regib4.html')


@app.route("/login1", methods=['POST', 'GET'])
def login1():

    print("in login1")

    username=request.form.get("username")
    password=request.form.get("password")

    val = usrtable.find({'_id':username,"password":password})

    try:
        usr = val[0]
    except IndexError as e:
        return '<center><img src="'+"https://blog.sqlauthority.com/wp-content/uploads/2017/04/warning.png"+'"><h3>Username/password Error, please try again</h3>'



    return render_template('index.html')


@app.route('/send_contacts')
def send_contacts():
    return render_template('send_contacts.html')

@app.route('/land_contacts')
def land_contacts():
    return render_template('land_contacts.html')
@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route("/land_rentals")
def land_rentals():
    return render_template('land_rentals.html')

@app.route("/register")
def register():
    return render_template('vams_log.html')

@app.route("/register1",methods=['POST','GET'])
def register1():

    print("in register")

    username=request.form.get("username")
    password=request.form.get("password")
    email=request.form.get("email")
    f1=open('users.txt','w')
    f1.write("sunmithra")
    if username == '' or password == '' or email == '':
        return "<center><h3>Registration Failed, please try again"




    userinfo = { "_id": username, "password": password,"email":email }

    try:

        status=usrtable.insert_one(userinfo)

    except pymongo.errors.DuplicateKeyError as e:
        return "<center><h3>Registration Failed username "+ username+" Exists , please try again"

    return '<center><img src="'+"http://www.webtechlearning.com/wp-content/uploads/2017/06/thank.png"+'>'

@app.route('/upload')
def uploadd_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


app.run(debug=True)
