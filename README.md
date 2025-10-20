# Audio Process API (FastAPI on Vercel)

Endpoints:
- `GET /` health
- `POST /upload` accepts video/audio file (multipart)

Writes to `/tmp` (the only writable path on Vercel Serverless).

## Local run
pip install -r requirements.txt
uvicorn api.index:app --reload --port 8000

## Deploy on Vercel
- New Project -> drag & drop this folder or import from Git
- After deploy, open your URL:
  - `GET /` returns health JSON
  - `POST /upload` with `file` field works