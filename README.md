# VOICEVOX Text-to-Speech Web App with Streamlit using Docker

This project is a Streamlit-based web application that synthesizes Japanese speech from text using the VOICEVOX engine, which is run inside Docker.

---

## ✨ Features

* Easy-to-use voice synthesis through a Streamlit web UI in your browser

* The VOICEVOX engine runs in Docker (requires Docker with NVIDIA GPU support)

* Includes speaker selection, audio playback, and download functionality

---

## ⚡ How to Run

### 1. Build the VOICEVOX engine in Docker

#### Pull and run the Docker image

```bash
docker pull voicevox/voicevox_engine:nvidia-latest
docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-latest
```

This will start the VOICEVOX engine.

### 2. Install required Python packages

In a separate terminal:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install streamlit requests
```

### 3. Launch the Streamlit app

```bash
streamlit run app.py
```

Once running, the app will be accessible in your web browser.

### 4. Stop the VOICEVOX ENGINE

```bash
docker stop `docker ps | grep voicevox | awk '{print $1}'`
```

To remove the container image if needed:

```bash
docker rmi `docker images | grep voicevox | awk '{print $3}'`
```

---

## 🌐 App Features

* Text input: Any Japanese text

* Speaker selection: Choose from Shikoku Metan, Zundamon, Ryusei Aoyama, etc. (via speaker ID)

* Speech generation: Uses the VOICEVOX API

* Playback and download: Provided in WAV format

---

## 🛠 Structure

```
.
├─ app.py            # Main Streamlit app
├─ LICENSE           # License
├─ README_ja.md      # japanese version
├─ README.md         # This file
├─ requirements.txt  # Required packages
└─ utils.py          # Voice generation functions
```

---

## 🗕 TODO / Future Plans

* Speed and pitch adjustment
* Batch generation with multiple speakers
* Save input history

---

## ✅ LICENSE

This project is licensed under the [MIT License](./LICENSE).
Please refer to VOICEVOX's official license and terms of use for using the VOICEVOX engine.

---

## 🙏 Special Thanks

* The VOICEVOX development team
* [VOICEVOX ENGINE](https://github.com/VOICEVOX/voicevox_engine)
* [Hiroshiba](https://github.com/hiroshiba)
