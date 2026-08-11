# 🎵 MelodyAI — AI Music Generator

## 🌐 Live Demo

👉 **[Open the Live Website](https://codeealpha-ai-music-generator.onrender.com)**

## 📌 CodeAlpha Internship — Task 3

AI Music Generation using Python, Flask, music21 and a probabilistic sequence model.# MelodyAI — CodeAlpha AI Internship Task 3

AI Music Generation web application. It generates original symbolic melodies as MIDI using a lightweight probabilistic sequence model trained on mood-specific melody patterns.

## Features
- Calm, Happy, Energetic and Sad moods
- 60–160 BPM tempo control
- 4/8/16/32 bar generation
- Probabilistic note-transition model
- Melody + chord accompaniment
- MIDI playback/download
- Flask web interface

## AI approach
The generator learns note-to-note transition probabilities from a small symbolic melody corpus. It then samples a new sequence from those learned transitions. This is a lightweight generative AI approach that avoids multi-gigabyte pretrained audio models.

## Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Task mapping
- AI music generation: probabilistic sequence model
- User controls: mood, tempo, length
- Output: generated MIDI
- Playback/download: browser audio + MIDI download
- Explanation: included in the UI and README

## LinkedIn
> 🎵 Built an AI Music Generation project for the CodeAlpha AI Internship — Task 3. It generates original symbolic melodies using probabilistic sequence modeling, mood controls, tempo controls and MIDI output. #CodeAlpha #ArtificialIntelligence #AIMusic #Python #Internship
