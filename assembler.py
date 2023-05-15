def input():
# ------------------------------------taking input from the file and storing it in final data-----------------------------------------
    f=open("example.txt",'r')
    data=f.readlines()
    l1=[]
    l2=[]
    l3=[]
    no_of_lines=0
    data_for_error_function_dic={}
    data_for_error_function_list=[]
    key=0
    final_data=[]
    var_data=[]
    var_dic={}
