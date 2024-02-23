from flask import Flask, request, render_template
import pickle
import numpy as np
from flask_restful import Api
app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')

# for local running, test with index.html
@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the request
    feature1 = float(request.form['feature1'])
    feature2 = float(request.form['feature2'])
    feature3 = float(request.form['feature3'])

    print(f"{feature1}, {feature2}, {feature3}")

    # Preprocess the input features
    # Make predictions using the loaded model
    prediction = model.predict([[feature1, feature2, feature3]])
    print(f"prediction: {prediction}")

    #Process the prediction
    max_indices_per_row = np.argmax(prediction, axis=1)

    return render_template('index.html', prediction=max_indices_per_row[0] if max_indices_per_row!=0 else "zero")


if __name__ == '__main__':
    # Load the model
    print("Model Loading ...")
    with open("assets\model.pkl", "rb") as f:
        model = pickle.load(f)
    app.run(debug=True)