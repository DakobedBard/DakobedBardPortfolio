from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   bootstrap_servers=['172.17.0.1:32783','172.17.0.1:32782','172.17.0.1:32781'])

producer.send("words", value={"hello": "producer"})
