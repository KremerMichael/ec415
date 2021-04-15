import sys
import os
import time
import random
import struct

import argparse

parser = argparse.ArgumentParser(description='Generate the messages for EC415 Lab5.')
parser.add_argument('filepath',
                    help='File path to decode.')
# parser.add_argument('grc_file', help='GRC file path that the program will compile and run.')
args = parser.parse_args()
filepath = args.filepath

print("File path = \"" + filepath + "\"")

# Given a filepath, returns the binary content of the file
def get_binary_file_data(filepath):
	try:
		f = open(args.filepath, 'rb')
		bits = f.read()
		f.close()
	except IOError as e:
		print("Couldn't open or read file (%s)." % e)

	# convert bytes into bits
	bin_str = ''.join(format(x, 'b').zfill(8) for x in bits)
	return bin_str

# Use this if you want to print the preamble in hex format
def bytes_to_hex(byte_str):
	hex_str = ""
	for c in byte_str:
		hex_str += hex(ord(c))[2:] + " "
	return hex_str

# Given a binary string, a start index, and number of bytes to read, returns a set of bytes/chars.
def get_bytes(bin_str, start, num_bytes):
	if not start+8*num_bytes < len(bin_str):
		print("Not enough bytes to consume.")
		exit(0)
	msg = ""
	for i in range(start, start+8*num_bytes, 8):
		msg += chr(int(bin_str[i:i+8], 2))
	return start+8*num_bytes, msg

# Searches a binary string for a preamble and returns the index where it is located
# Returns -1 if no preamble found
def search_for_preamble(bin_str, preamble, start):
	if not preamble or not isinstance(preamble, str):
		print("No valid preamble given. Enter the preamble as a string with the hex digits you want to search for.")
		exit(1)
	preamble = bin(int(preamble,16))[2:]
	idx = bin_str[start:].find(preamble)
	if idx == -1:
		return len(bin_str), False
	return idx+start, True

# Use this to decode the hex encoded message into ASCII. Faulty characters are replaced with a '*'.
def decode_hex(s):
    msg = ''
    for i in range(0, len(s), 2):
        try:
            msg += ''.join(chr(int(''.join((s[i],s[i+1])), 16)))
        except:
            msg += '*'
    return msg

""" ******************************************************* """
"""			Your Implementation Goes Below This Line		"""
""" ******************************************************* """

"""
You have access to some useful variables and functions:
	filepath
		This variable contains the path of the file you entered as a command line argument
	get_binary_file_data(filepath)
		This function will take a filepath and return a binary string with all the information in that file.
	search_for_preamble(bin_str, preamble, start)
		This function will find a preamble within a binary string starting from the index "start". It returns 2
		items, the index of where a preamble was found and a boolean of whether a preamble was found. If no preamble
		is found, it returns the last index of the binary string.
	get_bytes(bin_str, start, num_bytes)
		This function will take a starting index, a number of bytes to process, and a binary string and return
		the index after consuming the bytes and a string containing the bytes (chars)
	bytes_to_hex(byte_str)
		This function takes a string of chars/bytes and will return a hex string of the ascii values of each char. For
		example, the ascii string "hello" would return "68 65 6c 6c 6f 0a".
	decode_hex(s)
		This function takes a string of hex values and returns the ASCII string equivalent. (e.g. "68656c6f0a" --> "hello")
"""
#################################
# MAIN
#################################
# Get binary data from file
bin_str = get_binary_file_data(filepath)
print("binary data from {}: {}\n".format(filepath, bin_str))

# Set up for loop
preamble="AABBCCDD"
start=0

print(bin_str.find('101010101011101111001100'))

# Main loop
while(True):
	start, found = search_for_preamble(bin_str, preamble, start)
	if (found):
		print("found preamble {} at {}".format(preamble, idx_))
	else:
		# Should be done reading
		print("preamble not found")
		quit()

	# Consume bytes for preamble
	get_bytes(bin_str, start, 4)

	# Consume next byte "size"
	start, size = get_bytes(bin_str, start, 1)

	# Consume "size" bytes and store as message
	start, message_ascii = get_bytes(bin_str, start, size)

	# Decode message from hex to ascii
	message_ascii = decode_dex(message_hex)

	# Print the message
	print(message_ascii)
