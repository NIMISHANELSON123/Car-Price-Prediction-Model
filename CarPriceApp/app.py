from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        enginesize = float(request.form['enginesize'])
        curbweight = float(request.form['curbweight'])
        horsepower = float(request.form['horsepower'])
        
        # Prepare feature array
        final_features = np.array([[enginesize, curbweight, horsepower]])
        
        # Make prediction
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        
        # Result text including the input values
        result_text = f"Estimated Car Price: ${output} (Engine Size: {enginesize}, Curb Weight: {curbweight}, Horsepower: {horsepower})"
        
        return render_template('index.html', prediction_text=result_text)
        
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)