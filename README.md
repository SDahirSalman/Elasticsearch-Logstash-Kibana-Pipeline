# Kafka-Elasticsearch-Logstash-Kibana-Pipeline
A pipeline demostrating the usage of the ELK Stack 

Faker python package is used to generate fake data and fed into a kafka producer. 

Logstash, acting as the kafka consumer reads the data, transform it using filters to add new fields and remove others. Finally, the data goes to Elastic Search and Visualized using Kibana.  

## How to run 

1. Install Kafka 
2. Install Docker and Docker Compose 
3. Create a docker-compose.yaml file to build elasticsearch and kibana image 
4. install logstash
5. Copy the logstash-pipeline.conf file into same directory as your logstash installation or create a new .conf file and copy the code.
6. Start the docker containers
7. Run the kafka producer
8. Finally, run logstash-pipeline.conf

