# dict_demo = {
#     "rno" : 89,
#     "name" : "Bharati",
#     "subject" : ("English","Maths","Science"),
#     "hobbies" : ["coding","reading","writing"],
#     "details" : {"address":"Mumbai","office":"Pune"}
# }

# print(dict_demo["name"])
# print(dict_demo["subject"][1])
# print(dict_demo["details"]["office"])
# print(dict_demo["hobbies"][0])


# dic_name = {
#     # [1,2,3] : 89,
#     1.5 : "subha",
#     ("English", "Maths") : ( "100","89"),
#     # {"gk", "computer"}   : ("pass"),
#     "details" : {"code":"ko","read":"po","write":5},
#     True : {"code":"ko","read":"po","write":5}
# }

# print(dic_name[[1,2,3]])               #List as key
# print(dic_name[1.5])                   #float as key
# print(dic_name["(English, Maths)"])      #Tuple as key
# print(dic_name["{gk, computer}"] )        #set as key
# print(dic_name["1.5"])                    #float as key



tup = ({1,2,3},189)
# lst = list(tup)
tup[0].add(89)
print(tup)