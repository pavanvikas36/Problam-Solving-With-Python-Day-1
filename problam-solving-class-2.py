# Buterfly Pattern :---
# *                     * 
# * *                 * * 
# * * *             * * * 
# * * * *         * * * * 
# * * * * *     * * * * * 
# * * * * * * * * * * * * 
# * * * * * * * * * * * * 
# * * * * *     * * * * * 
# * * * *         * * * * 
# * * *             * * * 
# * *                 * * 
# *                     * 
# for i in range(6):
#     stars = ""
#     for j in range(6):
#         if(j >= i + 1):
#             stars += "  "
#         else:
#             stars += "* "
#     for l in range(5 - i):
#         stars += "  "
#     for k in range(i + 1):
#         stars += "* "
#     print(stars)
    
# for i in range(6):
#     stars = ""
#     for j in range(6):
#         if(j >= 6 - i):
#             stars += "  "
#         else:
#             stars += "* "
#     for l in range(i):
#         stars += "  "
#     for k in range(6 - i):
#         stars += "* "
#     print(stars)


# Maximum Number In Array :---
# arr = [22, 24, 10, 20, 9, 11, 14, 1]
# max_num = 0
# for i in range(0, len(arr)):
#     if(arr[i] > max_num):
#         max_num = arr[i]
# print(max_num)
# # Secound Maximum Number In Array :---
# max_num_2 = 0
# for i in range(0, len(arr)):
#     if(max_num > arr[i] and max_num_2 < arr[i]):
#         max_num_2 = arr[i]
# print(max_num_2)


# count = 0
# for i in range(6):
#     stars = ""
#     for j in range(5):
#         stars += chr(97 + count) + " "
#         count += 1
#         if(count == 26):
#             count = 0
#     print(stars)