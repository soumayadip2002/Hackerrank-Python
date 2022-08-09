n = int(input())
numbers = [int(num) for num in input().split(" ", n-1)]

result = (sorted(set(numbers))[-2])
print(result)




