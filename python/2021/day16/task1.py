import numpy as np

def get_data():
	with open('data.txt') as file:
		hex_data = file.readline()
		binary_data = bin(int(hex_data, 16))[2:]

		file.close()

	return binary_data

def parse_data(binary, pad=False):
	print('-----------------------------------------')
	parsed_data = []

	if pad:
		binary = pad_binary(binary)

	if not len(binary):
		return False

	packet, binary = get_packet(binary)

	parsed_data.append(packet)

	



	return binary

def pad_binary(binary):
	required_leading_zeros = 4 - len(binary) % 4

	if required_leading_zeros == 4:
		required_leading_zeros = 0

	binary = '0'*required_leading_zeros	+ binary

	return binary

def get_packet_version(binary):
	packet_version_binary = binary[:3]
	packet_version = int(packet_version_binary, 2)

	binary = binary[3:]

	return packet_version, binary

def get_packet_type(binary):
	packet_type_binary = binary[:3]
	packet_type = int(packet_type_binary, 2)

	binary = binary[3:]

	return packet_type, binary

def get_length_type_id(binary):
	length_type_id = int(binary[0])
	binary = binary[1:]

	return length_type_id, binary

	bits_describing_packet_length = 11 if length_type_id else 15

	packet_length_binary = binary[:bits_describing_packet_length]
	packet_length = int(packet_length_binary, 2)

	binary = binary[bits_describing_packet_length:] 

	return packet_length, binary

def get_packet_length(binary, length_type_id):
	bits_describing_packet_length = 11 if length_type_id else 15

	packet_length_binary = binary[:bits_describing_packet_length]

	packet_length = int(packet_length_binary, 2)

	binary = binary[bits_describing_packet_length:] 

	return packet_length, binary


def get_sub_packets(binary, length_type_id, packet_length):
	sub_packet_list = []

	if length_type_id == 0:
		print('Length Type ID == 0')

		sub_packets_binary = binary[:packet_length]
		print('sub_packets_binary')
		print(sub_packets_binary)

		while len(sub_packets_binary):
			sub_packets_binary = parse_data(sub_packets_binary)

		parse_data(sub_packets_binary)

	else:
		number_of_sub_packets = packet_length

		for i in range(number_of_sub_packets):
			sub_binary = binary[:11]
			# sub = int(sub_binary, 2)

			sub_packet = get_packet(sub_binary)

			binary = binary[11:]

			sub_packet_list.append(sub_packet)

	return sub_packet_list

def get_literal_value(binary):
	print('--- get_literal_value ---')
	# print(len(binary))

	# binary = pad_binary(binary)

	# required_leading_zeros = 4 - ( len(binary) % 4)

	# print(binary)
	# print(len(binary))

	# print(f'required_leading_zeros {required_leading_zeros}')

	# # binary += '0'*required_leading_zeros

	# binary = '0'*required_leading_zeros + binary

	# print(binary)

	binary_number = ''

	finished = False
	while not finished :
		first_bit = binary[:1]
		four_bits = binary[1:5]

		print(f'First bit: {first_bit}')

		print(f'four_bits: {four_bits}')

		binary_number += four_bits

		binary = binary[5:]

		if first_bit == '0':
			finished = True

	print(binary_number)

	literal_value = int(binary_number, 2)

	print(literal_value)

	print(f'Remaining binary:{binary}')



	# print(binary)

	# binary_groups = split_binary_into_groups_of_4(binary)

	# print(binary_groups)

	# print(binary)

	# literal_value_binary = ''

	# for group in binary_groups:
	# 	literal_value_binary += group[1:]

	# literal_value = int(literal_value_binary, 2)

	return literal_value, binary

def split_binary_into_groups_of_4(binary):
	groups = []

	for i in range(int(len(binary)/4)):
		pointer = i*4
		g = binary[pointer:pointer+4]
		groups.append(g)

	return groups

def get_packet(binary):
	global version_numbers
	print('---get_packet---')
	print(binary)
	packet_version, binary = get_packet_version(binary)

	version_numbers.append(packet_version)

	packet_type, binary = get_packet_type(binary)

	print(f'Packet Version: {packet_version}')
	print(f'Packet Type: {packet_type}')

	if packet_type == 4: # Literal value
		print('Packet Type == 4')
		literal_value, binary = get_literal_value(binary)
		print(literal_value)
		return literal_value, binary

	else: # Operator
		# print(binary)
		# print('')
		length_type_id, binary = get_length_type_id(binary)

		print(f'Length Type ID: {length_type_id}')

		packet_length, binary = get_packet_length(binary, length_type_id)

		print(f'Packet Length: {packet_length}')

		sub_packets = get_sub_packets(binary, length_type_id, packet_length)

		print('Sub packets:')
		print(sub_packets)


		# print(binary)

		# print(length_type_id)





	return 'test', binary


binary = get_data()
version_numbers = []

parsed_data = parse_data(binary, pad=True)

# print(parsed_data)

print('::::::::::::::::::::::::::::::::::::::')
print(version_numbers)
print(np.sum(version_numbers))