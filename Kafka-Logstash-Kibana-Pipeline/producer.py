from ensurepip import bootstrap
from faker import Faker
import json 
import time 
from kafka import KafkaProducer
fake = Faker()

def get_user_data():
    return {
        "name": fake.name(),
        "äddress": fake.address(),
        "date": fake.year(),
        "age": fake.random_number(digits = 2),
        "country": fake.country()
    }


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

if __name__ == '__main__':
    while 1 == 1:
        data = get_user_data()
        print(data)
        producer.send('test', value = json.dumps(data).encode('utf-8'))
        time.sleep(3)


