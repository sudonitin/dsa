from copy import deepcopy

# TOOK A HINT (EXTENSION OF PREV QUESTION i.e. Balanced Paranthesis)
# 
def generate_abbreviations(string):
    result = [""]
    list_str = list(string)
    while True:
        result_len = len(result)
        new_char = list_str[len(result[0])]
        new_result = []
        for i in range(result_len):
            # push char
            new_result.append(result[i]+new_char)
            # push 1
            if len(result[i]) != 0 and result[i][len(result[i])-1].isdigit():
                temp = list(result[i])
                temp[len(result[i])-1] = str(int(temp[len(result[i])-1])+1)
                result[i] = "".join(temp)
                new_result.append(result[i])
            else:
                new_result.append(result[i]+"1")
        result = new_result
        if len(result[0]) == len(string):
            return result

print(generate_abbreviations("BAT"))

# 2ND FAILED ATTEMPT
# def find_all_subsets(arr):
#     arr = list(arr)
#     # print(arr, "%")
#     result = [[]]
#     for i in arr:
#         temp = []
#         result_len = len(result)
#         for subset in range(result_len):
#             # print(result[subset] + [i])
#             temp.append(result[subset] + [i])
#         result += temp
#     result = ["".join(sub) for sub in result]
#     return generate_abbreviations(result, arr)

# def generate_abbreviations(result, og_str):
#     og_str = "".join(og_str)
#     # print(og_str, "$")
#     # print(result)
#     new_result = []
#     for subset in result:
#         if subset == "":
#             subset = og_str
#             # print(subset, "---")
#         else:
#             temp = deepcopy(og_str)
#             subset = temp.replace(subset, str(len(subset)))
#         # print(subset)
#         new_result.append(subset)
#     # print(result, "%")
#     return set(new_result)

# print(find_all_subsets("BAT"))

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
