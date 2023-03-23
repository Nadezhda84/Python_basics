"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for ping in ARGS:
    ping_process = subprocess.Popen(ping, stdout=subprocess.PIPE)
    print(ping_process.stdout)
    for line in ping_process.stdout:
        res = chardet.detect(line)
        print(line.decode(res['encoding']))
