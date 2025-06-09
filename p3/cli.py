from p3.builder.setup_builder import setup_builder
from p3.builder.exe_builder import exe_builder
from p3.builder.reqs_builder import reqs_builder
from p3.builder.functions import yes_or_no_func

def main():
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