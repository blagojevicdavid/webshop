from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import date
import runpy

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#([('ime', 'David'), ('prezime', 'Blagojevic'), ('registerEmail', 'davidblagojevic7@gmail.com'), ('brojTelefona', '066498934'), ('password', '12345678'), ('btn', 'Register')])
class Database():
    def __init__(self):
        connection = sqlite3.connect("database.db", check_same_thread=False)
        crsr = connection.cursor()
        self.crsr = crsr
        self.connection = connection
        

    def all(self):
        crsr = self.crsr
        connection = self.connection
        crsr.execute("""SELECT * FROM users""")
        ans= crsr.fetchall()
        print(ans)
        connection.commit()
        #connection.close()


    def datapassword(self, email):
        crsr = self.crsr
        connection = self.connection
        crsr.execute("""SELECT * FROM users """)
        ans= crsr.fetchall()
        for i in range(0, len(ans)):
            if ans[i][3] == email:
                return ans[i][5]
        connection.commit()
        #connection.close()


    def newuser(self, ime, prezime, email, brojtelefona, password):
        dat = str(date.today())
        crsr = self.crsr
        connection = self.connection
        crsr.execute('INSERT INTO users VALUES (NULL, "' + ime + '", "' + prezime + '", "' + email + '", "' + brojtelefona + '", "' + password + '", NULL, NULL, NULL, "' + dat + '" )')
        connection.commit()
        #connection.close()

    def check_for_email(self, email):
        crsr = self.crsr
        #connection = self.connection
        crsr.execute("""SELECT * FROM users """)
        ans= crsr.fetchall()
        for i in range(0, len(ans)):
            if ans[i][3] == email:
                return True
        return False
        #connection.commit()

    def getinfo(self, email):        
        crsr = self.crsr
        connection = self.connection
        crsr.execute("""SELECT * FROM users """)
        ans= crsr.fetchall()
        for i in range(0, len(ans)):
            if ans[i][3] == email:
                return [ans[i][1], ans[i][2]]
        connection.commit()

database = Database()

@app.route('/', methods=['POST', 'GET'])

def index():
    return render_template('index.html')


@app.route('/desktop/login', methods=['POST', 'GET'])
def login():
    global database
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            email = request.form['email']
            password = request.form['password']
            dbpassword = database.datapassword(email)
            if password == dbpassword:
                session['ime'] = database.getinfo(email)[0]
                session['prezime'] = database.getinfo(email)[1]
                return redirect("/desktop/home", code=302)
            else:
                return render_template('desktop/login.html', statment=True)

        elif request.form['btn'] == 'redirect':
            return redirect('/desktop/register', code=302)

    return render_template('desktop/login.html', statment=False)


@app.route('/desktop/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['btn'] == 'register':
            ime = request.form['ime']
            prezime = request.form['prezime']
            mail = request.form['registerEmail']
            telefon = request.form['brojTelefona']
            passw = request.form['password']
            if database.check_for_email(mail) == False:
                if len(passw) >= 8:
                    try:
                        database.newuser(ime, prezime, mail, telefon, passw)
                        session['ime'] = database.getinfo(mail)[0]
                        session['prezime'] = database.getinfo(mail)[1]
                        return redirect("/phone/home", code=302)

                    except:
                        return 'Doslo je do grseske prilikom registracije'
                else: 
                    return render_template('desktop/register.html', errstatement=True)
            else: 
                if len(passw) < 8:
                    return render_template('desktop/register.html', statement=True, errstatement=True)
                return render_template('desktop/register.html', statement=True)

        elif request.form['btn'] == 'redirectLogin':
                return redirect('/desktop/login', code=302)
    return render_template('desktop/register.html', statement=False)


@app.route('/desktop/home', methods=['POST', 'GET'])
def home():
    try:
        username = session['ime']
        userlast = session['prezime']
        userinfo = username + ' ' + userlast
        return render_template('desktop/home.html', userinfo=userinfo)
    except:
        return render_template('desktop/home.html', userinfo='Login')
    
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('ime', None)
    session.pop('prezime', None)
    return redirect('/', code=302)


@app.route('/desktop/runscript', methods=['GET', 'POST'])
def runscript():
    runpy.run_path('script/script.py')
    return 'Running script'





if __name__ == "__main__":
    app.run(debug=True)