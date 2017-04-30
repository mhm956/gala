import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Note: Abandoning Lex for now:
# 1) Lambda performs the same task as the backend of API.AI
# 2) Only supports text (not speech) input from the Python Application
