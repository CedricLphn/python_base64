dictionnaire = {'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011', 'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111', 'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011', 'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111', 'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011', 'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111', 'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011', 'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111', 'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011', 'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111', 'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011', 's': '101100', 't': '101101', 'u': '101110', 'v': '101111', 'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011', '0': '110100', '1': '110101', '2': '110110', '3': '110111', '4': '111000', '5': '111001', '6': '111010', '7': '111011', '8': '111100', '9': '111101', '+': '111110', '/': '111111'}

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

def decode(string_to_decode):
    """Decode to Base 64

    Args:
        string_to_decode: String to decode
    Returns: 
        Text decoded string
    """

    final = ""

    def str_to_b64_decimal(s):
        """String to binary base 64

        Args:
            str : String to decode

        Returns:
            Binary base 64 array
        """

        list = []

        for char in s.strip('='):
            list.append(dictionnaire[char])
            
        return list


    def convert_6b_to_8b(bits): 
        """Convert array of 6 bit to 8 bits

        Args:
            bits : array of bits

        Return:
            List of 8 bits

        """
        result = []
        string = ''.join(bits)
        list_range = range(0, len(string)-1)
        old_cut = 0
        for i in list_range:
            if i % 8 == 0 and i != 0:
                result.append(string[old_cut:i])
                old_cut = i
        return result
            
    listing = convert_6b_to_8b(str_to_b64_decimal(string_to_decode))

    for decimal in listing:
        final += chr(int(decimal, 2))

    return final
