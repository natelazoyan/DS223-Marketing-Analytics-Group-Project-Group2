import subprocess
import webbrowser

def start_fastapi():
    subprocess.run(["uvicorn", "main:app", "--reload"])
    webbrowser.open('http://127.0.0.1:8000/docs')

name = "__main__"

if name == "__main__":
    start_fastapi()