# Patterns

# 1) First Pattern :---
# *                     * 
# * *                 * * 
# * * *             * * * 
# * * * *         * * * * 
# * * * * *     * * * * * 
# * * * * * * * * * * * * 
# for i in range(6):
#     stars = ""
#     for j in range(1 + i):
#         stars += "* "
#     for k in range(5 - i):
#         stars += " "
#     for l in range(5 - i):
#         stars += "   "
#     for j in range(1 + i):
#         stars += "* " 
#     print(stars)

# 2) Secounf Pattern :---
# * * * * 
# *   * 
# * * 
# * 
# In Place of 4 we can use n and assign a number value to the n
# for i in range(4):
#     stars = ""
#     for j in range(4 - i): # 4 - 1 - 1 ==> 0, 3
#         if(i == 0 or j == 0 or i == 4 - 1 or j == 4 - i - 1):
#             stars += "* "
#         else:
#             stars += "  "
#     print(stars)

# 3) Third Even And Odd Number
# n = 6
# if(n & 1):
#     print("Odd Number")
# else:
#     print("Even Number")

