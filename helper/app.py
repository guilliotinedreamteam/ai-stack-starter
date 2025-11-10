from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Helper service for Stable Diffusion stack."}

@app.get("/health")
async def health():
    return {"status": "ok"}
