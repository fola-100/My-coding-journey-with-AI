import file_loader
import text_analyzer
def main():
    # COLLECT TEXT
    return_value=path()
    if not return_value["result"]:
        print(return_value["error"])
        return None
    text = return_value["data"]
    result = text_analyzer.count_content(text)
    print( result)
    result = text_analyzer.total_lines(text)
    print(result)
    while True:
        option=menu()
        if "exist"== option:
            print("Exist program")
            return None

        elif "number of word"==option:
             result = text_analyzer.count_content(text)
             # RETURN TOTAL NUMBER OF WORDS
             if result["result"]:
                print(result["data"])

        elif "number of lines" == option:
            result = text_analyzer.total_lines(text)
            if result["result"]:
                print(result["data"])

        elif "check most common word" == option:
             result = text_analyzer.common_word(text)
             print(result)

             if result["result"]:
                print(result["data"])


def menu():
    print("___menu_option___")
    print("1)Number of words")
    print("2)Number of lines")
    print("3)Check most common word")
    print("4)exist")
    choice = input(">:")
    while choice not in ["1", "2", "3", "4"]:
        print("option not available")
        choice = input(">:")
    if choice == "1":
        return "number of word"
    elif choice == "2":
        return "number of lines"
    elif choice == "3":
        return  "number of lines"
    else:
        return "exist"



def get_file_path():
    """ USER HAS TWO CHOICE HARDCODE FILE PATH OR ENTER INPUT IT"""
    file_path=None
    if file_path is None:
       while True:
            file_path=input("Enter in file path:")
            if file_path:
               return {"result":True,
                        "error":None,
                        "data":file_path}
            else:
                  print("No folder name entered")

    return file_path

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
            folder_name = folder_path()
            if folder_name["result"]:
              name = folder_name["data"]
              # GETTING  IN FOLDER
              result = file_loader.get_all_file(name)
              if not result["result"]:
                return {"result": False,
                        "error": result["error"],
                        "data": None}

              files = result["data"]
              print("List of folder found")
              for each_file in files:
                 print(each_file)
                # FILE USER LOOKING FOR
              file_name = input("Enter in file name searching for:")
              while True:
                  if file_name and file_name in files:
                      full_path=f'{name}/{file_name}'
                      result = file_loader.get_text(full_path)

                      if result["result"]:
                          return {"result": True,
                                  "error": None,
                                  "data": result["data"]}

                      else:
                          return {"result": False,
                                  "error": result["error"],
                                  "data": None}

                  else:
                    print("File name not seen")
                    file_name = input("Enter in file name searching for:")

        elif options == "2":
            file_path = get_file_path()
            if file_path["result"]:
               name=file_path["data"]
               result = file_loader.get_text(name)

               if result["result"]:
                  return {"result": True,
                        "error": None,
                        "data": result["data"]}
               else:
                  return {"result": False,
                        "error": result["error"],
                        "data": None}

if __name__=="__main__":
    main()






