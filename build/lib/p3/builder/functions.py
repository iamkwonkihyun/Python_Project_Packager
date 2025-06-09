import os
import sys
import subprocess
import importlib

def yes_or_no_func(question: str, default=True) -> bool:
    """yes or no 함수

    Args:
        question (str): 질문
        default (bool, optional): Y or N 둘 중 어떤것을 기본값으로 할 건지. 기본값은 Y.

    Returns:
        bool: yes는 True no는 False를 반환
    """
    default_val = "(Y/n)" if default else "(y/N)"
    while True:
        answer = input(f"{question} {default_val}: ").strip().lower()
        if answer == "":
            return default
        if answer in ("y", "n"):
            return answer == "y"
        print("잘못된 입력입니다. y 또는 n을 입력해주세요.")

def qna_func(question: str, choice: list[str] = None) -> str:
    """qna 함수

    Args:
        question (str): 질문
        choice (list[str], optional): 선택지. Defaults to None.

    Returns:
        bool | str: 선택지 중 대답이 포함되어 있으면 
    """
    while True:
        answer = input(f"{question}")
        
        # 빈 값을 받을 때 입력 다시받기
        if answer == "":
            print("잘못된 입력입니다. 다시 입력하여 주세요.")
            continue
        
        if choice is not None and answer in choice:
            return answer
        else:
            return answer

def clear_screen_func(step):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(step)

def require_module(package):
    while True:
        try:
            importlib.import_module(package)
            break
        except ImportError:
            print("필요한 모듈이 설치되지 않았습니다.\n필요한 모듈을 설치하겠습니다...")
            # sys.executable을 쓰는 것이 현재 파이썬 환경에 pip를 정확히 적용할 수 있음
            result = subprocess.run([sys.executable, "-m", "pip", "install", package])
            if result.returncode != 0:
                print("pipreqs 설치에 실패했습니다. 수동으로 설치해주세요.")
                sys.exit(1)