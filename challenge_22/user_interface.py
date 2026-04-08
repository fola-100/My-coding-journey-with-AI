import file_loader
import text_analyzer

def main():
    # COLLECT TEXT
    return_value=path()
    if return_value=="search for file in folder":
        folder_name = folder_path()
        if folder_name["result"]:
            name = folder_name["data"]
            # GETTING  IN FOLDER
            result = file_loader.get_all_file(name)
            if not result["result"]:
                print(result["error"])
                return None
            # GIVE SUMMARY OF FILE FOUND IN FOLDER
            files = result["data"]
            if not files:
                print("No text file found in folder")
                return None
            for each_file in files:
                full_path = f'{name}/{each_file}'
                result = file_loader.get_text(full_path)
                if result["result"]:
                    text_file = result["data"]
                    analysis=text_analyzer.text_summary(text_file)
                    print(analysis["data"])
                else:
                    print(result["error"])
                    return None

    elif  return_value=="enter in file path":
        file_path = get_file_path()
        if file_path["result"]:
            name = file_path["data"]
            result = file_loader.get_text(name)
            if result["result"]:
                text_file = result["data"]
                analysis=text_analyzer.text_summary(text_file)
                print(analysis["data"])

            else:
                print(result["error"])
                return None

    return None


def get_file_path():
    """ USER HAS TWO CHOICE HARDCODE FILE PATH OR ENTER INPUT IT"""
    file_path =None
    if file_path is None:
       while True:
            file_path=input("Enter in file path:")
            if file_path:
               return {"result":True,
                        "error":None,
                        "data":file_path}
            else:
                  print("No folder name entered")

    return {"result":True,
            "error":None,
            'data':file_path}

def folder_path():
    while True:
         folder_location = input("Enter in folder path:")
         if folder_location:
             return {"result": True,
                     "error": None,
                     "data":folder_location }
         else:
             print("No folder name entered")



def path():
    while True:
        print("1)Search for file in folder")
        print("2)Enter in file path")
        options = input("Enter in option:")
        while options not in ["1","2"]:
            print("Option not available ")
            options = input("Enter in option:")
        if options == "1":
          return "search for file in folder"
        else:
            return "enter in file path"

if __name__=="__main__":
    main()






