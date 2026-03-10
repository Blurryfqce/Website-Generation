from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS
import os

client = OpenAI(
    base_url= "https://openrouter.ai/api/v1",
    api_key= os.getenv("OPEN_API_KEY")
)

app = Flask(__name__)
CORS(app)
sessions = {}

@app.route("/build", methods= ["POST"])
def build():
    try:
        data = request.json
        user_message = data["message"]
        session_id = data["session_id"]
        
        template = """
            You are a specialized Web Developer GPT. 
            
            INTENT GUIDELINES:
            - If the user provides a specific topic or request for a website, build it according to the technical requirements below.
            - If the user engages in small talk (e.g., "Hi", "How are you?"), respond naturally and briefly as a developer, then ask what kind of website they want to build. Do not build a random website for small talk.

            TECHNICAL REQUIREMENTS:
            - Return only a single HTML file containing CSS (in <style>) and JS (in <script>).
            - Use responsive, modern design with interactive elements.
            - Avoid irrelevant comments.
            - Output the code and NOTHING else.
            
            CRITICAL: No external .css or .js files.
        """

        if session_id not in sessions:
            sessions[session_id] = [
                {"role": "system", "content":template}
            ]
            
        sessions[session_id].append(
            {"role": "user", "content": user_message}
        )

        response = client.chat.completions.create(
            model = "stepfun/step-3.5-flash:free",
            messages=sessions[session_id],
            temperature=0.6
        )
        reply = response.choices[0].message.content
        
        sessions[session_id].append(
            {"role": "assistant", "content": reply}
        )
        
        # print(session_id)
        
        if len(sessions[session_id]) > 5:
            del sessions[session_id]
            
        return jsonify({
                "response" : reply
            })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug= True)
    # app.run(debug=False, host="0.0.0.0", port=5000)