import os

def makedir_and_cd_dir(dirPath="./example"):
    os.makedirs(dirPath, exist_ok=True)
    os.chdir(dirPath)

def find_files_prefix_and_subfix(dirPath, prefix="", subfix=""):
    result = []

    with os.scandir(dirPath) as files:
        for file in files:
            if file.is_file() and file.name.startswith(prefix) and file.name.endswith(subfix):
                result.append(file.name)

    return result



if __name__ == "__main__":
    # print(find_files_prefix_and_subfix("/Users/yqiaoliang/Desktop/main_hub/pythonFiles"))
    pass