from flask import Flask, request, jsonify

app = Flask(__name__)

def compute_fibonacci(n):
    if n < 0:
        raise ValueError("Input must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n', 0))  # Default to 0 if no input
        result = compute_fibonacci(n)
        return jsonify({"input": n, "result": result}), 200
    except ValueError:
        return jsonify({"error": "Input must be an integer"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)