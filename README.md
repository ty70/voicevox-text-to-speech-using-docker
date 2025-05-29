# VOICEVOX Text-to-Speech Web App with Streamlit using Docker

このプロジェクトは、VOICEVOX エンジンを Docker で実行、利用して日本語テキストから音声を合成する Streamlit ベースの Web アプリケーション です。

---

## ✨ 特徴

* Streamlit Web UI により、簡単にブラウザ上で音声合成が可能

* VOICEVOXエンジンは Dockerで実行、利用(nvidia対応のDockerがインストールされている事が前提)

* 話者の選択、音声再生、ダウンロード機能を搭載

---

## ⚡ 実行方法

### 1. VOICEVOXエンジンをDocker上で構築する

#### Dockerイメージの取得、起動
```bash
docker pull voicevox/voicevox_engine:nvidia-latest
docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-latest
```
これでVOICEVOXエンジンが起動します。

### 2. 必要パッケージのインストール
別のターミナルにて
```bash
pip install -r requirements.txt
```

または：

```bash
pip install streamlit requests
```

### 3. Streamlit アプリ起動
```bash
streamlit run app.py
```
正常に起動するとWebページ上で操作可能になります。

### 4. VOICEVOX ENGINE を停止する方法
```bash
docker stop `docker ps | grep voicevox | awk '{print $1}'`
```

必要に応じてコンテナを削除するには：
```bash
docker rmi `docker images | grep voicevox | awk '{print $3}'`
```
---

## 🌐 アプリ機能

* 文本入力: 任意の日本語テキスト

* 話者選択: 四国めたん、ずんだもん、青山龍星など（speaker ID使用）

* 音声生成: VOICEVOX APIを使用

* 再生・ダウンロード: WAV形式で提供

---

## 🛠 構成

```
.
├─ app.py            # Streamlitアプリ本体
├─ LICENSE           # ライセンス
├─ README.md         # このファイル
├─ requirements.txt  # 必要パッケージ
└─ utils.py          # 音声生成関数
```
---

## 📅 TODO / 拡張案

* 速度・ピッチ調整
* 複数話者一括生成
* 入力履歴の保存

---

## ✅ LICENSE

このプロジェクトは [MIT ライセンス](./LICENSE)で提供されます。
VOICEVOXエンジンの使用については、
VOICEVOX公式のライセンス・利用規約に従ってください。

---

## 🙏 Special Thanks

* VOICEVOX開発チーム
* [VOICEVOX ENGINE](https://github.com/VOICEVOX/voicevox_engine)
* [Hiroshiba氏](https://github.com/hiroshiba)