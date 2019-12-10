import argparse

from src.functions import *


def main():
    """Main module

    checks the arguments passed by the user and adds as an exclusion rule 
    the simultaneous use of encoding and decoding arguments 
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--decode", action="store_true")
    group.add_argument("-e", "--encode", action="store_true")
    parser.add_argument("-s")
    args = parser.parse_args()
    if(args.decode):
        print("Decoding", args.s)
    elif(args.encode):
        print("Encoding", args.s)
    else:
        print("Nothing to do.")

    input_test = "coucou"
    run = res_list_to_string(
                tricky(
                    convert_bits_to_int_to_char(
                        convert_string_binary_to_list(
                            convert_list_to_string(
                                convert_list_to_binary(
                                    convert_list_to_int(
                                        from_string_to_list(input_test)
                                    )))))))
    print(run)

if __name__ == '__main__':
    main()