import threading
from collections import defaultdict
import time

def search_in_file(file_path, keywords, result):
    """Пошук ключових слів у файлі та збереження результатів."""
    found = defaultdict(list)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    found[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    finally:
        result.update(found)

def threaded_search(file_paths, keywords):
    threads = []
    result = defaultdict(list)
    start_time = time.time()

    for file_path in file_paths:
        thread = threading.Thread(target=search_in_file, args=(file_path, keywords, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Threaded search took: {time.time() - start_time} seconds")
    return result
