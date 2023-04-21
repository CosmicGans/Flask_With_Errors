from flask import Flask, render_template, request
from metrics import Metrics
app = Flask(__name__)
metrics = Metrics()
@app.route('/addition')
def add_numbers():
    num1 = int(request.args.get('num1')) 
    num2 = int(request.args.get('nu2'))
    result = num1 + num2 


    temp= render_template('results.html', num1=num1, num2=num2, result=result) 
    return temp
@app.route('/average')
def average(): 
    return metrics.get_current_average()


@app.route('/add_then_average')
def add_and_average():  
    
    num1 = int(request.args.get('num1'))   
    average = metrics.get_current_average()
    metrics.append(num1)
    return average
  


if __name__ == '__main__':
    app.run(debug=True)
