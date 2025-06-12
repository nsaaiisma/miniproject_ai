
from flask import Flask, render_template, request
from pitch_detect import record_audio, get_main_pitch, estimate_note
from spotify import search_song_by_pitch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/detect', methods=['POST'])
def detect():
    audio = record_audio()
    pitch = get_main_pitch(audio)
    note = estimate_note(pitch)
    songs = search_song_by_pitch(note)
    return render_template('index.html', result=songs, note=note)

if __name__ == '__main__':
    app.run(debug=True)
