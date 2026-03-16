from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    result = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100
        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            label = 'Underweight'
        elif bmi < 25:
            label = 'Normal'
        elif bmi < 30:
            label = 'Overweight'
        else:
            label = 'Obese'

        result = {'bmi': bmi, 'label': label}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(port=5000)