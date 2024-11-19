from flask import Flask, request, jsonify
import os
import requests
import json
import traceback
import base64

app = Flask(__name__)

@app.route('/lyra_payin', methods=['POST', 'GET'])
def lyra_payin():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    request_data = {
      "orderId": "It-23920DK-1",
      "orderInfo": "Shopping cart with #1 item 23920DK",
      "currency": "INR",
      "amount": 100,
      "customer": {
        "name": "swathi",
        "emailId": "swathi@gmail.com",
        "phone": "+1234567890"
      },
      "webhook": {
        "url": "https://18.188.39.218/api/frontend/lyra_testing_callback"
      }
    }
 
    url="https://api.in.lyra.com/pg/rest/v1/charge"
    username = "20753740"
    password = "testpassword_j98abAdPr1sUznplPZksKwKlhxq8WAIG0GkEeUPUXppeH"
    
    credentials = f"{username}:{password}"
    
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
    headers["Authorization"] = f"Basic {encoded_credentials}"
    
    try:
        response = requests.post(url,json=request_data, headers=headers)

        if response :

            lyraResponseData = json.loads(response.text)
            print("Paywize Response Data:", lyraResponseData)
            return jsonify(lyraResponseData), 200
        else:
            print("Failed to create payment")
            return jsonify({"error": "Failed to create payment"}), 400

    except Exception as e:
        print("Internal server error:", e)
        return jsonify({"error": "Internal server error"}), 500


@app.route('/lyra_status_Check',methods=['GET'])
def lyra_status_Check() :
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    username = "20753740"
    password = "testpassword_j98abAdPr1sUznplPZksKwKlhxq8WAIG0GkEeUPUXppeH"
    
    credentials = f"{username}:{password}"
    
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
    headers["Authorization"] = f"Basic {encoded_credentials}"
    uuid="84e3b75b900d4652a2a36f1668f04578"
    status_url=f"https://api.in.lyra.com/pg/rest/v1/charge/{uuid}"
    try:
        lyra_status=requests.get(status_url, headers=headers)
        print(lyra_status,"(((((((((((lyra_status)))))))))))")
        if lyra_status:
            lyraStatusResponseData = json.loads(lyra_status.text)
            print("Lyra status Response Data:", lyraStatusResponseData)
            return jsonify(lyraStatusResponseData), 200
        else:
            print("Failed to fetch status ")
            return jsonify({"error": "Failed to fetch status"}), 400

    except Exception as e:
        print("Internal server error:", e)
        return jsonify({"error": "Internal server error"}), 500


@app.route("/lyra_testing_callback",methods=["POST"])
def lyra_testing_callback():
    data_status = {"responseStatus":1, "result": "success"}
    print(request.json,"lyra card check term request.json")
    print(request.data,"lyra card check term request.data")
    print(request.form,"lyra card check term request.form")
    return

if __name__ == '__main__':
    app.run(debug=True)