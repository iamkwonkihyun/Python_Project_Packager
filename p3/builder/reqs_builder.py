import subprocess

def reqs_builder():
    subprocess.run(["pipreqs", "./", "--encoding=utf-8", "--force"])
    
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]