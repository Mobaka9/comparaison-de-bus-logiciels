import json
import time
import sys
from kafka import KafkaProducer


def publish_message(kafka_producer, topic_name, msg):
    try:
        #key_bytes = str(employee['id']).encode('utf-8')

        string_bytes = str.encode(msg)

        kafka_producer.send(topic_name, value=string_bytes)
        kafka_producer.flush()
        #print('Message published successfully.')
    except Exception as ex:
        print(str(ex))


if __name__ == '__main__':
    start_time = time.time()
    kafka_producer  = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    msg = 'hello Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.Lorem ipsum dolor sit amet. Aut laboriosam praesentium hic voluptatem praesentium sit architecto unde. Qui officia adipisci sit obcaecati debitis et adipisci adipisci et iste nisi aut consequuntur dolores qui labore dolorem. Eum dolorem natus ea suscipit tempore At molestiae magnam qui alias dignissimos aut similique impedit. Id sunt dolores aut quis nemo sed voluptas asperiores qui voluptate quidem non galisum sint ut corrupti architecto. In accusantium exercitationem aut saepe dolores sed incidunt rerum aut aspernatur architecto ut dolor facere et voluptas doloremque. Id exercitationem saepe ut unde commodi aut magnam commodi? Ea quae accusantium et labore quia ab voluptates ratione qui suscipit deleniti est temporibus perferendis. Ea dolores dolore est saepe dolores ad architecto consequatur eum reprehenderit obcaecati ab voluptatem galisum. Nam perspiciatis placeat sed autem sunt qui rerum voluptatem in nisi iure. Aut nisi illum nam perspiciatis odit quo beatae vero ut sunt vitae id velit fugiat id aliquid repellat. Est sunt reprehenderit et odio quia rem laudantium mollitia sed velit tempore.'
    total_msgs = sys.argv[1]
    total_msgs = int(total_msgs)
    
    for i in range(total_msgs):
        
        msg = "hello ="
        publish_message(
                kafka_producer=kafka_producer,
                topic_name='hello',
                msg=str(i)+msg
                
            )
    last_msg = "last message ="+str(start_time)
    publish_message(
                kafka_producer=kafka_producer,
                topic_name='hello',
                msg=last_msg
                
            )
    
    if kafka_producer is not None:
        kafka_producer.close()









'''
from kafka import KafkaProducer
import time

# Créer un producteur Kafka qui envoie des messages à l'adresse du broker
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
time.sleep(5)

# Envoyer un message à un sujet (topic) spécifique
producer.send('mon-sujet', b'Mon message de test!')
print('Message envoyé avec succès.')
'''