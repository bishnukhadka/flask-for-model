from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_restful import Api, Resource, reqparse
import json
from utility.utility1 import * 
app = Flask(__name__)
api = Api(app)

# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')     


# Define how the api will respond to the post requests
#Here we have inherited from Resource class of flask module and overwritten the post() method. other method is default.
class StudentModel(Resource):
    def post(self):
        request_data = request.get_json()
        print(f"request_data: {request_data}") 
        if(requestJson_is_in_format(request_data)):
            print("Data is in format")
            list2D_from_request = get_data_from_request(request_data)
        else:
            bad_request_mesage = json.dumps(BAD_REQUEST)
            return bad_request_mesage, 400


        # Preprocess the input features
        # Make predictions using the loaded model
        prediction = model.predict(list2D_from_request)
        print(f"prediction: {prediction}")

        #Process the prediction
        max_indices_per_row = np.argmax(prediction, axis=1).tolist()
        print(f"max: {max_indices_per_row}")
        response_data = {
            "status": "200 OK",
            "prediction": max_indices_per_row
        }
        return jsonify(response_data)

api.add_resource(StudentModel, '/predict')
with open("assets\\model.pkl", "rb") as f:
        model = pickle.load(f)

# The code below is for running locally only, do not push this to productoin. 
# if __name__ == '__main__':
#     app.run(debug=False)