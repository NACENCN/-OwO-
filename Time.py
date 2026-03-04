import os
import sys
import time

def get_minutes():
    """从环境变量或命令行参数获取分钟数，默认25分钟"""
    # 优先级：1. 命令行参数 2. 环境变量 3. 默认值
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            print("参数错误，使用默认值25分钟")
            return 25
    env_min = os.environ.get("FOCUS_MINUTES")
    if env_min is not None:
        try:
            return int(env_min)
        except ValueError:
            print("环境变量 FOCUS_MINUTES 格式错误，使用默认值25分钟")
            return 25
    return 25  # 默认25分钟

def main():
    minutes = get_minutes()
    seconds = minutes * 60

    # 判断是否在交互式终端中，以决定是否使用 \r 刷新同一行
    is_interactive = sys.stdout.isatty()

    print(f"专注计时器启动，时长：{minutes} 分钟")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        if is_interactive:
            # 交互式终端：刷新同一行
            print(timer, end='\r')
        else:
            # 非交互式环境（如CI）：每行打印一条记录
            print(timer)
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!" if is_interactive else "Time's up!")

if __name__ == "__main__":
    main()
sadas
s
s
s
s
s

s
ss
s
s
s
