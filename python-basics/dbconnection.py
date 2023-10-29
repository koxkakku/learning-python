# connect using mysql connector
# import mysql.connector
# connection = mysql.connector.connect(user='koxkakku', password='k0X@2020', host='127.0.0.1', database='test_app')
# print(connection.is_connected())
# connection.close()

# using connection from mysql connector
# from mysql.connector import connection
# cnx = connection.MySQLConnection(user='koxkakku', password='k0X@2020', host='127.0.0.1', database='test_app')
# print(cnx.is_connected())
# cnx.close()

# using configuration dictonary
# import mysql.connector
# config = {
#     'user': 'koxkakku',
#     'password': 'k0X@2020',
#     'host': '127.0.0.1',
#     'database': 'test_app'
# }
# connection = mysql.connector.connect(**config)
# print(connection.is_connected())
# connection.close()

import logging
import time
import mysql.connector

# setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s -- %(name)s - %(levelname)s - %(message)s")

# log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# log to file
file_handler = logging.FileHandler("cnx.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def connect_to_mysql(config, attempts, delay):
    attempt = 1
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError, Exception) as err:
            if attempts is attempt:
                logger.info("Failed to connect. Exiting without a connection : %s", err)
                return None
            logger.info("connection failed: %s. Retrying (%d%d)...",
                        err,
                        attempt,
                        attempts - 1)
            time.sleep(delay ** attempt)
            attempt += 1

    return None
