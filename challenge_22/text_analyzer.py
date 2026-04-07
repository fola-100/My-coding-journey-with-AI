def success(data):
    return{"result":True,
           "error":None,
           "data":data}
def error(error_message):
    return{"result":False,
           "error":error_message,
           "data":None}

def count_content(note):
    note=str(note)
    total_text_numb=0
    char = note.split()
    for each_word in char:
        total_text_numb+= len([each_word])
    return success(total_text_numb)

def total_lines(text):
    text=str(text)
    each_lines=len(text.splitlines())

   # total_count=each_lines+1
    return success(each_lines)

def common_word(text):
    word_found={}
    most_common=[]
    clean_text=text.replace("!","").replace(",","").replace("?","").replace(".","")
    words=clean_text.split()

    for each_word in words:
        if each_word not in word_found:
            word_found[each_word]=1
        else:
           word_found[each_word]+=1

    max_count = max(word_found.values())
    for word in word_found:
        if word_found[word]==max_count:
           most_common.append(word)
    result=most_common, max_count
    return success(result)

def text_summary(text):
    result=count_content(text)

    total_words=result["data"]

    result=total_lines(text)
    total_text_line=result["data"]

    result=common_word(text)
    most_common_word=result["data"]

    summary_result={"total_word":total_words,
                    "total_lines":total_text_line,
                    "common_word":most_common_word}
    return summary_result

if __name__=="__main__":
   book=""
   print(text_summary(book))
