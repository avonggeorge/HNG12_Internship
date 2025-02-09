from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(n))

def get_fun_fact(n):
    """Fetch a fun fact about the number using the Numbers API."""
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # Return the fun fact from the API
    return f"{n} is a fascinating number with unique properties."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Validate input
    if not number or not number.lstrip('-').isdigit():
        return jsonify({
            "number": number if number else "null",
            "error": True
        }), 400
    
    number = int(number)
    
    # Calculate properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    
    # Build response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
