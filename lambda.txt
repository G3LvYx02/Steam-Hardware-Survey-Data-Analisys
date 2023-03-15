import boto3
import sys
sys.path.insert(0, '/opt/AWSSDKPandas-Python39')
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup

# Imposta i nomi del bucket S3 e del file HTML di output
BUCKET_NAME = 'bucketsteam'
OUTPUT_HTML_FILE = 'top-10-prodotti.html'
INPUT_CSV_FILE = 'bucketsteam/gpu.csv' # aggiungi il nome del tuo file CSV

def lambda_handler(event, context):
    
    # Legge il file CSV dal bucket S3
    s3 = boto3.resource('s3')
    #s3 = boto3.client('s3')
    #bucket = s3.Bucket(BUCKET_NAME) # aggiungi il nome del tuo bucket S3
    #response = s3.get_object(BUCKET_NAME, INPUT_CSV_FILE).get
    #file_content = response['Body'].read().decode('utf-8')
    #file_obj = bucket.get_object(INPUT_CSV_FILE) # aggiungi il nome del tuo file CSV
    #file_content = file_obj.get()['Body'].read().decode('utf-8')
    obj = s3.Object(BUCKET_NAME, INPUT_CSV_FILE)
    response = obj.get()
    file_content = response['Body'].read().decode('utf-8')
    
    # Converte il file CSV in un DataFrame pandas
    #data = pd.read_csv(StringIO(file_content))
    #data = pd.read_csv(INPUT_CSV_FILE, usecols=[1, 6], header=None, skiprows=1
    data = pd.read_csv(INPUT_CSV_FILE, usecols=[1, 6], header=None, skiprows=1)
    data = data.sort_values(by='JUL', ascending=False)
    top_10 = data[['GPU NAME', 'JUL']].head(10)

    
    # Calcola la somma delle quantità possedute per ogni prodotto
    #data['Quantità posseduta'] = data.iloc[:, 2:7].sum(axis=1)
    #data['JUL'] = pd.to_numeric(data['JUL'], errors='coerce')
    
    # Ordina il DataFrame in base alla quantità posseduta e seleziona i primi 10 prodotti
    #top_10 = data[['GPU NAME', 'Quantità posseduta']].groupby('GPU NAME').sum().nlargest(10, 'Quantità posseduta')
    #top_10 = data[['GPU NAME', 'JUL']].groupby('GPU NAME').sum().nlargest(10, 'JUL')
    
    # Genera il file HTML con i 10 prodotti più posseduti
    html = top_10.to_html()
    soup = BeautifulSoup(html, 'html.parser')
    html_output = soup.prettify()
    
    # Carica il file HTML nel bucket S3 di output
    s3.Object(BUCKET_NAME, OUTPUT_HTML_FILE).put(Body=html_output)
    
    return {
        'statusCode': 200,
        'body': 'File HTML di output creato con successo.'
    }

