import subprocess

def reqs_builder():
    with open("requirements.txt", "w") as f:
            subprocess.run(["pip", "freeze"], stdout=f)
    
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]