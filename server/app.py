from flask import Flask

app = Flask(__name__)

# Index view: Displays title in an h1 element
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print_string view: Takes a string, prints to console, and displays in browser
@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  # Prints the string to the console
    return parameter  # Just return the string without any HTML tags

# Count view: Takes an integer and displays all numbers up to that integer
@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a string of numbers from 0 to parameter-1, joined by newlines
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers  # Return the numbers as plain text with newlines

# Math view: Takes two numbers and performs an operation
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' or operation == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    
    # Return only the result (e.g., 10) instead of the equation
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
