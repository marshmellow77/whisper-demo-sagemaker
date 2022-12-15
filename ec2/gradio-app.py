import gradio as gr
import boto3
import json
from iso639 import languages


def transcribe(microphone, file_upload):
    output = ""
    if (microphone is not None) and (file_upload is not None):
        output = (
            "WARNING: You've uploaded an audio file and used the microphone. "
            "The recorded file from the microphone will be used and the uploaded audio will be discarded.\n\n"
        )

    elif (microphone is None) and (file_upload is None):
        return "ERROR: You have to either use the microphone or upload an audio file"

    filename = microphone if microphone is not None else file_upload
#    print(type(file))
    file = open(filename, "rb")
    audio_content = file.read()
    
    endpoint_name = "whisper-large-v2-2022-12-15-18-55-47-431"
    sagemaker_runtime = boto3.client('runtime.sagemaker', region_name="us-east-1")
    
    res = sagemaker_runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='audio/x-audio',
            Body=audio_content
    )
    
    d = json.loads(res['Body'].read().decode())
    detected_lang_code = d['detected_language']
    if detected_lang_code == "iw":
        detected_lang_code = "he"
    try:
        detected_lang = languages.get(alpha2=detected_lang_code).name
    except:
        detected_lang = detected_lang_code
    transcription = d['transcription']
    
    language = f"Detected language: {detected_lang}\n\n"

    return output + language + transcription


demo = gr.Interface(
    fn=transcribe,
    inputs=[
        gr.inputs.Audio(source="microphone", type="filepath", optional=True),
        gr.inputs.Audio(source="upload", type="filepath", optional=True),
#        gr.inputs.FileUpload(accept="audio/mpeg"),
    ],
    outputs="text",
    layout="horizontal",
    theme="huggingface",
    title="Whisper Demo: Transcribe Audio",
    description=(
        "Transcribe long-form microphone or audio inputs with the click of a button!"
    ),
    allow_flagging="never",
)

demo.launch(server_port=8501, share=True)