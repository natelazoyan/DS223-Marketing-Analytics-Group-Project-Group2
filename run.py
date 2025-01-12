import subprocess
import webbrowser
from CLV_Analysis.API import main


def start_fastapi():
    subprocess.run(["uvicorn", "CLV_Analysis.API.main:app", "--reload"])
    webbrowser.open('http://127.0.0.1:8000/docs#/')


name = "__main__"

if name == "__main__":
    start_fastapi()
