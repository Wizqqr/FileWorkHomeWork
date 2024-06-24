def copy_line(source_file, target_file, line_number):
    with open(source_file, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    if line_number < 1 or line_number > len(source_lines):
        print("Некорректный номер строки!")
        return
    line_to_copy = source_lines[line_number - 1]

    # Чтение содержимого целевого файла
    with open(target_file, 'r', encoding='utf-8') as f:
        target_lines = f.readlines()
    target_lines.append(line_to_copy)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.writelines(target_lines)

    print(f"Строка номер {line_number} успешно скопирована из {source_file} в {target_file}.")


source_file = 'source.txt'
target_file = 'target.txt'
line_number = int(input("Введите номер строки для копирования: "))

copy_line(source_file, target_file, line_number)
