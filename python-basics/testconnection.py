from dbconnection import connect_to_mysql

config = {
    'user': 'koxkakku',
    'password': 'k0X@2020',
    'host': '127.0.0.1',
    'database': 'test_app'
}
attempts = 3
delay = 2
connection = connect_to_mysql(config, attempts, delay)
if connection is not None:
    print(connection.is_connected())
    myCursor = connection.cursor()
    # myCursor.execute("CREATE TABLE app_users "
    #                        "(user_id INTEGER, user_name VARCHAR(255), password VARCHAR(255))")
    myCursor.execute("SHOW TABLES")
    for tb in myCursor:
        print(tb)
    myCursor.execute("DESC app_users")
    for tb in myCursor:
        print(tb)
    myCursor.execute("INSERT INTO app_users (user_id,user_name,password) values (1,'Sharad','test@2020')")
    myCursor.execute("SELECT * FROM app_users")
    for row in myCursor:
        print(row)
    connection.close()


