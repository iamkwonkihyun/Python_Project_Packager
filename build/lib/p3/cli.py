from p3.builder.reqs_builder import reqs_builder
from p3.builder.setup_builder import setup_builder
from p3.builder.exe_builder import exe_builder
from p3.builder.functions import yes_or_no_func, clear_screen_func, require_module

def main():
    # 화면 clear 및 환영인사
    clear_screen_func("[~] Welcome to P3!! [~]")
    
    # 필요 라이브러리/모듈 확인
    require_module("pipreqs")
    require_module("jinja2")
    require_module("PyInstaller")
    
    # 필요한 것만 입력
    reqs_input = yes_or_no_func("Do you need requirements.txt?")
    setup_input = yes_or_no_func("Do you need add to setup.py?")
    exe_input = yes_or_no_func("Do you need convert to exe?")
    
    actions = [
    (reqs_input, reqs_builder),
    (setup_input, setup_builder),
    (exe_input, exe_builder),
    ]

    for flag, func in actions:
        if flag:
            func()