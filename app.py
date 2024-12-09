from flask import Flask,render_template,request
import pickle
import numpy as np

#load training model
with open('model.pkl','rb') as file:
    model =pickle.load(file)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index1.html')

@app.route("/predict",methods=["POST"])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction = model.predict(final_features)
    output = 'Good' if prediction[0]==0 else "Hazarderous"
    if prediction[0]==0:
        output='Good'
    elif prediction[0]==1:
        output='Moderate'
    elif prediction[0]==2:
        output='Poor' 
    else: output='Hazardeous'
    return render_template('index1.html',prediction_text ="Prediction: {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)