from elasticsearch import Elasticsearch

def ping_db(ip, port):
    connection = Elasticsearch([{
        'host': ip,
        'port': port,
        'scheme': 'http'
    }])

    if not connection.ping():
        raise Exception('Connection failed...')
    print('Connection successful...')

    return connection


def confirm_index(connection, index_name, vec_dim):
    body = {
        'mappings': {
            'properties': {
                'question': {'type': 'text'},
                'vector': {'type': 'dense_vector', 'dims': vec_dim},
                'id': {'type': 'long'}
            }
        }
    }

    try:
        if not connection.indices.exists(index_name):
            connection.indices.create(index=index_name, body=body)
    except Exception as e:
        print(str(e))

