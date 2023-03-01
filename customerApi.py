from flask import Flask,render_template,request,flash
from flask_cors import CORS
from waitress import serve
import time
# from db import Customer as c
app = Flask(__name__,template_folder='html')
app.secret_key = '1234'
CORS(app)

@app.route('/viewCustomer/', methods=['GET'])
def vCustomer():
    try:
        customerList = []
        file = open("customer.txt","r")
        for x in file:
            a = x.split(",")
            customerList.append(a)
    except Exception as e:
        print(e)
        customerList = []

    return render_template('home.html',customer=customerList)


@app.route('/registerCustomer/', methods=['GET','POST'])
def rCustomer():
    try:
        customerList = []
        if request.method == 'POST':
            cIc =  request.form['Ic']
            cIc = cIc.replace('-','')
            file = open('customer.txt', 'r')
            for x in file:
                a = x.split(",")
                customerList.append(a)
            for y in customerList:
                Id =  int(y[0]) +1

            file1 = open('customer.txt','a')
            data = str(Id)+","+request.form['name']+","+request.form['age']+","+request.form['location']+","+cIc
            if Id!=1:
                file1.write("\n"+data)
            flash('Registration successful')
    except Exception as e:
       print(str(e))
       customerList = ['Error']
    return render_template('register.html',customer=customerList)

@app.route('/deleteCustomer/', methods=['POST'])
def dCustomer():
    try:
        data = request.json
        customerList = []
        file = open("customer.txt","r")
        for x in file:
            a = x.split(",")
            customerList.append(a)
        for x in customerList:
            if int(x[0]) == int(data['ID']):
                customerList.remove(x)

        file1 = open("customer.txt","w")
        count =1
        for y in customerList:
            if len(customerList) == count:
                data = str(y[0])+","+y[1]+","+y[2]+","+y[3]+","+y[4].strip()
                file1.write(data)
            else:
                data = str(y[0])+","+y[1]+","+y[2]+","+y[3]+","+y[4]
                file1.write(data)
            count +=1

    except Exception as e:
        print(e)

    return render_template('home.html')

@app.route('/getCustomer', methods=['POST'])
def gCustomer():
    try:
        customerList = []
        # Open txt file and format it 
        file = open("customer.txt","r")
        for x in file:
            a = x.split(",")
            if request.form['ic'].strip() == a[4].strip():
                customerList.append(a)
    except Exception as e:
        print(e)
    return render_template('update.html',customer=customerList)

@app.route('/updateCustomer', methods=['POST'])
def uCustomer():
    line = 0
    customerList = []
    try:
        # append new data to list
        gcustomer = []
        gcustomer.append(request.form['id'])
        gcustomer.append(request.form['name'])
        gcustomer.append(request.form['age'])
        gcustomer.append(request.form['location'])
        gcustomer.append(request.form['ic'])

        
        file = open("customer.txt","r")
        for x in file:
            a = x.split(",")
            customerList.append(a)

        for y in customerList:
            if int(y[0]) == int(request.form['id']):
                customerList.remove(y)
                customerList.insert(line, [request.form['id'],request.form['name'],request.form['age'],request.form['location'],request.form['ic'].strip()])
            else:
                line+=1
        # After Update list append new data to customer text file
        file1 = open("customer.txt","w")
        count =1
        for y in customerList:
            if count < len(customerList):
                data = str(y[0])+","+y[1]+","+y[2]+","+y[3]+","+y[4].strip()+"\n"
                file1.write(data)
            else:
                data = str(y[0])+","+y[1]+","+y[2]+","+y[3]+","+y[4].strip()
                file1.write(data)
            count+=1
            
        # return message use 
        flash('Update successful')

    except Exception as e:
        print(e)
    return render_template('update.html',customer=[gcustomer])

if __name__ == '__main__':
    app.run()
