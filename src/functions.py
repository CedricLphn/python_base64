def b64_table_index():
    """
    Return : index from table b64
    """
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

## 1
def from_string_to_list(str):
    """
    Args : string
    Return : list
    """
    a = []
    for string in str[:]:
        a.append(string)
    return a

## 2
def from_b64_index_to_decimal(i):
    """
    Args : index from b64 table
    Return : decimal ASCII
    """
    a = ord(i)
    return a

def convert_list_to_int(list):
    """
    Args : list
    Return : modified list of Int
    """
    modified = []
    for item in list[:]:
        item = from_b64_index_to_decimal(item)
        modified.append(item)
    return modified


##3
def decimal_to_binary(d):
    """
    Args : decimal
    Return : binary 8 bits
    """
    a = bin(d).replace("0b", "")
    a = str(a)

    while len(a) < 8:
        a = "0" + a
    return a

def convert_list_to_binary(list):
    """
    Args : list
    Return : modified list of 8 bits
    """
    modified = []
    for item in list[:]:
        item = decimal_to_binary(int(item))
        modified.append(item)
    return modified

##4
def convert_list_to_string(list):
    """
    Args : list
    Return : string
    """
    strl = ""
    return (strl.join(list))

##5
def convert_string_binary_to_list(str):
    """
    Args : string
    Return : list
    """
    ## size of string
    l = len(str)
    ## empty list
    r = []
    ## if size of string superior to 5
    if l > 5:
        ## loop to catch by 6 chars
        ## add to list
        for n in range(0, l, 6):

            catch = str[n: n+6:]

            if len(catch) < 6:

                while len(catch) < 6:
                    catch += "0"

                r.append(catch)

            else:
                r.append(catch)

    return r
