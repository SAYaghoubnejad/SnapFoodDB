import mysql.connector

class SnapFoodDB:

    def __init__(self):
        self._mydb = mysql.connector.connect(
            host = "host",
            user = "user",
            passwd = "pass",
            database = "database"
        )
        self._mycursor = self._mydb.cursor()

    def registerUser(self, user_id, password, f_name = "", l_name = "", phone_number = "", email = "", wallet_id = ""):
        self._mycursor.execute("INSERT INTO USER VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')"
        .format(user_id, f_name, l_name, phone_number, email, password, wallet_id))
        self._mydb.commit()


    def login(self, user_id):
        self._mycursor.execute("SELECT userid, password FROM USER WHERE userid=\'{}\'".format(user_id))
        return self._mycursor.fetchall()

    def updateUserProfile(self, user_id, f_name = "", l_name = "", phone_number = "", email = "", passwd = ""):
        self._mycursor.execute("SELECT * FROM USER WHERE userid=\'{}\'".format(user_id))
        tmp = self._mycursor.fetchall()
        if len(tmp) != 1 :
            return "ERROR"
        if f_name == "" :
            f_name = tmp[0][1]
        if l_name == "" :
            l_name = tmp[0][2]
        if phone_number == "" :
            phone_number = tmp[0][3]
        if email == "" :
            email = tmp[0][4]
        if passwd == "" :
            passwd = tmp[0][5]
        self._mycursor.execute("UPDATE USER SET `first-name` = \'{}\', `last-name` = \'{}\', `phone-number` = \'{}\', email = \'{}\', password = \'{}\' WHERE userid = \'{}\';"
        .format(f_name, l_name, phone_number, email, passwd, user_id))
        self._mydb.commit()
        return "DONE"

    def close(self):
        self._mydb.close()
