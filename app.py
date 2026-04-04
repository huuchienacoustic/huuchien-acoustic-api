from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import librosa

app = FastAPI()

# 🔥 CORS (bắt buộc)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "HuuChien Acoustic API running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    audio_bytes = await file.read()

    with open("temp.wav", "wb") as f:
        f.write(audio_bytes)

    y, sr = librosa.load("temp.wav", sr=None)

    rt60 = round(np.random.uniform(0.3, 1.2), 2)
    spl = round(np.mean(np.abs(y)) * 100, 2)

    return {"rt60": rt60, "spl": spl}