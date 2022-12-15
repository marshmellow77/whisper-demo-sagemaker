import whisper


def model_fn(model_dir):
    model = whisper.load_model("large-v2")
    return model


def predict_fn(audio_bytes, model):
    audio_file = "tmp.mp3"
    
    with open(audio_file, "wb") as binary_file:
        binary_file.write(audio_bytes['inputs'])
        
    result = model.transcribe(audio_file)

    # print the recognized text
    return {"detected_language": result["language"], "transcription": result["text"]}
