# import json
# json_file = open('sample_data.json')
# # print(open('sample_data.json').read())
# convert_json_to_py = json.load(json_file) # the same as json.load(json_file), dict() u can write and dont write
# # print(convert_json_to_py)
# keys = convert_json_to_py.keys() 
# # print(keys) --> # dict_keys(['totalCount', 'imdata'])
# list_imdata_key = convert_json_to_py['imdata'] # i need imdata key cause within this key i have 'dn': 'topology/pod-1/node-201/sys/phys-[eth1/34]', so on..
# # print(list_imdata_key)
# print('''Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------'''
# )
# for i in list_imdata_key:
#     # print("i is: ",i,"\n")
#     dn = i['l1PhysIf']['attributes']['dn']
#     speed = i['l1PhysIf']['attributes']['speed']
#     mtu = i['l1PhysIf']['attributes']['mtu']
#     print('{0:^1}                              {1:^2}   {2:^2}'.format(dn, speed, mtu))
#    #print("{0:^1}                               {1:^1}{2:^8}".format(q1, q2, q3))