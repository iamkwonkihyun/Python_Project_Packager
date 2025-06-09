import os
from jinja2 import Environment, PackageLoader, select_autoescape
from p3.builder.reqs_builder import reqs_builder
from p3.builder.functions import qna_func, yes_or_no_func

def setup_builder():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("## setup builder ##")
    
    # reqs 파일
    reqs_path = "requirements.txt"
    if not os.path.exists(reqs_path):
        reqs_list = reqs_builder()
    else:
        reqs_list = reqs_builder()
    
    check = False
    
    while not check:
        program_name = qna_func("program name: ")
        program_ver = qna_func("program version: ")
        cli_name = qna_func("cli name: ")
        entry_point = qna_func("entry point: ")
    
        context = {
            "name": program_name,
            "version": program_ver,
            "requirements": reqs_list,
            "cli_name": cli_name,
            "entry_point": entry_point
        }
        
        for key, value in context.items():
            print(f"{key}: {value}")
        
        check = yes_or_no_func("다시 한번 확인해주세요. 이걸로 결정하시겠습니까?: ")
    
    env = Environment(
    loader=PackageLoader('p3', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('setup.py.j2')
    
    rendered = template.render(context)

    with open("setup.py", "w") as f:
        f.write(rendered)