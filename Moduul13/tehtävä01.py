from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = is_prime(number)
    return jsonify({"Number": number, "isPrime": result})


app.run(debug=True)
