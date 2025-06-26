# from flask t Flask, request, jsonify
from flask import Flask, request, jsonify
from flask_cors import CORS
from pprint import pprint
from app import get_chat


app= Flask(__name__)
CORS(app)



@app.route("/chat",methods=["POST"])
def chat_sesssion():
    data=request.json
    user_id=data.get("UserId","anonymous")
    chat_input=data.get("chatInput")

    if not chat_input:
        return jsonify({"error":"missing input"}),400
    
    try:
        result=get_chat(user_id,chat_input)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error":str(e)}),500
    

if __name__=="__main__":
    app.run(debug=True,port=5000)
