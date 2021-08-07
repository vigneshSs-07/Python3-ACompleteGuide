#Object in JSON
{
    "person" :
    {
            "emp_name" : "neethu",
            "emp_id": "1091594",
            "emp_salary" : 1200000,
            "dateofjoining" : "23-Feb 2017"
        
    }
}

#Array of JSON
{
    "person" : ["neethu", "TCS", "23-02-2017"]
}

json.dumps()

#import module
import json

#Json objects#Serialization Example
person = {"name":"Neethu", "age":27, "city":"Chennai"}
## conversion to JSON done by dumps() function
person_details = json.dumps(person)
print(person_details)
print(type(person_details))


#DeSerialization Example
json_var ="""
{
    "Country": {
        "name": "INDIA",
        "Languages_spoken": [
            {
                "names": ["Hindi", "English", "Bengali", "Telugu"],
                "symbol": ["$","%","!","@"]
            }
        ]
    }
}
"""
var = json.loads(json_var)
print(var)

#Encoding and Decoding
import demjson
# Encoding, storing marks of 3 subjects
var = [{"Math": 50, "physics":60, "Chemistry":70}]
print(demjson.encode(var))