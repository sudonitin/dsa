
print(find_all_subsets("abc"))

# HAGGA HUA CODE N LOGIC
# def find_all_subsets(arr):
#     string_results = [arr]
#     og_str = arr
#     arr = list(arr)
#     result = [[]]
#     for i in arr:
#         temp = []
#         result_len = len(result)
#         for subset in range(result_len):
#             # print(result[subset] + [i])
#             temp.append(result[subset] + [i])
#             # string evaluation
#             temp_str = "".join(result[subset] + [i])
#             # temp_str = list(result[subset] + [i])
#             append_str = ""
#             count = 0
#             count_pushed = False
#             # print("comparing for", temp_str)
#             if len(temp_str) == len(og_str):
#                 append_str += str(len(og_str))
#             else:
#                 for j in range(len(og_str)):
#                     if temp_str == og_str[j:len(og_str)-1]:
#                         print("#", temp_str)
#                         count += 1
#                     else:
#                         if count>0 and not count_pushed:
#                             count_pushed = True
#                             append_str += str(count)+og_str[j]
#                         else:
#                             append_str += og_str[j]
#                 if len(append_str) != len(og_str):
#                     append_str += str(count)
#                 # for j in range(len(og_str)):
#                 #     if j < len(temp_str):
#                 #         if temp_str[j] == og_str[j]:
#                 #             count += 1
#                         # else:
#                         #     if not count_pushed:
#                         #         count_pushed = True
#                         #         append_str += str(count)+og_str[j]
#                         #     else:
#                         #         append_str += og_str[j]
#                 #     else:
#                 #         if not count_pushed:
#                 #             count_pushed = True
#                 #             append_str += str(count)+og_str[j]
#                 #         else:
#                 #             append_str += og_str[j]
#             # if append_str == "":
#             #     append_str += str(count)
#             print(append_str, result[subset] + [i])
#             string_results.append(append_str)
#         result += temp
#         # print(append_str, temp)
#         # print(string_results)
#         # print(result)
#     return string_results
#     # return result
