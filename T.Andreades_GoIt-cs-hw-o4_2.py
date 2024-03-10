from multiprocessing import Pool, Manager
import time

def process_file(file_path, keywords):
    """Пошук ключових слів у файлі."""
    found = defaultdict(list)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    found[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return found

def merge_results(results):
    """Об'єднання результатів пошуку з різних процесів."""
    final_result = defaultdict(list)
    for result in results:
        for keyword, files in result.items():
            final_result[keyword].extend(files)
    return final_result

def multiprocessing_search(file_paths, keywords):
    start_time = time.time()
    with Manager() as manager:
        with Pool() as pool:
            results = pool.starmap(process_file, [(file_path, keywords) for file_path in file_paths])
            final_result = merge_results(results)
    
    print(f"Multiprocessing search took: {time.time() - start_time} seconds")
    return final_result
