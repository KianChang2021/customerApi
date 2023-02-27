from flask import Flask,render_template,request
from flask_cors import CORS
from waitress import serve
# from db import Customer as c
app = Flask(__name__,template_folder='html')
CORS(app)

@app.route('/viewCustomer/', methods=['GET'])
def vCustomer():
    try:
        customerList = []
        file = open("customer.txt","r")
        for x in file:
            a = x.split(",")
            customerList.append(a)
        print(customerList)
    except Exception as e:
        print(e)
        customerList = []

    return render_template('home.html',title="Customer" ,customer=customerList)


@app.route('/registerCustomer/', methods=['GET','POST'])
def rCustomer():
    try:
        customerList = []
        if request.method == 'POST':
            cName = request.form['name']
            cAge =  request.form['age']
            cLocation =  request.form['location']
            cIc =  request.form['Ic']
            cIc = cIc.replace('-','')

            file = open('customer.txt', 'r')
            x = len(file.readlines())

            Id = x+1
            file1 = open('customer.txt','a')
            data = str(Id)+","+cName+","+cAge+","+cLocation+","+cIc
            if x >0:
                file1.write("\n")
                file1.write(str(data))
            else:
                file1.write(str(data))

        
    except Exception as e:
       print(str(e))
       customerList = ['Error']

    return render_template('register.html',title="Customer" ,customer=customerList)

# @app.route('/updateCustomer/', methods=['POST'])
# def uCustomer():
#     try:
#         cName = request.json['cName']
#         cAge = request.json['cAge']
#         cLocation = request.json['cLocation']
#         cIc = request.json['cIc']
#         cId = request.json['cId']

#         response = jsonify(response_data)
#     except Exception as e:
#         response_data = {'Error':str(e)}
#         response = jsonify(response_data)

#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/deleteCustomer/', methods=['POST'])
# def dCustomer():
#     try:
#         cId = request.json['cId']
#         # Check ic is it exists
        
#         response = jsonify(response_data)
#     except Exception as e:
#         response_data = {'Error':str(e)}
#         response = jsonify(response_data)

#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


if __name__ == '__main__':
    app.run()
