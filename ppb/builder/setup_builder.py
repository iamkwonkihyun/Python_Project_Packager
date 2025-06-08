from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape
import os
from importlib.resources import files
from pathlib import Path
from ppb.builder.reqs_builder import reqs_builder

def setup_builder():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("## setup builder ##")
    
    # reqs 파일
    reqs_path = "requirements.txt"
    if not os.path.exists(reqs_path):
        reqs_list = reqs_builder()
    else:
        reqs_list = reqs_builder()
    
    # 프로그램 이름
    while True:
        program_name_input = input("program name: ")
        check_program_name = input(f"\"{program_name_input}\" 정말 이걸로 하시겠습니까? (y/n): ").strip().lower()
        if check_program_name == "y":
            break
        elif check_program_name == "n":
            continue
        else:
            print("잘못된 입력 값 입니다.")
            continue
    
    # 프로그램 버전
    while True:
        program_ver_input = input("program version: ")
        check_program_ver = input(f"\"{program_ver_input}\" 정말 이걸로 하시겠습니까? (y/n): ").strip().lower()
        if check_program_ver == "y":
            break
        elif check_program_ver == "n":
            continue
        else:
            print("잘못된 입력 값 입니다.")
            continue
    
    # cli 이름
    while True:
        cli_name_input = input("cli name: ")
        check_cli_name = input(f"\"{cli_name_input}\" 정말 이걸로 하시겠습니까? (y/n): ").strip().lower()
        if check_cli_name == "y":
            break
        elif check_cli_name == "n":
            continue
        else:
            print("잘못된 입력 값 입니다.")
            continue
    
    # 시작 지점
    while True:
        entry_point_input = input("entry point(ex. main.py에 main함수이면 main:main): ")
        check_entry_point = input(f"\"{entry_point_input}\" 맞으신가요? (y/n): ").strip().lower()
        if check_entry_point == "y":
            break
        elif check_entry_point == "n":
            continue
        else:
            print("잘못된 입력 값 입니다.")
            continue
    
    context = {
        "name": program_name_input,
        "version": program_ver_input,
        "requirements": reqs_list,
        "cli_name": cli_name_input,
        "entry_point": entry_point_input 
    }
    
    env = Environment(
    loader=PackageLoader('ppb', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('setup.py.j2')
    
    rendered = template.render(context)

    with open("setup.py", "w") as f:
        f.write(rendered)