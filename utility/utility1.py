BAD_REQUEST = {
    "response" : "400 BAD REQUEST"
    }



"""
[
    {
        "input_array": [0,0,0]
    }, 
    {
        "input_array": [0,0,0]
    }
]
if the input json format is as above, we use the following two method implementation of: 
    -get_data_from_request() and 
    -requestJson_is_in_format() method
"""
def get_data_from_request(request_data):
    # parse the list
    # get values for dict
    temp_list = []
    for i, data in enumerate(request_data):
        lst = []
        for j, data in enumerate(data['input_array']):
            lst.append(float(data))
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
            if not ('input_array' in keys):
                print("Request is not in format: problem with dict")
                return False
            values = data.values()
            print(f"values: {values}")
            if any( any(value<0 for value in sublist) for sublist in values):
                return False
    return True
