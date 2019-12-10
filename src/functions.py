def b64_table_index():
    """
    Return : index from table b64
    """
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def from_string_to_list(str):
    """
    Args : string
    Return : list
    """
    a = []
    for string in str[:]:
        a.append(string)
    return a


def from_b64_index_to_decimal(i):
    """
    Args : index from b64 table
    Return : decimal ASCII
    """
    a = ord(i)
    return a


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
