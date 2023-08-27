from sqlalchemy import text

class KafkaCollectorDao:
    def __init__(self, database, KafkaAdminClient, kafkaConsumer):
        self.db = database
        self.KafkaAdminClient = KafkaAdminClient
        self.kafkaConsumer = kafkaConsumer

    def selectConsumerGroup(self):
        existingConsumerGroupList = self.KafkaAdminClient.list_consumer_groups()
        return existingConsumerGroupList

    def selectTopic(self):
        existingTopicSet = self.kafkaConsumer.topics()
        return existingTopicSet
    
    def updateHumTemperData(self, group_id, device_id, hum_data, temper_data):
        return self.db.execute(text("""
            UPDATE SOILDATA 
            SET HUMIDITY = :hum_data, TEMPERATURE = :temper_data
            WHERE DEVICEID = :device_id
            AND GROUPID = :group_id
            """), {
                'hum_data'      : hum_data,
                'temper_data'   : temper_data,
                'device_id'     : device_id,
                'group_id'      : group_id
            }).rowcount
    