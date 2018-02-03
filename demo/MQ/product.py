#coding:utf8
import pika
import sys

mq_server = "10.200.25.194"

vhost = "cloudplay_channelcenter"
vhost_user_name = "cloudplay_channelcenter"
vhost_user_password = "channelcenter"

exchange_name = 'channelcenter.rabbitmq.exchange'
queue_name = 'pplcoud.rabbitmq.streamstatus.queue'

routing_key = 'pplcoud.rabbitmq.streamstatus.queue'

credentials = pika.PlainCredentials(vhost_user_name,
                                    vhost_user_password)
connect_parameter = pika.ConnectionParameters(mq_server,
                                              virtual_host=vhost,
                                              credentials=credentials)
connection = pika.BlockingConnection(connect_parameter)

channel = connection.channel()
# channel.exchange_declare(exchange='topic_logs',
#                          type='topic')
#
# result = channel.queue_declare(exclusive=True)
# queue_name = result.method.queue


message = r'''
{
	"header": {
		"createTime": 1517624919457,
		"messageId": "a4b54e1a-a10b-48a8-a292-74f324c52dca",
		"errorMsg": null,
		"messageType": "vodstatus_v1"
	},
	"body": {
		"channelid": 159277234,
		"cpname": "ppcloud",
		"vodstatus": 112,
		"version": "1",
		"fid": 5816143,
		"duration": 6,
		"coverImg": "/14/36/14368dd21bc898ef965fc36159277234/1517624916853.jpg",
		"channel_file_id": null,
		"channel_file_status": null,
		"reviewmsg": null,
		"encode_code": null,
		"encode_msg": null,
		"message_type": "vodstatus_v1"
	}
}
'''
channel.basic_publish(exchange=exchange_name,
                      routing_key=routing_key,
                      body=message)

print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()