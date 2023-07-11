text_path = r'C:\pyhton\def.txt'


def split_path(text_path: str) -> tuple():
    list_text_path = text_path.split('\\')
    list_last_elem = list_text_path[-1].split('.')
    path = '\\'.join(list_text_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[1]
    return path, name, expansion


print(split_path(text_path))