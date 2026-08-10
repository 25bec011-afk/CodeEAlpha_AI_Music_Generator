from pathlib import Path
import random
from music21 import stream, note, chord, tempo, meter, instrument

MELODIES = {
 "calm":[[60,62,64,67,64,62,60,55],[60,64,67,64,62,60,57,55],[67,65,64,62,60,62,64,60]],
 "happy":[[60,64,67,72,71,67,69,72],[62,64,67,69,72,71,69,67],[60,62,64,67,69,72,74,72]],
 "energetic":[[60,64,67,69,72,69,67,64],[62,65,69,72,76,72,69,65],[60,67,72,76,74,72,69,67]],
 "sad":[[60,63,67,65,63,60,58,55],[57,60,63,62,60,57,55,53],[60,62,63,67,65,63,60,58]]
}
CHORDS = {
 "calm":[[60,64,67],[57,60,64],[53,57,60],[55,59,62]],
 "happy":[[60,64,67],[65,69,72],[67,71,74],[62,65,69]],
 "energetic":[[60,64,67],[57,60,64],[65,69,72],[67,71,74]],
 "sad":[[60,63,67],[57,60,63],[53,57,60],[55,58,62]]
}

def model(sequences):
    t={}
    for seq in sequences:
        for a,b in zip(seq,seq[1:]):
            t.setdefault(a,[]).append(b)
    return t

def generate_music(output_path: Path, mood="calm", bpm=100, bars=8):
    mood = mood if mood in MELODIES else "calm"
    transitions=model(MELODIES[mood])
    seq=[random.choice(MELODIES[mood])[0]]
    for _ in range(bars*4-1):
        seq.append(random.choice(transitions.get(seq[-1], MELODIES[mood][0])))
    score=stream.Score()
    melody=stream.Part(); melody.insert(0,instrument.Piano())
    melody.insert(0,tempo.MetronomeMark(number=bpm)); melody.insert(0,meter.TimeSignature("4/4"))
    for i,p in enumerate(seq):
        n=note.Note(p,quarterLength=0.5 if i%7==0 else 1)
        n.volume.velocity=random.randint(65,100); melody.append(n)
    bass=stream.Part(); bass.insert(0,instrument.AcousticGuitar())
    bass.insert(0,tempo.MetronomeMark(number=bpm)); bass.insert(0,meter.TimeSignature("4/4"))
    for i in range(bars):
        c=chord.Chord(CHORDS[mood][i%4]); c.quarterLength=4; c.volume.velocity=30; bass.append(c)
    score.insert(0,melody); score.insert(0,bass)
    score.write("midi",fp=str(output_path))
