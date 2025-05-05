from pwn import *
import re

host = "3d8aa0bd0bd49305.247ctf.com"
port = 50138

context.log_level = 'error'

conn = remote(host, port)

print(conn.recvline())
print(conn.recvline())

for i in range(500):

	math = conn.recvline().decode('UTF-8')
	nums = re.findall(r'\d+', math)

	num1 = int(nums[0])
	num2 = int(nums[1])

	result = str(num1 + num2)
	final = (result + '\r\n').encode('UTF-8')
	conn.sendline(final)
	conn.recvline()
	print(f"the operation {i} has been done with a {result}")

print(conn.recvline().decode('UTF-8'))

# 247CTF{6ae15c0aeb45a334b3f01eb0dda5cab1}