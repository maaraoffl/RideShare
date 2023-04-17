import mysql.connector
from driver_info import DriverInfo


connection = mysql.connector.connect(user = 'root', password = 'new_password', database = "driver")

def list_driver():
  cursor = connection.cursor()
  query = 'SELECT * from driver_info'
  cursor.execute(query)

  data = cursor.fetchall()

  drivers = []
  for row in data:
    driver = DriverInfo(row[0], row[1], row[2])
    drivers.append(driver)

  return drivers

def list_driver_by_id(id):
  cursor = connection.cursor()
  query = f"""SELECT * from driver_info where id = {id};"""
  cursor.execute(query)

  data = cursor.fetchone()
  driver = DriverInfo(data[0], data[1], data[2])
  return driver  