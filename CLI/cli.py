import coreapi

client = coreapi.Client()
schema = client.get('http://127.0.0.1:8000/')

action = ['api-token-auth','create']
params = {"username":"example","password":"secret"}
result = client.action(schema, action, params)

auth = coreapi.auth.TokenAuthentication(
    scheme='JWT',
    token='<token>'
)

client = coreapi.Client(auth=auth)

users = client.action(schema, ['users','list'])

new_user = client.action(schema, ['users','create'], param={"username":"max"})


users = client.action(scema, ['users','list'])

