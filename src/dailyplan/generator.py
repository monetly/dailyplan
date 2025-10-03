import json
import yaml
from datetime import datetime, timedelta

TEMPLATE = """BEGIN:VEVENT
DTSTART;TZID=Asia/Shanghai:{start}
DTEND;TZID=Asia/Shanghai:{end}
SUMMARY:{title}
DESCRIPTION:{desc}
END:VEVENT
"""

VCALENDAR_HEADER = """BEGIN:VCALENDAR
PRODID:-//Daily Plan Generator//ZH
VERSION:2.0
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
BEGIN:STANDARD
DTSTART:19700101T000000
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
END:STANDARD
END:VTIMEZONE
"""

VCALENDAR_FOOTER = "END:VCALENDAR\n"


def load_tasks(path):
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    elif path.endswith(".yaml") or path.endswith(".yml"):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    else:
        raise ValueError("仅支持 JSON 或 YAML 文件")
    return [(t["title"], t["desc"]) for t in data["tasks"]]


def generate_events(start_date, tasks, start_hour, duration):
    events = []
    date = datetime.strptime(start_date, "%Y%m%d")

    for i, (title, desc) in enumerate(tasks):
        day = date + timedelta(days=i)
        start_dt = day.replace(hour=start_hour, minute=0, second=0)
        end_dt = start_dt + timedelta(hours=duration)
        start_str = start_dt.strftime("%Y%m%dT%H%M%S")
        end_str = end_dt.strftime("%Y%m%dT%H%M%S")

        events.append(
            TEMPLATE.format(start=start_str, end=end_str, title=title, desc=desc)
        )
    return "".join(events)


def generate_ical(start_date, taskfile, start_hour, duration, outfile):
    tasks = load_tasks(taskfile)
    events = generate_events(start_date, tasks, start_hour, duration)
    ical = VCALENDAR_HEADER + events + VCALENDAR_FOOTER

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(ical)
    return outfile
