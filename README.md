# Kafka-Elasticsearch-Logstash-Kibana-Pipeline
A pipeline demostrating the usage of the ELK Stack 

Faker python package is used to generate fake data and fed into a kafka producer. 

Logstash, acting as the kafka consumer reads the data, transform it using filters to add new fields and remove others. Finally, the data goes to Elastic Search and Visualized using Kibana.  