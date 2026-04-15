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

def text_summary(text,number):
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

    result=top_n_common_words(text,number)
    if not result["result"]:
        return result
    top_three_words=result["data"]

    summary_result={"total_words":total_words,
                    "total_lines":total_text_line,
                    "common_word":most_common_word,
                    "top_3_words":top_three_words}
    return success(summary_result)

def top_n_common_words(text,n):
    if not isinstance(n, int):
        return error("n must be a whole number")

    if n<=0:
        return error(f'n must be greater than 0')

    stop_words = {"the", "is", "and", "in", "of"}

    word_found = {}

    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clean_text.lower().split()

    for each_word in words:
        if each_word not in stop_words:
          word_found[each_word] = word_found.get(each_word, 0) + 1

    if not word_found:
        return success([])

    sorted_words=sorted(word_found.items(),key=lambda x:x[1],reverse=True)

    top_n=sorted_words[:n]

    return success(top_n)

if __name__=="__main__":
   book=""
   print(top_n_common_words(book,50))
