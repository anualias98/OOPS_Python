"""match"""
# import re
# pattern=r"avodha"
# if re.match(pattern,"avodha hello  how are you...stay safe...."):
#     print("matched")
# else:
#     print("not matched")
"""search"""
# import re
# pattern=r"avodha"
# if re.search(pattern," hello avodha how are you...stay safe...."):
#     print("matched")
# else:
#     print("not matched")

"""findall"""
# import re
# pattern=r"avodha"
# print(re.findall(pattern,"avodha hello  how are you...stay safe..avodha.."))
""" find & replace"""
# import re
# str="hai avodha,how r u"
# pattern=r"avodha"
# new1=re.sub(pattern,"AVODHA NEW",str)
# print(new1)

""" """
# import re
# pattern=r"av.dha"
# if re.match(pattern,"aviidha"):
#     print("matched")
# else:
#     print("not matched")

"""chr class"""
import re
pattern=r"[A-Z][a-z][0-9]"
if re.search(pattern,"Av3"):
    print('corrected')
else:
    print("not correct")