from flask import Flask, jsonify
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from flask_dynamo import Dynamo

app = Flask(__name__)

# Configure DynamoDB Local
app.config['DYNAMO_TABLES'] = [
    {
        'TableName': 'users',
        'KeySchema': [{'AttributeName': 'username', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'username', 'AttributeType': 'S'}],
        'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    }
]
app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 8000

dynamodb = Dynamo(app)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    try:
        # Attempt to check connection
        dynamodb.tables['users'].table_name
        return jsonify({"status": "healthy"}), 200
    except (NoCredentialsError, PartialCredentialsError):
        return jsonify({"status": "unhealthy", "reason": "Credentials error"}), 500
    except Exception as e:
        return jsonify({"status": "unhealthy", "reason": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
