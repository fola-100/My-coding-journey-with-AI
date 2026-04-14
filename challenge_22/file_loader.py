import os

def success(data):
    return {"result": True,
            "error": None,
            "data": data}

def error(error_message):
    return {"result": False,
            "error": error_message,
            "data": None}

def get_all_file(folder_path):
    try:
        files=os.listdir(folder_path)
        text_file=[ file for file in files
                   if file.endswith(".txt")]
        return success(text_file)
    except FileNotFoundError:
        return error("folder not found")

def get_text(file_path):
    try:
        with open(file_path,"r") as f:
            file=f.read()
            return success(file)
    except FileNotFoundError:
        return error("file not found")

#if __name__=="__main__":












