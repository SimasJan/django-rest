import requests
import json

headers = {'Content-Type':'application/json'}
#delete a line ctrl+k
#copy a line 


def getSesssionId(start_response):
    for k,v in response.json().items():
        if 'id' in k:
            return v
        else:
            print('Error')


def buildCoreQuery():
    sbj = input('enter subject: ')
    rel = input('enter relationship: ')
    string = '{"subject"'+sbj+'","relationship":"'+rel+'"}'
    return stringed


main_query = [x for x in buildCoreQuery()]
