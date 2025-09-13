from flask import Flask, request, jsonify, render_template
import numpy as np
import json
import tensorflow as tf

app = Flask(__name__)

# Load the model
def load_model():
    with open('lstm_model.json', 'r') as json_file:
        model_json = json_file.read()
        model = tf.keras.models.model_from_json(model_json)
    # Load weights
    model.load_weights('lstm_model.keras')
    return model

model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_text', methods=['POST'])
def predict_text():
    data = request.json
    sentence = data['sentence']
    
    # Preprocess the text
    # Example: Convert to lowercase, tokenize, pad sequences, etc.
    # This step should be adapted to your preprocessing needs
    # For example, if using Keras Tokenizer:
    tokenizer = ... # Initialize your tokenizer
    text_sequence = tokenizer.texts_to_sequences([sentence])
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(text_sequence, padding='post')
    
    # Predict
    prediction = model.predict(padded_sequence)[0][0]
    sarcasm = "SARCASM" if prediction > 0.5 else "NOT SARCASTIC"
    
    return jsonify({'result': sarcasm, 'accuracy': round(prediction * 100, 2)})

@app.route('/predict_audio', methods=['POST'])
def predict_audio():
    file = request.files['audio']
    # Process the audio file
    # Convert to waveform, extract features, etc.
    # This part depends on your specific requirements
    # Example:
    audio_data = ... # Load and process the audio file
    # Transform audio data to match model input
    # Example: use a model to convert audio data to features
    features = ... # Extract features from audio
    features_sequence = np.array([features])
    
    # Predict
    prediction = model.predict(features_sequence)[0][0]
    sarcasm = "SARCASM" if prediction > 0.5 else "NOT SARCASTIC"
    
    return jsonify({'result': sarcasm, 'accuracy': round(prediction * 100, 2)})

if __name__ == '__main__':
    app.run(debug=True)
