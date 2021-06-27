import os
from dotenv import load_dotenv

load_dotenv('.env')

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'host.docker.internal',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PASS': os.environ.get('SOURCE_DB_PASS')           
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'host.docker.internal',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_PASS')       
        }
    },
}