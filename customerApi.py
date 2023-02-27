from flask import Flask,jsonify,request,json
from flask_cors import CORS
from waitress import serve
from db import Customer as c
app = Flask(__name__)
CORS(app)

@app.route('/viewCustomer/', methods=['GET'])
def vCustomer():
    try:
        customerList = []
        all_customer = c.getCustomer()
        for x in all_customer:
            eCustomer = [x.customerName,x.Id,x.customerAge,x.customerLocation]
            customerList.append(eCustomer)
        response = jsonify(customerList)

    except Exception as e:
        response_data = {'Status':'Error in '+str(e)}
        response = jsonify(response_data)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/registerCustomer/', methods=['POST'])
def rCustomer():
    try:
        cName = request.json['cName']
        cAge = request.json['cAge']
        cLocation = request.json['cLocation']
        cIc = request.json['cIc']
        cIc = cIc.replace('-','')
        exist = c.checkCustomerIc(cIc)
        if exist == True:
            response_data = {'Status':'Customer Ic exist'}
        else:
            result = c.addCustomer(cName,cAge,cLocation,cIc)
            if result != True:
                response_data = {'Status':'Fail to Register' }
            else:
                response_data = {'Status':'Success Register' }
        response = jsonify(response_data)
    except Exception as e:
        response_data = {'Error':str(e)}
        response = jsonify(response_data)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/updateCustomer/', methods=['POST'])
def uCustomer():
    try:
        cName = request.json['cName']
        cAge = request.json['cAge']
        cLocation = request.json['cLocation']
        cIc = request.json['cIc']
        cId = request.json['cId']
        # Check ic is it exists
        exist = c.checkCustomerId(cId)
        if exist != True:
            response_data = {'Status':'Customer Id not exist'}
        else:
            result = c.updateCustomer(cName,cAge,cLocation,cIc,cId)
            if result != True:
                response_data = {'Status':'Fail to Update' }
            else:
                response_data = {'Status':'Success Update' }
        response = jsonify(response_data)
    except Exception as e:
        response_data = {'Error':str(e)}
        response = jsonify(response_data)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteCustomer/', methods=['POST'])
def dCustomer():
    try:
        cId = request.json['cId']
        # Check ic is it exists
        exist = c.checkCustomerId(cId)
        if exist != True:
            response_data = {'Status':'Customer did not exist'}
        else:
            result = c.deleteCustomer(cId)
            if result != True:
                response_data = {'Status':'Fail to Delete' }
            else:
                response_data = {'Status':'Success Delete' }
        response = jsonify(response_data)
    except Exception as e:
        response_data = {'Error':str(e)}
        response = jsonify(response_data)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
