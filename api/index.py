from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime

app = FastAPI(title="qingchao-laopian API")

# 允许跨域（后续可以收紧到你的域名）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TMP_DIR = "/tmp"  # Vercel 运行时可写目录

@app.get("/")
def ping():
    return {"ok": True, "msg": "API alive. Use POST /api/upload"}

@app.post("/api/upload")   # ✅这里修改了
async def upload(file: UploadFile = File(...)):
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    safe_name = f"{ts}_{file.filename or 'upload.bin'}"
    save_path = os.path.join(TMP_DIR, safe_name)
    with open(save_path, "wb") as f:
        f.write(await file.read())

    return JSONResponse({
        "ok": True,
        "message": "文件接收成功（下一步加入处理逻辑）",
        "saved_as": safe_name,
        "tmp_path": save_path
    })
