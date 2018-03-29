from flask import Flask, request, jsonify

app = Flask(__name__)

def get_BMI(height, weight, sex='male'):
    #Calculates BMI and BMI category
    BMI = float(weight) / (float(height)/100)**2
    if sex == 'male': #default class as it has larger bins
        if BMI < 16:
            category = 'Severly underweight'
        elif BMI <18.5:
            category = 'Underweight'
        elif BMI <25:
            category = 'Healthy'
        elif BMI <30:
            category = 'Overweight'
        else:
            category = "Obese"
    elif sex == 'female':
        if BMI < 16:
            category = 'Severly underweight'
        elif BMI <18.5:
            category = 'Underweight'
        elif BMI <24:
            category = 'Healthy'
        elif BMI <29:
            category = 'Overweight'
        else:
            category = "Obese"
    #return a dict which will be converted to JSON
    return {"BMI": BMI, "category": category, "data": {"height": height, "weight": weight, "sex": sex}}

def process_request(query):
    if 'height' in query.keys() and 'weight' in query.keys():
        if 'sex' in query.keys():
            response = get_BMI(query['height'], query['weight'], sex=query['sex'])
        else:
            response = get_BMI(query['height'], query['weight'])
    else:
        response = {"error": "'height' and 'weight' are required"}
    return jsonify(response)

@app.route('/api')
def API():
    return process_request(request.args) #get URL arguments

if __name__ == "__main__":
    app.run(debug=True)
