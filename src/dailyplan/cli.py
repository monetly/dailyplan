import argparse
import os
from .generator import generate_ical

def main():
    parser = argparse.ArgumentParser(description="生成每日任务 iCalendar 文件")
    parser.add_argument("--start", required=True, help="起始日期 (格式: YYYYMMDD)")
    parser.add_argument("--tasks", default=os.path.join(os.path.dirname(__file__), "config", "tasks.yaml"),
                        help="任务文件 (默认: config/tasks.yaml)")
    parser.add_argument("--outfile", default="plan.ics", help="输出文件名")
    parser.add_argument("--hour", type=int, default=8, help="每天开始的小时 (24小时制, 默认 8 点)")
    parser.add_argument("--duration", type=int, default=3, help="任务持续小时数 (默认 3 小时)")
    args = parser.parse_args()

    path = generate_ical(args.start, args.tasks, args.hour, args.duration, args.outfile)
    print(f"✅ 已生成 {path}")
