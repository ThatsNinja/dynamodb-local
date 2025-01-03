import os
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
app.config['DYNAMO_LOCAL_HOST'] = 'dynamodb-local'
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
    with app.app_context():
        dynamodb.create_all()

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
