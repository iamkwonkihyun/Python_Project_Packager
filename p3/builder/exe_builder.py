import os
import subprocess
from p3.builder.functions import qna_func, yes_or_no_func

def exe_builder():
    # 화면 지우기
    os.system('cls' if os.name == 'nt' else 'clear')
    print("## exe builder ##")
    
    # 기본 명령어
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconfirm",
        "--clean",
    ]
    
    check = False
    
    while not check:
        
        program_type = qna_func("GUI or CLI?: ", ["gui", "cli"])
        python_file = qna_func("python file name: ")
        program_name = qna_func("program name: ")
        
        if yes_or_no_func("Are you going to add an icon?:", default=False):
            program_icon = qna_func("icon_path: ")
        else:
            program_icon = None
        
        exe_info = {
        "program_type": program_type,
        "python_file": python_file,
        "program_name": program_name,
        "program_icon": program_icon
        }
        
        for item, answer in exe_info.items():
            print(f"{item}: {answer}")
            
        check = yes_or_no_func("다시 한번 확인해주세요. 이걸로 결정하시겠습니까?")
    
    cmd.append(python_file)
    cmd.append("-c" if program_type == "cli" else "-w")
    cmd.append(f"-n {program_name}")
    if program_icon is not None:
        cmd.append(f"--icon {program_icon}")
    
    # 명령어 실행
    subprocess.run(cmd)

exe_builder()