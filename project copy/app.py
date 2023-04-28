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
    result = knapsack(capacity, weights, values, n)
    return render_template('result.html', result=result)

def knapsack(W, wt, val, n):
    items = list(zip(wt, val))
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i - 1][0] <= w:
                K[i][w] = max(items[i - 1][1] + K[i - 1][w - items[i - 1][0]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]


if __name__ == '__main__':
    app.run(debug=True)
