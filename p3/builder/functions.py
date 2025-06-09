def yes_or_no_func(question, default=True):
    default_val = "(Y/n)" if default else "(y/N)"
    while True:
        answer = input(f"{question} {default_val}: ").strip().lower()
        if answer == "":
            return default
        if answer in ("y", "n"):
            return answer == "y"
        print("잘못된 입력입니다. y 또는 n을 입력해주세요.")

def qna_func(question, choice: list[str] = None):
    while True:
        answer = input(f"{question}")
        if answer == "":
            print("잘못된 입력입니다. 다시 입력하여 주세요.")
        if choice is not None and answer in choice:
            return answer
        return answer