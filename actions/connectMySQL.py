import mysql.connector

def inputdatabase(Phone_number, Name, Quantity_people, Time_using, Food_order):
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "14021999", database = "rasa")  
    # code3 = "CREATE DATABASE dbrasa"
    # code1 = "USE dbrasa;"
    # code4 = ""
    text_customer = "VALUES (\'" + str(Phone_number) + '\',\'' + str(Name) + '\',\'' +str(Quantity_people) + '\',\'' + str(Time_using) + '\');' 
    import_customer = "INSERT INTO `customer` (`Số điện thoại`, `Tên khách hàng`, `Số lượng chỗ ngồi`, `Thời gian sử dụng`) "+ text_customer
    mycursor = myconn.cursor()
    mycursor.execute(import_customer)
    for i in Food_order:
        if Food_order[i] != None:
            text_food_order = "VALUES (\'" + str(Phone_number) + '\',\'' + str(i) + '\',\'' +str(Food_order[i]) + '\');' 
            import_food_order = "INSERT INTO `order_food` (`Số điện thoại`, `Tên món ăn`, `Số lượng món ăn`)"+ text_food_order
            mycursor = myconn.cursor()
            mycursor.execute(import_food_order)
    myconn.commit()


# *******TEST******** 
# information_customer = {
#                     "name_customer": "Anh",
#                     "phone_number_customer": "0987654321",
#                     "quatity_people_using": "4",
#                     "time_using_customer": "2023-05-16 18:00:00",
#                     "list_food_order": {"Gà hấp đông cô sốt bào ngư": 8,
#                                         "Tôm càng nướng wasabi": 7,
#                                          "Thạch xoài ăn kèm sữa dừa": 3}
# }

# inputdatabase(information_customer["phone_number_customer"], 
#               information_customer["name_customer"], 
#               information_customer["quatity_people_using"], 
#               information_customer["time_using_customer"], 
#               information_customer["list_food_order"])