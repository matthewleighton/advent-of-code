import hashlib

def get_data():
	with open('data.txt') as file:
		data = file.readline().rstrip()
		file.close()
	return data

secret_key = get_data()

i = 0
task1, task2 = False, False

while not task1 or not task2:
	hashed = hashlib.md5((secret_key + str(i)).encode()).hexdigest()

	if not task1 and hashed[:5] == '00000':
		task1 = i

	if hashed[:6] == '000000':
		task2 = i

	i+=1

print(f'Task 1: {task1}')
print(f'Task 2: {task2}')
