from flask import Flask, request, jsonify
from register import add_user, is_valid_email, generate_token

app = Flask(__name__)

@app.route('/api/register/', methods=['POST'])
def register_user():
    data = request.get_json()
    if 'email' not in data:
        return jsonify({"error": "Missing email parameter"}), 400

    email = data['email']
    if is_valid_email(email):
        token = generate_token()
        add_user(email, token, 'db.json')
        return jsonify({"email": email, "token": token}), 200
    else:
        return jsonify({"error": "Invalid email"}), 400

if __name__ == '__main__':
    app.run(debug=True)

