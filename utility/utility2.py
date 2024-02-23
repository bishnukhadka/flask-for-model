BAD_REQUEST = {
    "response" : "400 BAD REQUEST"
    }

"""
if the input json format is as below, we use the commented out 
    -get_data_from_request() and 
    -requestJson_is_in_format() method
[
    {
    "attendanceScore": "0.2",
    "assestmentScore": 0.9,
    "assignmentScore": 0.8
},
{
    "assestmentScore": 0.9,
    "attendanceScore": 0.9,
    "assignmentScore": 0.9
}
]
"""

def get_data_from_request(request_data):
    # parse the list
    # get values for dict
    temp_list = []
    for i, data in enumerate(request_data):
        lst = []
        lst.append(float(data['attendanceScore']))
        lst.append(float(data['assestmentScore']))
        lst.append(float(data['assignmentScore']))
        print(f"lst: {lst}")
        temp_list.append(lst)
    print(f"temp_list: {temp_list}")
    return temp_list

def requestJson_is_in_format(request_data):
    if not isinstance(request_data, list):
        print("Request not in format: request not a list")
        return  False
    else:
        for data in request_data:
            keys = data.keys()
            if not ('attendanceScore' in keys and 'assestmentScore' in keys and 'assignmentScore' in keys):
                print("Request is not in format: problem with dict")
                return False
            values = data.values()
            if any(float(value)<0 or float(value)>1 for value in values):
                return False
    return True   