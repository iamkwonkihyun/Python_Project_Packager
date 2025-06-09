import subprocess

def reqs_builder(exist: bool = False) -> list[str]:
    """requirements.txt 생성 함수

    Returns:
        list[str]: requirements.txt의 list
    """
    
    if not exist:
        subprocess.run(["pipreqs", ".", "--encoding=utf-8", "--force"])
    
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]