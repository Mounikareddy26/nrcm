from flask import request,Flask,render_template,redirect
import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="nrcm"
)

cursor = mydb.cursor()

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def hello():
    if request.method == "POST":
        user = request.form['usernm']
        roll = request.form['rollno']
        email = request.form['mail']
        password = request.form['pwd']

        cursor.execute("INSERT INTO `users` set username=%s, roll_number=%s,email=%s,password=%s ",  (user, roll, email, password, ))
        mydb.commit()
        return redirect("/login")
    return render_template("form.html")

@app.route("/login")
def login():
    return render_template("index.html")


@app.route("/users")
def usersList():
    cursor.execute("SELECT* FROM USERS")    

    data=cursor.fetchall()
    return render_template("users.html",users=data)



if __name__ == "__main__":
    app.run(debug=True)