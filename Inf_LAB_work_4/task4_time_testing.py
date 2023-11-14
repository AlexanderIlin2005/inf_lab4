import timeit
import yaml
import json
import re


print("Время выполнения 10000 конвертаций:")


code_to_test = open("base_task.py", "r").read()


print("Простой заменой символов(базовое задание):", timeit.timeit(code_to_test, number=10000))

code_to_test = """
def parse(string):
    return yaml.dump(json.loads(string), default_flow_style=False, allow_unicode=True, sort_keys=False)

if __name__ == "__main__":
    input_file = "in.json"
    output_file = "out_task1.yaml"

    string = open(input_file, "r").read()
    open(output_file, "w").write(parse(string))
"""
print("При помощи библиотек(доп. задание 1):", timeit.timeit(code_to_test, number=10000))

code_to_test = open("task2.py", "r").read()
import_delta = """
import re
from enum import Enum, auto
"""
print("При помощи регулярных выражений(доп. задание 2):",
      timeit.timeit(code_to_test, number=100) - timeit.timeit(import_delta, number=10000))

code_to_test = open("task3.py", "r").read()
print("При помощи формальной грамматики(доп. задание 3):", timeit.timeit(code_to_test, number=10000))
