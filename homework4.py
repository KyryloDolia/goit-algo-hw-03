from pathlib import Path

def total_salary(path: str) -> tuple:
    
    path = Path(path)
    if not path.exists():
        print("Файл за вказаним шляхом не знайдений")
        return None

    with open(path, 'r', encoding='utf-8') as fh:
        lines = [el.strip().split(',') for el in fh.readlines()]
        summ = sum([int(line[1]) for line in lines])
        avg = summ // len(lines)
        return (summ, avg)
