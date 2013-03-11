def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    end_quote = 0
    while True:
        tag_link = page.find('"<a href="',end_quote)
        if tag_link == -1:
            break
        start_link = page.find('">',tag_link)
        start_quote = page.find('"',start_link)
        end_quote = page.find('"',start_quote + 1)


def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    pass

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote+1:end_quote]
    return url, end_quote
