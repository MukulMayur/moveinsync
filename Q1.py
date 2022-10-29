from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/c', methods=['GET'])
def helloworld():
	if(request.method=='GET'):
		data=[
			{
			    "userid":1,
			    "customerName":"Mukul Mayur",
			    "email":"mukulmayur123@gmail.com",
			    "mobileNo":"3456734567",
			    "city":"Banglore"
	    	},
			{
				"userid":2,
				"customerName": "Gaurav Naik",
				"email": "gauravnaik@gmail.com",
				"mobileNo": "798766789",
				"city": "Banglore"

			},
			{
				"userid": 3,
				"customerName": "Abhishek Kumar",
				"email": "abhishekumar@gmail.com",
				"mobileNo": "678902345",
				"city": "Banglore"
			},
			{
				"userid": 4,
				"customerName": "Aditya Singh",
				"email": "adityasingh@gmail.com",
				"mobileNo": "7867898765",
				"city": "Banglore"
			},
			{
				"userid": 5,
				"customerName": "Maddy Sen",
				"email": "maddysen@gmail.com",
				"mobileNo": "7023985018",
				"city": "Banglore"
			}
		]
		return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True)
