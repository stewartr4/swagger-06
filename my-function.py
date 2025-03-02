import json

def lambda_handler(event, context):
    # Get query parameters
    query_params = event.get("queryStringParameters", {})
    keyword = query_params.get("keyword", "nothing")
    
    # Construct response
    response_text = f"Rian Stewart says {keyword}"
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": response_text})
    }
