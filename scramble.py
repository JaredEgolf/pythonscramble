# Accepts as input a string and returns a scrambled version
# of the individual words in the string.
# The input string is a list of words separated by spaces.
# The output string is a list of individually scrambled 
# words separated by spaces.
#
# The scrambling algorithm is as follows:
# 1. Split the input string into a list of words.
# 2. For each word in the list longer than three characters,
#  rearrange the internal characters of the word.
# 3. Return the list of scrambled words in the same order.
#
# The input string can be accepted on the command line or
# provided as an input file.
#
# The output string is printed to the terminal by default
#
# The -h option prints the help message.
# The -v option prints the version number.
# The -d option prints the debug messages.
# The -t option prints the time taken to execute the program.
# The -s option prints the size of the input string.
# The -l option prints the length of the longest word in the string.
# The -w option prints the number of words in the string.
# The -e option allows a list of exceptions to be provided
# that will not be scrambled.
# The -o option allows the output to be saved to a file.
# The output file is overwritten if it already exists.
# The output file is created if it does not exist
#  with the name "scramble.txt".
#

# Parse input arguments
import argparse
parser = argparse.ArgumentParser(description='Scramble a string of words.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
parser.add_argument('-d', '--debug', action='store_true', help='print debug messages')
parser.add_argument('-t', '--time', action='store_true', help='print time taken to execute')
parser.add_argument('-s', '--size', action='store_true', help='print size of input string')
parser.add_argument('-l', '--longest', action='store_true', help='print length of longest word')
parser.add_argument('-w', '--words', action='store_true', help='print number of words in string')
parser.add_argument('-e', '--exceptions', action='store_true', help='print exceptions')
parser.add_argument('-o', '--output', action='store_true', help='save output to file')
parser.add_argument('string', nargs='?', help='string to scramble')
args = parser.parse_args()

# Print debug messages
if args.debug:
    print("Debug messages enabled")
    print("Input string: " + args.string)
    print("Other active arguments:" + str(args.exceptions) + str(args.output))

# Print time taken to execute
if args.time:
    import time
    start = time.time()

# Print size of input string
if args.size:
    print("Size of input string: " + str(len(args.string)))

# Print length of longest word
if args.longest:
    print("Length of longest word: " + str(max(len(word) for word in args.string.split())))

# Print number of words in string
if args.words:
    print("Number of words in string: " + str(len(args.string.split())))

# Print exceptions
if args.exceptions:
    print("Exceptions: " + str(args.string.split()))

# Print output to file
if args.output:
    print("Output to file: " + str(args.string.split()))

# Scramble string
import random
def scramble(string):
    # Split string into list of words
    words = string.split()
    # For each word in the list longer than three characters,
    # rearrange the internal characters of the word.
    for word in words:
        if len(word) > 3:
            # Shuffle all characters except the first and the last in the word
            random.shuffle(word[1:-1])
            # If the shuffled word is the same as the original word, then repeat
            # the process until a different shuffle is found.
            while word == word[1:-1]:
                random.shuffle(word[1:-1])
                # If debug is enabled then ouput the shuffled word
                if args.debug:
                    print("Shuffled word: " + word)
            # Print the scrambled word
            print(word)
    return

# Scramble string
scramble(args.string)

# Print time taken to execute
if args.time:
    print("Time taken to execute: " + str(time.time() - start))
