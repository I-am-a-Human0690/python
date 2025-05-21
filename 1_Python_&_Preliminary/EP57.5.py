# a={
#     "a":{
#         "a1":"a11",
#         "a2":["a21","a22"],
#         "a3":"a31"
#     },
#     "b":{
#         "a1":"a11",
#         "a2":["a21","a22"],
#         "a3":"a31"
#     },
#     "c":{
#         "a1":"a11",
#         "a2":["a21","a22"],
#         "a3":"a31"
#     }
# }
# market={
#     "ร้านป้าพร":{
#         "name":"ป้าพร",
#         "menu":["กระเพราไก่","ก๋วยเตี๋ยว"],
#         "zone":"ตะวันออก"
#     },
#     "ร้านลุงป้อม":{
#         "name":"ลุงป้อม",
#         "menu":["มะม่วง","ทุเรียน"],
#         "zone":"ตะวันตก"
#     },
#     "ร้านน้าใจ":{
#         "name":"น้าใจ",
#         "menu":["นมปั่น","ชาเย็น"],
#         "zone":"ข้าง 7-11"
#     }
# }
# print(a)
# print("")
# print(a["a"]["a2"])
# print("")
# print(a["a"]["a2"][0])
# print("")
# print("a21" in a["a"]["a2"])
# print("")


# print(market)
# print("")
# print(market["ร้านป้าพร"]["menu"])
# print("")
# print(market["ร้านป้าพร"]["menu"][0])
# print("")
# print("กระเพราไก่" in market["ร้านป้าพร"]["menu"])

registered_list = [
    {"name":"Napoleon","course":[
    {"c_name":"Front End Design","credit":3},
    {"c_name":"Intro.to Computer Programming","credit":3},
    {"c_name":"Statistics and Probability","credit":3},
    {"c_name":"Operating Systems","credit":2},
    {"c_name":"Calculus","credit":3},
    {"c_name":"Entrepreneurship","credit":3},
    {"c_name":"Seminar","credit":1},
    {"c_name":"Organization and ISM","credit":3}
]},
    {"name":"Snowball","course":[
    {"c_name":"Discrete Mathematics","credit":3},
    {"c_name":"Databace Systems","credit":3},
    {"c_name":"Cooperative Education","credit":6},
    {"c_name":"Web Dev. and Programming","credit":3},
    {"c_name":"Front End Design","credit":3},
    {"c_name":"Statistics and Probability","credit":3},
    {"c_name":"Intro.to Computer Programming","credit":3},
]},
    {"name":"Squealer","course":[
    {"c_name":"Seminar","credit":1},
    {"c_name":"Digital Marketing","credit":3},
    {"c_name":"Organization and ISM","credit":1},
]},
    {"name":"A","course":[
    {"c_name":"Seminar","credit":1},
    {"c_name":"Digital Marketing","credit":3},
    {"c_name":"Organization and ISM","credit":1},
]}]
print(registered_list[0]["name"])
print(registered_list[0]["course"][0]["c_name"])

# for regiter in registered_list:
#     print(regiter["name"])
#     print('-'*20)
#     total_credit,count_course = 0,0
#     for course in regiter["course"]:
#         count_course+=1
#         print(count_course,course["c_name"],course["credit"])
#         total_credit+=course["credit"]
#     print('-'*20)
#     print("Total : ",total_credit,"credits")
#     print("="*20)
#     print("")