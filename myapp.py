import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)



def post_data():
    data={
        "name":"himel",
        "roll":22,
        "city":"masdir"
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)





def update_data():
    data={
        'Id':4,
        'name':'sarfaraz himel',
        'roll':22,
        'city':'narayanganj',
    }
    json_data=json.dumps(data)
    r= requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data={
        'Id':2,

    }
    json_data=json.dumps(data)
    r= requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)


if __name__=='__main':
    # get_data(2)
    # post_data()
    # update_data()
       delete_data()
