import mysql.connector as mysql

# connecting to the database using 'connect()' method
# it takes 3 required parameters 'host', 'user', 'passwd'


def userinfo(Name: object, Mobile_number, Email, Age, Gender):
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="kickbenten",
        database="rasa",
        auth_plugin = 'mysql_native_password'
    )

    cursor = db.cursor()
    sql = 'insert into user_details(Name, Mobile_number, Email,Age, Gender) values ("{0}","{1}", "{2}", "{3}", "{4}");'.format(Name, Mobile_number, Email, Age, Gender)
    cursor.execute(sql)
    db.commit()
    print("record inserted.")

# if __name__ == "__main__":
#     userinfo("Challa Kusuma","9856321267","lilly@gmail.com",24, "Female")