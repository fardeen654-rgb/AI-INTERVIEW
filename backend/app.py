from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import os, json, re
from dotenv import load_dotenv

load_dotenv()

# Point Flask to frontend folder directly (no templates subfolder)
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_groq(prompt, system_prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )
    content = response.choices[0].message.content
    content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
    return content


# ─── Serve Frontend ───────────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory('../frontend', 'index.html')


# ─── Generate Question ────────────────────────────────────────────────────────
@app.route("/api/generate-question", methods=["POST"])
def generate_question():
    try:
        data     = request.json
        role     = data.get("role", "")
        level    = data.get("level", "")
        focus    = data.get("focus", "")
        total    = data.get("total", 5)
        current  = data.get("current", 1)
        prev_qas = data.get("prev_qas", [])

        prev_text = ""
        if prev_qas:
            prev_text = "\n\nPrevious questions asked:\n"
            for i, qa in enumerate(prev_qas):
                prev_text += f"Q{i+1}: {qa['question']}\nA: {qa['answer']}\n\n"
            prev_text += "Make sure this question is different and builds naturally on the interview flow."

        prompt = f"""You are a professional interviewer. Generate interview question #{current} of {total} for:
- Role: {role}
- Level: {level}
- Focus: {focus}
{prev_text}

Return ONLY the question text, nothing else. No numbering, no preamble."""

        question = call_groq(
            prompt,
            "You are a professional, concise interviewer. Output only the question, no explanation."
        )
        return jsonify({"question": question.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Evaluate Answer ──────────────────────────────────────────────────────────
@app.route("/api/evaluate-answer", methods=["POST"])
def evaluate_answer():
    try:
        data     = request.json
        role     = data.get("role", "")
        level    = data.get("level", "")
        question = data.get("question", "")
        answer   = data.get("answer", "")

        prompt = f"""You are an expert interviewer evaluating a candidate.

Role: {role}
Level: {level}
Question: {question}
Candidate's Answer: {answer}

Provide a JSON response with this exact structure:
{{
  "score": <number 1-10>,
  "feedback": "<2-3 sentences of specific, constructive feedback on the answer>"
}}

Be fair but critical. Consider clarity, relevance, depth, and use of specific examples."""

        raw     = call_groq(prompt, "You are an expert interviewer. Return only valid JSON, no markdown, no explanation.")
        cleaned = re.sub(r"```json|```", "", raw).strip()
        parsed  = json.loads(cleaned)
        return jsonify(parsed)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)