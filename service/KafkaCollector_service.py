import json


class KafkaCollectorService:
    def __init__(self, KafkaCollectorDao, kafkaConsumer):
        self.KafkaCollectorDao = KafkaCollectorDao
        self.kafkaConsumer = kafkaConsumer

    def consumerGroupList(self):
        resultList=self.KafkaCollectorDao.selectConsumerGroup()
        return str(resultList)
    
    def topicList(self):
        resultList=self.KafkaCollectorDao.selectTopic()
        return str(resultList)
    
    def SoilDataSubscribeAndModify(self):
        for message in self.kafkaConsumer:
            print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" % (message.topic, message.partition, message.offset, message.key, message.value))
            key_json = json.loads(message.key.decode('utf-8'))
            value_json = json.loads(message.value.decode('utf-8'))
            print(key_json['GroupID'], key_json['DeviceID'], value_json['Humidity'], value_json['Temperature'])
            self.KafkaCollectorDao.updateHumTemperData(key_json['GroupID'], key_json['DeviceID'], value_json['Humidity'], value_json['Temperature'])
