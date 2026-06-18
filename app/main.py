from fastapi import FastAPI

app = FastAPI(
    title="DDR Report Generator",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "ddr-report-generator"
    }