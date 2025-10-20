from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime

app = FastAPI(title="qingchao-laopian API")

# 允许跨域（先放开，后面可收紧）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TMP_DIR = "/tmp"  # Vercel 无状态，运行期只有 /tmp 可写

@app.get("/")
def hello():
    return {"ok": True, "msg": "API alive. POST /api/upload with a file field."}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    safe_name = f"{ts}_{file.filename or 'upload.bin'}"
    save_path = os.path.join(TMP_DIR, safe_name)

    # 保存到 /tmp
    with open(save_path, "wb") as f:
        f.write(await file.read())

    # 这里只做“先跑通”的测试，后续我们在这里接入视频降质 & 音频炸麦
    return JSONResponse({
        "ok": True,
        "message": "文件接收成功（后续将进行处理）",
        "saved_as": safe_name,
        "tmp_path": save_path
    })
