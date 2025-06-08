import subprocess

def exe_builder():
    
    # 기본 명령어
    cmd = [
        "pyinstaller",
        "--onefile",
        "--noconfirm",
        "--clean",
    ]
    
    # cli 프로그램이면 -c, gui 프로그램이면 -w
    while True:
        program_type_input = input("GUI or CLI?: ").strip().lower()
        
        if program_type_input not in ("gui", "cli"):
            print("잘못된 입력 값 입니다.")
            continue
        else:
            cmd.append("-c" if program_type_input == "cli" else "-w")
            break
    
    # 프로그램 name 옵션
    while True:
        program_name_input = input("program name: ")
        check_program_name = input(f"\"{program_name_input}\" 정말 이걸로 하시겠습니까? (y/n): ").strip().lower()
        if check_program_name == "y":
            cmd.append(f"--name {program_name_input}")
            break
        elif check_program_name == "n":
            continue
        else:
            print("잘못된 입력 값 입니다.")
            continue
    
    # 아이콘 추가 옵션
    while True:
        program_icon_input = input("if you need add icon? (y/n): ")
        
        if program_icon_input == "y":
            cmd.append(f"--icon {input("icon path: ")}")
            break
        elif program_icon_input == "n":
            pass
        else:
            print("잘못된 입력 값 입니다.")
            continue
    
    # 명령어 실행
    subprocess.run(cmd)