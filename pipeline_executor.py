import yaml
import pandas as pd
import json
import importlib.util

def load_module_from_path(name, path):
    try:
        # モジュール仕様の取得
        spec = importlib.util.spec_from_file_location(name, path)

        # 仕様がNoneの場合、モジュールのロードに失敗している
        if spec is None:
            print(f"Cannot load module from {path}")
            return None

        # モジュールの作成とロード
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module

    except FileNotFoundError:
        print(f"File not found: {path}")
    except SyntaxError as e:
        print(f"Syntax error in {path}: {e}")
    except Exception as e:
        print(f"Error loading module from {path}: {e}")

    return None


def execute_pipeline(yaml_file):
    with open(yaml_file, 'r') as file:
        pipeline = yaml.safe_load(file)

    for step in pipeline['steps']:
        if step['type'] == 'download':
            merge_module = load_module_from_path("download", "file_downloader.py")
            merge_module.download(step['download_config'], step['download_dir'])
    
        elif step['type'] == 'merge':
            merge_module = load_module_from_path("merge", "datanorm.py")
            merge_module.merge(step['input_files'], step['transform_config'], step['output_file'])
       
        

if __name__ == "__main__":
    execute_pipeline('pipeline.yaml')

