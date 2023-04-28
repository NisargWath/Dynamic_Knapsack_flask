from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    capacity = int(request.form.get('capacity'))
    weights = [int(i) for i in request.form.get('weights').split()]
    values = [int(i) for i in request.form.get('values').split()]
    n = len(values)
    result = knapsack_backtracking(weights, values, capacity, n)
    return render_template('result.html', result=result)

def knapsack_backtracking(weights, values, capacity, n):
    def backtrack(i, current_weight, current_value):
        nonlocal best_value
        if current_weight <= capacity and current_value > best_value:
            best_value = current_value
        if i >= n or current_weight >= capacity:
            return
        # Explore the possibility of taking the item
        backtrack(i + 1, current_weight + weights[i], current_value + values[i])
        # Explore the possibility of not taking the item
        backtrack(i + 1, current_weight, current_value)

    items = list(zip(weights, values))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    best_value = 0
    backtrack(0, 0, 0)
    return best_value


if __name__ == '__main__':
    app.run(debug=True)
