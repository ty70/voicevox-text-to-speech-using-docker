import streamlit as st
from utils import synthesize_voice
import os

st.title("🎤 VOICEVOX テキスト読み上げアプリ")
st.markdown("日本語テキストを入力して、VOICEVOXで音声合成します。")

text = st.text_area("📄 読み上げるテキストを入力", "こんにちは。今日はいい天気ですね。")
speaker_id = st.selectbox("🔊 話者を選択", options=[1, 3, 14], format_func=lambda x: {
    1: "四国めたん",
    3: "ずんだもん",
    14: "青山龍星"
}.get(x, f"ID {x}"))

if st.button("▶️ 音声生成"):
    if text.strip():
        output_path = synthesize_voice(text, speaker_id)
        if output_path and os.path.exists(output_path):
            audio_file = open(output_path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            st.download_button("💾 音声をダウンロード", audio_bytes, file_name="voice.wav")
        else:
            st.error("音声の生成に失敗しました。")
    else:
        st.warning("テキストを入力してください。")