import os


def gen_files_path(path: str, find_path: str):
    for i_elem in os.listdir(path):
        try:
            next_path = os.path.join(path, i_elem)
            if i_elem == find_path:
                for i in os.listdir(next_path):
                    yield f'{os.path.join(next_path, i)}'
            if os.path.isdir(next_path):
                for i in os.listdir(next_path):
                    new_path = os.path.join(next_path, i)
                    if i == find_path:
                        for i_path in os.listdir(new_path):
                            yield f'{os.path.join(new_path, i_path)}'
                    gen_files_path(new_path, find_path)
        except PermissionError:
            continue


start_path = os.path.abspath(os.path.join('/'))
my_path = 'Practice'
found_path = gen_files_path(path=start_path, find_path=my_path)
for found_path in found_path:
    print(found_path)