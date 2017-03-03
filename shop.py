from flask import Flask, request, session, redirect, url_for, render_template
from flask_cors import CORS #Used to allow http requsets from other servers than the one this code runs on
import MySQLdb #Used to communicate with MySQL database
import json #Used to format data to and from JSON format
from configparser import SafeConfigParser #Used to read database user and password from .ini file
import time

config = SafeConfigParser()
config.read('databaseconfig.ini')


app = Flask(__name__)
app.secret_key = 'unicorn'
CORS(app)

#    CREATE TABLE `Order`        ( `order_id` int(11) NOT NULL AUTO_INCREMENT, `customer_id` int(11), `time` int(11), PRIMARY KEY (`order_id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
#    CREATE TABLE `OrderProduct` ( `product_id` int(11), `order_id` int(11) ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


@app.route('/')
def shop():
    return render_template('shop.html')

@app.route('/getcustomers',methods = ['GET'])
def getcustomers():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT customer_id,firstname,lastname,ssn,adress,city,email,phone,admin FROM Customer;")
    result=cursor.fetchall()
    y=[]
    for data in result:
        x=[]
        x.append(str(data[0]))            #customer_id
        x.append(data[1].encode('utf-8')) #firstname
        x.append(data[2].encode('utf-8')) #lastname
        x.append(data[3].encode('utf-8')) #ssn
        x.append(data[4].encode('utf-8')) #adress
        x.append(data[5].encode('utf-8')) #city
        x.append(data[6].encode('utf-8')) #email
        x.append(data[7].encode('utf-8')) #phone
        x.append(str(data[8]))            #admin
        y.append(x)
    db.close()
    return(json.dumps(y))

@app.route('/updatecustomer',methods = ['POST'])
def updatecustomer():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("UPDATE Customer SET firstname='"+received_data[1]+"',lastname='"+received_data[2]+"',ssn='"+received_data[3]+"',adress='"+received_data[4]+"',city='"+received_data[5]+"',email='"+received_data[6]+"',phone='"+received_data[7]+"',admin="+str(received_data[8])+" WHERE customer_id='"+str(received_data[0])+"';")
    db.commit()
    db.close()
    return("ok")
	
@app.route('/order',methods = ['POST'])
def order():
    if ( ('logged_in' not in session) or session['logged_in']==False):
        return("login")
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("INSERT INTO `Order` (customer_id,time) VALUES ("+str(session['customer'])+","+str(time.time())+");")
    for item in received_data:
        cursor.execute("INSERT INTO OrderProduct ( product_id, order_id ) VALUES ("+str(item[0])+",LAST_INSERT_ID());")
        cursor.execute("UPDATE Product SET instock=instock-1 WHERE product_id='"+str(item[0])+"';")
    db.commit()
    db.close()
    return("ok")

@app.route('/addstock',methods = ['POST'])
def addstock():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("INSERT INTO Product ( product_id, name, description, imgname, manufacturer, instock, cost ) VALUES ("+str(received_data[0])+",'"+received_data[1]+"','"+received_data[2]+"','"+received_data[3]+"','"+received_data[4]+"',"+str(received_data[5])+","+str(received_data[6])+");")
    db.commit()
    db.close()
    return("ok")

@app.route('/updatestock',methods = ['POST'])
def updatestock():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("UPDATE Product SET name='"+received_data[1]+"', description='"+received_data[2]+"', imgname='"+received_data[3]+"', manufacturer='"+received_data[4]+"', instock=instock+"+str(received_data[5])+", cost="+str(received_data[6])+" WHERE product_id="+str(received_data[0])+";")
    db.commit()
    db.close()
    return("ok")

@app.route('/removestock',methods = ['POST'])
def removestock():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("DELETE FROM Product WHERE product_id="+str(received_data)+";")
    db.commit()
    db.close()
    return("ok")

@app.route('/savecart',methods = ['POST'])
def savecart():
    if ( ('logged_in' not in session) or session['logged_in']==False):
        return("Not logged in")
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("UPDATE Customer SET cart='"+request.get_data()+"' WHERE customer_id="+str(session['customer'])+";")
    db.commit()
    db.close()
    return("ok")

@app.route('/getcart',methods = ['GET'])
def getcart():
    if ( ('logged_in' not in session) or session['logged_in']==False):
        return("[]")
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cart FROM Customer WHERE customer_id="+str(session['customer'])+";")
    result=cursor.fetchall()
    db.close()
    return(result[0][0])

@app.route('/search',methods = ['POST'])
def search():
    received_data=request.get_data()
    for char in '\'"-':  
        received_data = received_data.replace(char,'')
    if (received_data=="top10"):
	    query="SELECT Product.* FROM Product INNER JOIN OrderProduct USING (product_id) GROUP BY Product.product_id ORDER BY count(*) DESC LIMIT 10;"
    else:
        words=received_data.split()
        query="SELECT * FROM Product"
        if len(words)>0:
            query+=" WHERE ( "
            for y in range(len(words)):
                query+="( name LIKE '%"+words[y]+"%' OR description LIKE '%"+words[y]+"%' OR manufacturer LIKE '%"+words[y]+"%') "
                if y!=len(words)-1:
                    query+=" AND "
            query+=" )"
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    y=[]
    for data in result:
        x=[]
        x.append(str(data[0]))            #productID
        x.append(data[1].encode('utf-8')) #Name
        x.append(data[2].encode('utf-8')) #Description
        x.append(data[3].encode('utf-8')) #imgname
        x.append(data[4].encode('utf-8')) #manufacturer
        x.append(str(data[5]))            #instock
        x.append(str(data[6]))            #cost
        y.append(x)
    return(json.dumps(y))

@app.route('/register', methods=['GET'])
def register():
    return render_template('signup.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    try:
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        ssn = request.form['ssn']
        adress = request.form['adress']
        city = request.form['city']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        if firstname and email and password:
            db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
            cursor = db.cursor()
            check = cursor.execute('SELECT * FROM Customer WHERE email =%s',(email, ))

            if int(check) > 0:
                return render_template('signup.html')
            else:
                cursor.execute("INSERT INTO Customer (firstname, lastname, ssn, adress, city, email, phone, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(firstname, lastname, ssn, adress, city, email, phone, password))
                db.commit()
                return render_template('shop.html')

    except Exception as e:
        return(str(e))

@app.route("/logoff")
def logout():
    session['logged_in'] = False
    session['customer'] = False
    session['customerName'] = False
    session['admin'] = False
    return ("ok")

@app.route("/login", methods=['POST'])
def login():
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer WHERE email=%s and password=%s',(received_data['user'],received_data['passwd'] ))
    customer=cursor.fetchall()
    if (len(customer) > 0):
        session['logged_in'] = True
        session['customer'] = customer[0][0]
        session['customerName'] = customer[0][1] + " " + customer[0][2]
        session['admin'] = customer[0][9]
        return ("ok")
    else:
        return ("error")

@app.route('/getuserstatus')
def getuserstatus():
    if ( ('logged_in' not in session) or session['logged_in']==False):
        return("{}")
    c={}
    c['name']=session['customerName']
    c['admin']=session['admin']
    return(json.dumps(c))

@app.route('/admin', methods=['GET'])
def admin():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    return render_template('admin.html')

@app.route('/listorders')
def listorders():
    if ( ('logged_in' not in session) or session['logged_in']==False or session['admin']==False):
        return("You do not have admin rights")
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `Order` INNER JOIN `Customer` USING (customer_id) ORDER BY `time` DESC;")
    buyers=cursor.fetchall()
    y=[]
    for buyer in buyers:
        x=[]
        x.append(str(buyer[0]))            #customer_id
        x.append(str(buyer[1]))            #order_id
        x.append(str(buyer[2]))            #UNIX timestamp
        x.append(buyer[3].encode('utf-8')) #First Name
        x.append(buyer[4].encode('utf-8')) #Last Name
        x.append(buyer[5].encode('utf-8')) #ssn
        x.append(buyer[6].encode('utf-8')) #address
        x.append(buyer[7].encode('utf-8')) #city
        x.append(buyer[8].encode('utf-8')) #email
        x.append(buyer[9].encode('utf-8')) #phone
        cursor.execute("SELECT * FROM `OrderProduct` INNER JOIN `Product` USING (product_id) WHERE order_id="+str(buyer[1])+";")
        items=cursor.fetchall()
        i=[]
        for item in items:
            z=[]
            z.append(str(item[0]))
            z.append(item[2].encode('utf-8'))
            z.append(item[5].encode('utf-8'))
            z.append(str(item[7]))
            i.append(z)			
        x.append(i)
        y.append(x)
    db.commit()
    db.close()
    return(json.dumps(y))

@app.route('/customer', methods=['GET'])
def customer():
    if ( ('logged_in' not in session) or session['logged_in']==False):
        return("Please log in to view your personal dashboard!")
    return render_template('customer.html')

@app.route('/getinfo', methods=['GET'])
def getInfo():
    info = session['customer']
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer WHERE customer_id=%s',(info, ))
    result = cursor.fetchall()
    y = []
    for data in result:
        x = []
        x.append(str(data[0]))             #customer_id
        x.append(data[1].encode('utf-8'))  #firstname
        x.append(data[2].encode('utf-8'))  #lastname
        x.append(data[3].encode('utf-8'))  #ssn
        x.append(data[4].encode('utf-8'))  #adress
        x.append(data[5].encode('utf-8'))  #city
        x.append(data[6].encode('utf-8'))  #email
        x.append(data[7].encode('utf-8'))  #phone
        y.append(x)
    return(json.dumps(y))

@app.route('/updateinfo', methods=['POST'])
def updateinfo():
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("UPDATE Customer SET firstname='"+received_data[1]+"', lastname='"+received_data[2]+"',ssn='"+received_data[3]+"',adress='"+received_data[4]+"',city='"+received_data[5]+"',email='"+received_data[6]+"',phone='"+received_data[7]+"' WHERE customer_id="+str(received_data[0])+";")
    db.commit()
    db.close()
    return("ok")

@app.route('/password', methods=['POST'])
def password():
    cuid = session['customer']
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT password FROM Customer WHERE customer_id=%s and password=%s",(cuid, received_data['oldpasswd'] ))
    passwd=cursor.fetchall()
    if (len(passwd) > 0):
        return ("ok")
    else:
        return ("error")

@app.route('/changepassword', methods=['POST'])
def changepasswd():
    cuid = session['customer']
    received_data=json.loads(request.get_data())
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute("UPDATE Customer SET password=%s WHERE customer_id=%s", (received_data['newpasswd'], cuid ))
    db.commit()
    db.close()
    return("ok")

@app.route('/history', methods=['GET'])
def orderhistory():
    cuid = session['customer']
    db = MySQLdb.connect(host=config.get('main', 'host'), user=config.get('main', 'user'), passwd=config.get('main', 'passwd'), db='webshop', use_unicode=True, charset="utf8")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM `Order` INNER JOIN `Customer` USING (customer_id) WHERE customer_id=%s', (cuid, ))
    customer=cursor.fetchall()
    y = []
    for info in customer:
        x = []
        x.append(str(info[0]))                   #customer_id
        x.append(str(info[1]))                   #order_id
        x.append(str(info[2]))                   #UNIX timestamp
        x.append(info[3].encode('utf-8'))        #first name
        cursor.execute("SELECT * FROM `OrderProduct` INNER JOIN `Product` USING (product_id) WHERE order_id="+str(info[1])+";")
        items=cursor.fetchall()
        i=[]
        for item in items:
            z=[]
            z.append(str(item[0]))              #product_id
            z.append(item[2].encode('utf-8'))   #product name
            z.append(item[5].encode('utf-8'))   #manufacturer
            z.append(str(item[7]))              #product cost
            i.append(z)
        x.append(i)
        y.append(x)
    db.commit()
    db.close()
    return(json.dumps(y))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1204)
