from ppb.builder.setup_builder import setup_builder
from ppb.builder.exe_builder import exe_builder
from ppb.builder.reqs_builder import reqs_builder

def main():
    while True:
        reqs_input = input("do you need requirements.txt? (y/n): ").strip().lower()
        
        if reqs_input in ("y", "n"):
            reqs_input = True if reqs_input == "y" else False
            break
        else:
            continue
    
    while True:
        exe_input = input("do you need convert to exe? (y/n): ").strip().lower()
        
        if exe_input in ("y", "n"):
            exe_input = True if exe_input == "y" else False
            break
        else:
            continue
    
    while True:
        setup_input = input("do you need add to setup.py? (y/n): ").strip().lower()
        
        if setup_input in ("y", "n"):
            setup_input = True if setup_input == "y" else False
            break
        else:
            continue
    
    # requirements.txt 생성
    if reqs_input:
        reqs_builder()
    # exe로 빌드
    if exe_input:
        exe_builder()
    # setup.py 생성
    if setup_input:
        setup_builder()