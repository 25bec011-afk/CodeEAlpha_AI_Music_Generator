from flask import Flask, render_template, request, jsonify, send_file
from music_generator import generate_music
from pathlib import Path
import uuid

app = Flask(__name__)
OUT = Path("generated"); OUT.mkdir(exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/generate")
def generate():
    data = request.get_json(silent=True) or {}
    mood = data.get("mood", "calm")
    tempo = max(60, min(160, int(data.get("tempo", 100))))
    bars = max(4, min(32, int(data.get("bars", 8))))
    try:
        name = f"melody_{uuid.uuid4().hex}.mid"
        path = OUT / name
        generate_music(path, mood, tempo, bars)
        return jsonify({"success": True, "file": f"/audio/{name}",
                        "message": "AI-generated melody created successfully."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.get("/audio/<filename>")
def audio(filename):
    path = OUT / filename
    return send_file(path, mimetype="audio/midi") if path.exists() else ("File not found", 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
