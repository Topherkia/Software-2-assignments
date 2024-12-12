from flask import Flask, jsonify

app = Flask(__name__)


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True


@app.route('/prime_number/<int:num>', methods=['GET'])
def primeNumber(num):
    result = {
        "Number": num,
        "isPrime": isPrime(num)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)