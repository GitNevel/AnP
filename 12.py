import re
from collections import Counter



def get_declension(count):
    """Возвращает правильное склонение слова 'запрос' в зависимости от числа."""
    n = count % 100
    n1 = count % 10
    if 11 <= n <= 19:
        return "запросов"
    if n1 == 1:
        return "запрос"
    if 2 <= n1 <= 4:
        return "запроса"
    return "запросов"


def format_size(size_in_bytes):
    """Форматирует размер в байтах в читаемый вид (KB, MB, GB)."""
    for unit in['Байт', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:g} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} PB"


log_pattern = re.compile(
        r'^(?P<ip>\S+)\s+--\s+\[(?P<datetime>.*?)\]\s+"(?P<method>\S+)\s+(?P<path>\S+)\s+(?P<protocol>.*?)"\s+(?P<status>\d+)\s+(?P<size>\d+|-)\s+(?P<agent>.*)$'
    )
total_requests = 0
total_size = 0

ip_counter = Counter()
status_counter = Counter()
path_counter = Counter()

with open('logs.txt') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        match = log_pattern.search(line)
        if match:
            total_requests += 1
            ip = match.group('ip')
            status = match.group('status')
            path = match.group('path')
            size = match.group('size')

            ip_counter[ip] += 1
            status_counter[status] += 1
            path_counter[path] += 1

            if size != '-':
                total_size += int(size)


print("Топ-5 IP-адресов:")
for ip, count in ip_counter.most_common(5):
    percent = (count / total_requests) * 100
    print(f"{ip} - {count} {get_declension(count)} ({percent:.1f}%)")

print("Статус-коды:")
for status, count in status_counter.most_common():
    percent = (count / total_requests) * 100
    print(f"{status} - {count} {get_declension(count)} ({percent:.1f}%)")

print("Самые популярные пути:")
for path, count in path_counter.most_common(3):
    print(f"{path} - {count} {get_declension(count)}")

print("Общий размер ответа из всех запросов:")
print(f"{total_size} байт (что составляет примерно {format_size(total_size)})")