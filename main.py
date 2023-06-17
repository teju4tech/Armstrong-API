from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstong/<int:n>')
def armstong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = (n%10)
        sum += digit**order
        n //= 10
    
    if(sum==copy_n):
        print(f"{copy_n} is an armsong")
        result = {
            "Number": copy_n,
            "Armstong": True,
            "Server IP": "122.127.234.25",
            "Routing values": [1,231,500,3]
        }
    else:
        print(f"{copy_n} is not !!")
        result = {
            "Number": copy_n,
            "Armstong": False,
            "Server IP": "122.127.234.25",
            "Routing values": [1,231,500,3]

        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
    
