import random
import re
eng_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z']

eng_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
'W', 'X', 'Y', 'Z']

def randomLinkCode():
    """
    It creates a list of 5 elements, the first element is a random integer between 0 and 9, the second
    element is a random lowercase letter, the third element is a random integer between 0 and 99, the
    fourth element is a random uppercase letter, and the fifth element is a random lowercase letter. 
    
    The function then returns the list as a string
    :return: A string of 5 characters.
    """
    link_key = []
    link_key.append(f'{random.randint(0,9)}')
    link_key.append(random.choice(eng_small))
    link_key.append(f'{random.randint(0,99)}')
    link_key.append(random.choice(eng_big))
    link_key.append(random.choice(eng_small))
    
    return ''.join(link_key)

# -------------------------------------------------------------
valid_url_pattern0 = "((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"
valid_url_pattern1 = "(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"
valid_url_pattern2 = "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"

def isURLValid(url : str) :
    if re.search(re.compile(valid_url_pattern0), url) or re.search(re.compile(valid_url_pattern1), url) or re.search(re.compile(valid_url_pattern2), url):
        return True
    return False

def crunchCustomHandle(custom_handle : str):
    temp_list = custom_handle.split(' ')
    strr = ''
    for i in temp_list:
        strr += i
    return strr
if __name__ == "__main__" :
    # print(isURLValid('https://www.geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/#:~:text=Match%20the%20given%20URL%20with,regular%20expression%2C%20else%20return%20false.'))
    # print(crunchCustomHandle('my love'))
    pass