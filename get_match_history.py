import requests
from pymongo import MongoClient
import dotenv
import os
# carrega o dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

MONGODB_IP = os.getenv("MONGODB_IP")
MONGODB_PORTA = os.getenv("MONGODB_PORTA")

def get_match_batch(min_match_id=None):

    ''' 
        Captura lista de partidas pro players
        caso seja passada um id de partida, a coleta é realizada a partir desta
    '''
    url = "https://api.opendota.com/api/proMatches"
    
    if min_match_id is not None:
        url += f"?less_than_match_id={min_match_id}"
    
    data = requests.get(url).json()

    return data

def save_matches(data,db_collection):
    '''Salva lista de partidas no banco de dados'''
    
    db_collection.insert_many(data)

    return True    


mongodb_client = MongoClient(os.getenv(MONGODB_IP,MONGODB_PORTA))
mongodb_database = mongodb_client["dota_raw"] 

data = get_match_batch()
save_matches(data,mongodb_database['pro_match_history'])


