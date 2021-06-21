import os
import json
import s3_util

def get_buckets_list():
    target_profile = 'default'
    target_region = os.environ['AWS_REGION']
    result = s3_util.get_buckets_list(target_profile, target_region)

    print("result = " % result)
    return result

def handler(event, context):
    print("event = %s" % event)
    print("context = %s" % context)

    # simluate workload
    result = get_buckets_list()

    print("ERROR: Simulate error in Python handler.")

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Greeting": "Hello World!!! from Python handler, version: 2021-06-20.",
            "result": result,
            "Version": "0.1"
        })
    }
    
    print("response = %s" % response)
    return response

