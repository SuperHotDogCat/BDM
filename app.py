import re
import os
import subprocess

def main():
    while True:
        try:
            current_directory = os.getcwd()
            bottom_directory = os.path.basename(current_directory)
            # 標準入力を受け取り空白で分割する
            cmd = input(f"{bottom_directory} % ")
            cmd = list(filter(lambda x: x != '', re.split(r'[ 　]+', cmd)))
            process_cmd(cmd)
        except EOFError:
            # Ctrl + D で終了
            break

def process_cmd(cmd: str):
    try:
        if cmd[0] == "sudo" or cmd[0] == "git":
            if not alcohol_check():
                subprocess.call(["open", "index.html"])
                print(1)
        else:
            subprocess.call(cmd)
    except Exception as e:
        # 例外が発生したときにエラーメッセージを取得する
        error_message = str(e)
        print(error_message)

def alcohol_check():
    return False

if __name__ == "__main__":
    main()