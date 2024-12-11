from fastapi import FastAPI, Request
import boto3

app = FastAPI()

dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')

@app.post("/process")
async def process_data(request: Request):
    data = await request.json()
    
    # Guardar en DynamoDB
    dynamodb.put_item(
        TableName='TuTabla',
        Item={
            'ID': {'S': data['id']},
            'Info': {'S': data['info']}
        }
    )

    # Procesar con Bedrock (ejemplo)
    response = invoke_bedrock_model(data['info'])
    
    return {"response": response}

def invoke_bedrock_model(input_text):
    # Ejemplo de llamada al modelo
    client = boto3.client('bedrock-runtime')
    response = client.invoke_model(
        modelId='tu-modelo',
        inputText=input_text
    )
    return response['outputText']


import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Inicio de la función Lambda")
    # Código


import boto3

dynamodb = boto3.client('dynamodb')
bedrock = boto3.client('bedrock-runtime')

def save_to_dynamodb(data):
    dynamodb.put_item(
        TableName='MiTabla',
        Item={'ID': {'S': data['id']}, 'Info': {'S': data['info']}}
    )

def call_bedrock(info):
    response = bedrock.invoke_model(
        modelId='tu-modelo',
        inputText=info
    )
    return response['outputText']
