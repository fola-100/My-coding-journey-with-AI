import string

def success(data):
    return{"result":True,
           "error":None,
           "data":data}
def error(error_message):
    return{"result":False,
           "error":error_message,
           "data":None}

def count_words(text):
    word_count = len(text.split())
    return success(word_count)

def total_lines(text):
    each_lines=len(text.splitlines())
    return success(each_lines)

def common_word(text):
    word_found={}
    most_common=[]
    clean_text=text.translate(str.maketrans("","",string.punctuation))
    words=clean_text.lower().split()

    for each_word in words:
       word_found[each_word]=word_found.get(each_word,0)+1
    if not word_found:
        return error("No words found")
    max_count = max(word_found.values())
    for word,count in word_found.items():
        if count==max_count:
           most_common.append(word)
    result={"words":most_common, "count":max_count}
    return success(result)

def text_summary(text):
    result = count_words(text)
    if not result["result"]:
        return result
    total_words=result["data"]

    result=total_lines(text)
    if not result["result"]:
        return result
    total_text_line=result["data"]

    result=common_word(text)
    if not result["result"]:
      return result
    most_common_word=result["data"]

    summary_result={"total_words":total_words,
                    "total_lines":total_text_line,
                    "common_word":most_common_word}
    return success(summary_result)

def top_three_common_words(text):
    word_found = {}
    most_common = {}
    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clean_text.lower().split()

    for each_word in words:
        word_found[each_word] = word_found.get(each_word, 0) + 1
    if not word_found:
        return error("No words found")

    each_word_total = word_found.values()
    highest_values=sorted(each_word_total, reverse=True)[:3]
    for word,number in  word_found.items():
        if number in highest_values:
            most_common[word]=number
    return success(most_common)

if __name__=="__main__":
   book=""
   print(top_three_common_words(book))
