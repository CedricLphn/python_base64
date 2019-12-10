import string

################################################ params
b64 = [
    "000000", "000001", "000010", "000011", "000100", "000101", "000110",
    "000111", "001000", "001001", "001010", "001011", "001100", "001101",
    "001110", "001111", "010000", "010001", "010010", "010011", "010100",
    "010101", "010110", "010111", "011000", "011001", "011010", "011011",
    "011100", "011101", "011110", "011111", "100000", "100001", "100010",
    "100011", "100100", "100101", "100110", "100111", "101000", "101001",
    "101010", "101011", "101100", "101101", "101110", "101111", "110000",
    "110001", "110010", "110011", "110100", "110101", "110110", "110111",
    "111000", "111001", "111010", "111011", "111100", "111101", "111110",
    "111111"
]

def b64_table_index():
    """Create an index for b64 table
    :return: index from table b64
    """
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def generate_b64_dic():
    """Generate a b64 dictionnary
    :return: b64 table
    """
    dic = {}
    get_index = b64_table_index()

    for i in range(len(get_index)):
        dic[get_index[i]] = b64[i]

    return dic

################################################ 1
def from_string_to_list(str):
    """Convert string to list
    :arg: string
    :return: list
    """
    a = []
    for string in str[:]:
        a.append(string)
    return a


################################################ 2
def from_b64_index_to_decimal(i):
    """Convert b64 index to decimal
    :arg: index from b64 table
    :return: decimal ASCII
    """
    a = ord(i)
    return a


def convert_list_to_int(list):
    """Convert list to int
    :arg: list
    :return: modified list of Int
    """
    modified = []
    for item in list[:]:
        item = from_b64_index_to_decimal(item)
        modified.append(item)
    return modified


################################################ 3
def decimal_to_binary(d):
    """Convert decimal to binary
    :arg: decimal
    :return: binary 8 bits
    """
    a = bin(d).replace("0b", "")
    a = str(a)

    while len(a) < 8:
        a = "0" + a
    return a


def convert_list_to_binary(list):
    """Convert list to binary
    :arg: list
    :return: modified list of 8 bits
    """
    modified = []
    for item in list[:]:
        item = decimal_to_binary(int(item))
        modified.append(item)
    return modified

################################################ 4
def convert_list_to_string(list):
    """Convert list to string
    :arg: list
    :return: string
    """
    return "".join(list)


################################################ 5
def convert_string_binary_to_list(str):
    """Convert string binary to list
    :arg: string
    :return: list
    """
    l = len(str)
    r = []
    if l > 5:
        for n in range(0, l, 6):

            catch = str[n: n + 6:]

            if len(catch) < 6:

                while len(catch) < 6:
                    catch += "0"

                r.append(catch)

            else:
                r.append(catch)

    return r

################################################ 6-7
def convert_bits_to_int_to_char(list):
    """Convert bits to index[i] of b64 table
    :param list:
    :return: char from b64
    """
    b64_dict = generate_b64_dic()
    new_dict = []

    for i in range(len(list)):
        for key, val in b64_dict.items():
            if list[i] == val:
                new_dict.append(key)

    return new_dict

################################################ 8
def tricky(list):
    """Trick to add =
    :param list:
    :return: list completed by optional =
    """
    count = len(list) % 2

    if count > 0:
        for i in range(count):
            list.insert(len(list), "=")

    return list

################################################ 9
def res_list_to_string(list):
    """Final result list to string
    :param list:
    :return: string
    """
    return ''.join(list)

