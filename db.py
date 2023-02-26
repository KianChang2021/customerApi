<<<<<<< HEAD
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=;'
                    'Database=Company;'
                    'Trusted_Connection=yes;')

class Customer:
    def getCustomer():
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM [dbo].[Customer]
            ''')
            data = cursor.fetchall()
            return data
        except Exception as ex:
            print(str(ex))
        cursor.close()

    def addCustomer(cName,cAge,cLocation,cIc):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO [dbo].[Customer] (customerName,customerAge,customerLocation,customerIc)
                VALUES ('{0}',{1},'{2}',{3});
            '''.format(cName,cAge,cLocation,cIc))
            cursor.commit()
            return True
        except Exception as ex:
            cursor.rollback()
            print(str(ex))
        cursor.close()

    def checkCustomerIc(cIc):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT customerIc FROM [dbo].[Customer] WHERE customerIc = {0}
            '''.format(cIc))
            data = cursor.fetchall()
            if len(data) >=1:
                return True
            
        except Exception as ex:
            print(str(ex))
        cursor.close()

    def checkCustomerId(cId):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT Id FROM [dbo].[Customer] WHERE Id = {0}
            '''.format(cId))
            data = cursor.fetchall()
            if len(data) >=1:
                return True
            
        except Exception as ex:
            print(str(ex))
        cursor.close()

    def updateCustomer(cName,cAge,cLocation,cIc,cId):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                Update [dbo].[Customer] SET customerName='{0}',customerAge={1},customerLocation='{2}',customerIc={3} WHERE Id={4}
            '''.format(cName,cAge,cLocation,cIc,cId))
            cursor.commit()
            return True
        except Exception as ex:
            cursor.rollback()
            print(str(ex))

        cursor.close()
    
    def deleteCustomer(cId):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                delete [dbo].[Customer] WHERE Id={0}
            '''.format(cId))
            cursor.commit()
            return True
        except Exception as ex:
            cursor.rollback()
            print(str(ex))

        cursor.close()

if __name__ == '__main__':
    updateCustomer(950817089988)
        #serve(app, host="0.0.0.0", port=8080)
=======
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                    'Server="";'
                    'Database=Company;'
                    'Trusted_Connection=yes;')

class Customer:
    def getCustomer():
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM [dbo].[Customer]
            ''')
            data = cursor.fetchall()
            return data
        except Exception as ex:
            print(str(ex))
        cursor.close()

    def addCustomer(cName,cAge,cLocation,cIc):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO [dbo].[Customer] (customerName,customerAge,customerLocation,customerIc)
                VALUES ('{0}',{1},'{2}',{3});
            '''.format(cName,cAge,cLocation,cIc))
            cursor.commit()
            return True
        except Exception as ex:
            cursor.rollback()
            print(str(ex))
        cursor.close()

    def checkCustomerIc(cIc):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT customerIc FROM [dbo].[Customer] WHERE customerIc = {0}
            '''.format(cIc))
            data = cursor.fetchall()
            if len(data) >=1:
                return True
            
        except Exception as ex:
            print(str(ex))
        cursor.close()

    def checkCustomerId(cId):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT Id FROM [dbo].[Customer] WHERE Id = {0}
            '''.format(cId))
            data = cursor.fetchall()
            if len(data) >=1:
                return True
            
        except Exception as ex:
            print(str(ex))
        cursor.close()

    def updateCustomer(cName,cAge,cLocation,cIc,cId):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                Update [dbo].[Customer] SET customerName='{0}',customerAge={1},customerLocation='{2}',customerIc={3} WHERE Id={4}
            '''.format(cName,cAge,cLocation,cIc,cId))
            cursor.commit()
            return True
        except Exception as ex:
            cursor.rollback()
            print(str(ex))

        cursor.close()
    
    def deleteCustomer(cId):
        try:
            cursor = conn.cursor()
            cursor.execute('''
                delete [dbo].[Customer] WHERE Id={0}
            '''.format(cId))
            cursor.commit()
            return True
        except Exception as ex:
            cursor.rollback()
            print(str(ex))

        cursor.close()

if __name__ == '__main__':
    updateCustomer(950817089988)
        #serve(app, host="0.0.0.0", port=8080)
>>>>>>> 32eb975e64d5220a2966862a8eb7c3c00f880f75
