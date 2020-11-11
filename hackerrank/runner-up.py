from itertools import combinations_with_replacement
s = "HACK 2".split()
for x in sorted(list(combinations_with_replacement("".join(sorted(s[0])), int(s[1])))):
    r = ""
    for i in range(int(s[1])):
        r += x[i]
    print(r)

# from itertools import combinations
# s = "HACK 2".split()
# for c in range(1, int(s[1])+1):
#     for x in sorted(list(combinations("".join(sorted(s[0])), c))):
#         r = ""
#         for i in range(c):
#             r += x[i]
#         print(r)

# from itertools import permutations
# s = "HACK 2".split()
# s = "ABCD 3".split()
# for x in sorted(list(permutations(s[0], int(s[1])))):
#     r = ""
#     for i in range(int(s[1])):
#         r += x[i]
#     print(r)


# from collections import namedtuple
# n, Score = int(input()), namedtuple('Score', input().split())
# scores = [Score(*input().split()).MARKS for i in range(n)]
# print("%.2f"% (sum(map(int,scores))/n))

#from collections import namedtuple
#s = ("ID         MARKS      NAME       CLASS".split())
#Students = namedtuple('Students', s)


# from itertools import groupby
#
#
# def group_by(arr):
#     for a, b in groupby(arr):
#         print(f'{a}')
#
#
# print(group_by([1, 1, 3, 3, 1, 1,  4, 4, 5, 5]))



# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(0))


# def wrap(string, max_width):
#     i = 0
#     s = []
#     while i < len(string) - max_width:
#         s.append(string[i:i + max_width])
#         i += max_width
#     s.append(string[i:])
#     return "\n".join(s)
#
# print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))


#arr = [2, 3, 6, 6, 5]
#m = max(arr)
#print(max([x for x in arr if x != m]))
#arr.insert(2, 9)
#print(arr)
#s = "this is a string"
#print('-'.join(s.split()))
# a = "holaholaholahola"
# b = "hola"
# c = 0
# for i in range(len(a)):
#     to = i + len(b)
#     if a[i:to] == b:
#         c += 1


# thickness = 5
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(
#         (
#                 (c*(thickness-i-1)).rjust(thickness)
#                 +c+
#                 (c*(thickness-i-1)).ljust(thickness)
#         ).rjust(thickness*6))
