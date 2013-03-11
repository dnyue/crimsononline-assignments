a = "~/Desktop/test.txt"

def common_words(path):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words.
    """
    ### returns word in order of most common to least common.
    f = open(os.path.expanduser(path))
    words = f.read()
    splitted = words.split()
    count = []
    for word in splitted:
        if len(count) == 0:
            count.append([word,1]) #takes care of initialization
        else:
            check = 0
            for x in count:
                if x[0] == word:
                    x[1] = x[1]+1
                    check = 1
                    break
            if check == 0:
                count.append([word,1]) #if word is in the list, add to the count. otherwise, add an entry to the list.
    sorted_count = sorted(count, key=lambda word: word[1], reverse=True)
    sort_list = [x[0] for x in sorted_count]
    return sort_list

def common_words_min(path, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    f = open(os.path.expanduser(path))
    words = f.read()
    splitted = words.split()
    count = []
    for word in splitted:
        if len(word)>=min_chars:
            if len(count) == 0:
                count.append([word,1]) #takes care of initialization
            else:
                check = 0
                for x in count:
                    if x[0] == word:
                        x[1] = x[1]+1
                        check = 1
                        break
                if check == 0:
                    count.append([word,1]) #if word is in the list, add to the count. otherwise, add an entry to the list.
    sorted_count = sorted(count, key=lambda word: word[1], reverse=True)
    sort_list = [x[0] for x in sorted_count]
    return sort_list
  

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    f = open(os.path.expanduser(path))
    words = f.read()
    splitted = words.split()
    count = []
    for word in splitted:
        if len(word)>=min_chars:
            if len(count) == 0:
                count.append([word,1]) #takes care of initialization
            else:
                check = 0
                for x in count:
                    if x[0] == word:
                        x[1] = x[1]+1
                        check = 1
                        break
                if check == 0:
                    count.append([word,1]) #if word is in the list, add to the count. otherwise, add an entry to the list.
    sorted_count = sorted(count, key=lambda word: word[1], reverse=True)
    tuple_sorted_count = [tuple(x) for x in sorted_count]
    return tuple_sorted_count

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        f = open(os.path.expanduser(path))
    except IOError:
        print 'cannot open' path
        return None
    words = f.read()
    splitted = words.split()
    count = []
    for word in splitted:
        if len(word)>=min_chars:
            if len(count) == 0:
                count.append([word,1]) #takes care of initialization
            else:
                check = 0
                for x in count:
                    if x[0] == word:
                        x[1] = x[1]+1
                        check = 1
                        break
                if check == 0:
                    count.append([word,1]) #if word is in the list, add to the count. otherwise, add an entry to the list.
    sorted_count = sorted(count, key=lambda word: word[1], reverse=True)
    tuple_sorted_count = [tuple(x) for x in sorted_count]
    return tuple_sorted_count

