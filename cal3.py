a, b = 10, 5
operations = ['+', '-', '*', '/', '%', '//']
results = [eval(f"a {op} b") for op in operations]

for op, res in zip(operations, results):
    print(f"{op}: {res}")
