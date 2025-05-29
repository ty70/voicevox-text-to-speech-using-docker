import requests
import json

VOICEVOX_ENGINE_URL = "http://localhost:50021"

def synthesize_voice(text: str, speaker: int = 1, output_path="output.wav"):
    # audio query
    query_resp = requests.post(
        f"{VOICEVOX_ENGINE_URL}/audio_query",
        params={"text": text, "speaker": speaker}
    )

    if query_resp.status_code != 200:
        return None

    # synthesis
    synthesis_resp = requests.post(
        f"{VOICEVOX_ENGINE_URL}/synthesis",
        params={"speaker": speaker},
        data=json.dumps(query_resp.json()),
        headers={"Content-Type": "application/json"}
    )

    if synthesis_resp.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(synthesis_resp.content)
        return output_path
    return None
