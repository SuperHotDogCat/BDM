import re
import os
import subprocess
from datetime import datetime, timedelta
import json

def main():
    subprocess.call(["clear"], shell=True)
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
            if not previous_warning_check(cmd[0]):
                #まだアルコールが残っている
                subprocess.call(["open", "index.html"])
            if not alcohol_check(cmd[0]):
                subprocess.call(["open", "index.html"])
        else:
            subprocess.call(cmd, shell=True)
    except Exception as e:
        # 例外が発生したときにエラーメッセージを取得する
        error_message = str(e)
        print(error_message)

def alcohol_check(command: str):
    warning_data = read_json_file()
    add_json_file(warning_data, command)
    return False

def read_json_file() -> list[dict]:
    with open('logs.json', 'r') as file:
        json_data = file.read()
    try:
        warning_data = json.loads(json_data)
    except:
        warning_data = []
    return warning_data

def add_json_file(warning_data: list[dict], command: str) -> None:
    warning_data.append({"command": command, "time": str(datetime.now())})
    with open('logs.json', 'w') as file:
        json.dump(warning_data, file, indent=4)

def write_json_file(warning_data: list[dict]) -> None:
    with open('logs.json', 'w') as file:
        json.dump(warning_data, file, indent=4)

def previous_warning_check(command: str):
    warning_data = read_json_file()
    for warning in warning_data:
        previous_command = warning["command"]
        previous_time = datetime.fromisoformat(warning["time"])
        current_time = datetime.now()
        if previous_command == command and current_time - previous_time < timedelta(hours=8):
            #まだアルコールが残っていると判定するため, Falseを返すことに
            return False
        if previous_command == command and current_time - previous_time >= timedelta(hours=8):
            #コマンドを実行しても良い
            warning_data.remove(warning) #8時間過ぎたデータは削除
            write_json_file(warning_data)
    return True

if __name__ == "__main__":
    main()