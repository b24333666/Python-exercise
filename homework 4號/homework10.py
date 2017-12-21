# #全班學生
all_student = {"John","Tina","Mary","Fiona","Tom","Tracy","Steven","Jimmy","Paul"}
# #英文及格
en_pass = {"John","Mary","Tom","Tracy","Jimmy","Paul"}
# #數學及格
math_pass={"Mary","Tom","Tracy","Steven","Tina"}

print("英數都及格的：{}".format( en_pass & math_pass ))
print("數學不及格的：{}".format( all_student - math_pass  ))
print("英文及格但是數學不及格的：{}".format( all_student - en_pass ))