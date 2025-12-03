t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	dif = abs(a - b)
	move = (dif + 9) // 10
	print(move)
