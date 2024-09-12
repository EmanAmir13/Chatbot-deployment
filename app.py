from flask import Flask, request, jsonify, render_template

from chat import get_response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_message = data['message']
    response = get_response(user_message)
    return jsonify({'answer': response})


if __name__ == '__main__':
    app.run(debug=True)
