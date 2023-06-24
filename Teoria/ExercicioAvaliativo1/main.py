#Exercício Avaliativo BD2, Paulo Otavio - 1732
import threading
import time
import random
from pymongo import MongoClient

#Acessando o MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['bancoiot']

#Criando 3 threads, cada um responsável por simular a temperatura de um sensor em uma rede IoT
#Cada thread representa um sensor
def sensor1():
    sensor1 = db.sensores

    #Gerando uma temperatura aleatória entre 30ºC e 40ºC
    temperatura1 = random.randint(30, 40)

    #Se a temperatura for maior que 38
    if temperatura1 > 38:

        sensor1.update_one(
            {"nomeSensor":  "Temp1"},
            {"$set": {"valorSensor": temperatura1}}
        )

        sensor1.update_one(
            {"nomeSensor": "Temp1"},
            {"$set": {"sensorAlarmado": True}}
        )
        print(temperatura1)
        print("Atenção! Temperatura muito alta! Verificar Sensor 1")


    #Caso a temperatura seja <= 38
    else:
        #Irá gerar uma nova temperatura sempre que a variável temperatura for menor que ou igual a 38
        while temperatura1 <= 38:
            time.sleep(5)
            temperatura1 = random.randint(30, 40)
            print(temperatura1)

            sensor1 = db.sensores
            if temperatura1 <=38:
                sensor1.update_one(
                    {"nomeSensor": {"$exists": "Temp1"}},
                    {"$set": {"valorSensor": temperatura1}}
                )
                sensor1.update_one(
                    {"nomeSensor": {"$exists": "Temp1"}},
                    {"$set": {"sensorAlarmado": False}}
                )

            elif temperatura1 > 38:
                sensor1.update_one(
                    {"nomeSensor": {"$exists": "Temp1"}},
                    {"$set": {"valorSensor": temperatura1}}
                )

                sensor1.update_one(
                    {"nomeSensor": {"$exists": "Temp1"}},
                    {"$set": {"sensorAlarmado": True}}
                )
                print("Atenção! Temperatura muito alta! Verificar Sensor 1")

def sensor2():
    sensor2 = db.sensores

    temperatura2 = random.randint(30, 40)
    if temperatura2 > 38:

        sensor2.update_one(
            {"nomeSensor": "Temp2"},
            {"$set": {"valorSensor": temperatura2}}
        )

        sensor2.update_one(
            {"nomeSensor": "Temp2"},
            {"$set": {"sensorAlarmado": True}}
        )
        print(temperatura2)
        print("Atenção! Temperatura muito alta! Verificar Sensor 2")

    else:
        while temperatura2 <= 38:
            time.sleep(5)
            temperatura2 = random.randint(30, 40)
            print(temperatura2)

            sensor2 = db.sensores

            if temperatura2 <= 38:
                sensor2.update_one(
                    {"nomeSensor": "Temp2"},
                    {"$set": {"valorSensor": temperatura2}}
                )
                sensor2.update_one(
                    {"nomeSensor": "Temp2"},
                    {"$set": {"sensorAlarmado": False}}
                )

            elif temperatura2 > 38:
                sensor2.update_one(
                    {"nomeSensor": "Temp2"},
                    {"$set": {"valorSensor": temperatura2}}
                )

                sensor2.update_one(
                    {"nomeSensor": "Temp2"},
                    {"$set": {"sensorAlarmado": True}}
                )
                print("Atenção! Temperatura muito alta! Verificar Sensor 2")

def sensor3():
    sensor3 = db.sensores

    temperatura3 = random.randint(30, 40)
    if temperatura3 > 38:
        sensor3.update_one(
            {"nomeSensor":  "Temp3"},
            {"$set": {"valorSensor": temperatura3}}
        )

        sensor3.update_one(
            {"nomeSensor": "Temp3"},
            {"$set": {"sensorAlarmado": True}}
        )
        print(temperatura3)
        print("Atenção! Temperatura muito alta! Verificar Sensor 3")

    else:
        while temperatura3 <= 38:
            time.sleep(5)
            temperatura3 = random.randint(30, 40)
            print(temperatura3)

            sensor3 = db.sensores

            if temperatura3 <= 38:
                sensor3.update_one(
                    {"nomeSensor":  "Temp3"},
                    {"$set": {"valorSensor": temperatura3}}
                )
                sensor3.update_one(
                    {"nomeSensor":  "Temp3"},
                    {"$set": {"sensorAlarmado": False}}
                )

            elif temperatura3 > 38:
                sensor3.update_one(
                    {"nomeSensor":  "Temp3"},
                    {"$set": {"valorSensor": temperatura3}}
                )

                sensor3.update_one(
                    {"nomeSensor": "Temp3"},
                    {"$set": {"sensorAlarmado": True}}
                )
                print("Atenção! Temperatura muito alta! Verificar Sensor 3")

def temperatura():
    threading.Thread(target=sensor1).start()
    threading.Thread(target=sensor2).start()
    threading.Thread(target=sensor3).start()

#OBS: Caso em algum sensor detecte-se alguma temperatura acima de 38,
# ele para de computar a temperatura desse mesmo sensor e continuará gerando
# valores para os outros. Até que todos detectem 39 ou 40 graus Celsius

print("Mostrando os valores dos sensores 1, 2 e 3:")
temperatura()