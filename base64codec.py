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
    parser.add_argument("-file")
    parser.add_argument("-out")
    args = parser.parse_args()

    if(args.decode):
        if(args.file):
            print("Reading", args.file)
            file = open(args.file, "r")
            print("Result: ", decode(file.readline()))
        else:
            print("Result: ", decode(args.s))
        if(args.out):
            file = open(args.out, "w+")
            if(args.s):
                file.write(decode(args.s))
            if(args.file):
                encoded_file = open(args.file, "r")
                file.write(decode(encoded_file.readline()))
            print("Successfull write to", args.out)
    elif(args.encode):
        if(args.file):
            file = open(args.file, "r")
            string = file.readline()
        else:
            string = args.s
        
        run = res_list_to_string(
            tricky(
                convert_bits_to_int_to_char(
                    convert_string_binary_to_list(
                        convert_list_to_string(
                            convert_list_to_binary(
                                convert_list_to_int(
                                    from_string_to_list(string))
                                ))))))
        if(args.out):
            file = open(args.out, "w+")
            file.write(run)
            print("Successfull write in", args.out)
        else:
            print("Result: ", run)


    else:
        print("Nothing to do.")



if __name__ == '__main__':
    main()