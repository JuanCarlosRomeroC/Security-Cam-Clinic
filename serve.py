from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	print(request.data)
	return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')