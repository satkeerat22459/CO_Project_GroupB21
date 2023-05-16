# --------------------------------------------------------Satwik Garg start--------------------------------
def inpu():
# ------------------------------------taking input from the file and storing it in final data-----------------------------------------
    # f=open("example.txt",'r')
    # data=f.readlines()
    # print("data",data)
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
    data=[]

    test=[]

    while True:
        try:
            testline=input()
            test.append(testline)
        except EOFError:
            break
    # print(test)

    for i in test:
        # for j in i:
        l3.append(i.split())
        # l1.append(l4)
        # l4=[]
            

    

    # print("data",data)
    for i in data:
        l3.append(i.split())
    
    for i in l3:
        if(i!=[]):
            l1.append(i)
    # print("l1",l1)
# --------------------------------------data for error function-------------------------------------------------------------------
    for i in l1:
        if(i!=[]):
            
            data_for_error_function_list.append(i)    #dictionary of all the data with line number
            data_for_error_function_dic[key]=i    #list of all the data
            key+=1

# --------------------------------------------------data for all other funtions----------------------------------------------
    for i in l1:
        if((i!=[]) and i[0]!='var'):
            final_data.append(i)
            no_of_lines+=1

    for i in l1:
        if(i[0]=="var"):
            var_data.append(i[1])
    k=0
    for i in var_data:
        k=k+1
        var_dic[i]=str(format((no_of_lines+k-1),'b')).rjust(7,'0')

    # f.close()
    return final_data,no_of_lines-1,var_dic,data_for_error_function_dic,data_for_error_function_list


# I have created all_ISA, register, variable, and label lists. Now u guys have to write the code for the errors.


def error(data_for_error_function_dic,data_for_error_function_list):
    # -------------------------------------------------------write the error code here------------------------------------------------------
    all_isa=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
    reg_lst = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]
    jump_statements=["jmp","jlt","jgt","je"]
    three_register=["add","sub","mul","xor","or","and"]
    two_register=["div","not","cmp"]
    imm_register=["ld","st","rs","ls"]
    register_dollar=["ls","rs"]
    register_with_variables=["ld","st"]
    var_list=[]#list for variables
    label_list=[]#list for lables

    for i in data_for_error_function_list:
        if(i[0]=="var"):
            var_list.append(i[1])
    
    # print()
    # print("variable list",var_list)

    for i in data_for_error_function_list:
        if(i[0][-1]==":" ):
            label_list.append(i[0][:len(i[0])-1])
    # print()
    # print("label list",label_list)
    # print()
    # -----------------------------------------------------$ in ls and rs------------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0]=="ls" or i[0]=="rs"):
            if(i[2][0]!="$"):
                print("no dollar sign")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
            
    # ------------------------------------------- no of registers ------------------
    for i in data_for_error_function_list:
        if(i[0] in three_register and len(i)!=4):
            print("inncorrect number of registers")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()
        if((i[0] in two_register or i[0] in imm_register or i[0]=="mov") and len(i)!=3):
            print("incorrect number of registers")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

    # --------------------------------------------------------    A     ------------------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] not in all_isa and (i[0])[:len(i[0])-1] not in label_list and i[0] not in reg_lst and i[0]!="var"):
            print(i[0])
            print("Typos in instruction name")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()
    
    for i in data_for_error_function_list:
        if(i[0] in three_register):
            # print(i)
            if(i[1] not in reg_lst or i[2] not in reg_lst or i[3] not in reg_lst):
                print("Typos in register name")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] in two_register):
            if(i[1] not in reg_lst or i[2] not in reg_lst):
                print("Typos in register name")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] in imm_register):
            if(i[1] not in reg_lst):
                print("Typos in register name")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list):
            if(i[1] in three_register):
                if(i[2] not in reg_lst or i[3] not in reg_lst or i[4] not in reg_lst):
                    print("Typos in register name")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in two_register):
                if(i[2] not in reg_lst or i[3] not in reg_lst):
                    print("Typos in register name")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in imm_register):
                if(i[2] not in reg_lst):
                    print("Typos in register name")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
        elif(i[0]=="mov" and i[1] not in reg_lst):
            print("Typos in register name")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()
        elif(i[0]=="mov" and i[2] not in reg_lst and (i[2])[0]!="$"):
            print("Typos in register name")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

# ----------------------------------------------------       B              --------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in register_with_variables):
            if(i[2] not in var_list):
                print("Use of undefined variables")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list and i[1] in register_with_variables):
            if(i[3] not in var_list):
                print("Use of undefined variables")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
# --------------------------------------------Satwik Garg end------------------------------------
# --------------------------------------------Satkeerat Singh start-------------------------------------
# ---------------------------------------------------        C               --------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in jump_statements):
            if(i[1] not in label_list):
                print("Use of undefined labels")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
            
# ------------------------------------------------------       D             ------------------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in three_register):
            # print(i)
            if(i[1]=="FLAGS" or i[2]=="FLAGS" or i[3]=="FLAGS"):
                print("Illegal use of FLAGS register")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] in two_register):
            if(i[1]=="FLAGS" or i[2]=="FLAGS"):
                print("Illegal use of FLAGS register")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif(i[0] =="FLAGS"):
            if(i[1] not in reg_lst):
                print("Illegal use of FLAGS register")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list):
            if(i[1] in three_register):
                if(i[2]=="FLAGS" or i[3]=="FLAGS" or i[4]=="FLAGS"):
                    print("Illegal use of FLAGS register")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in two_register):
                if(i[2]=="FLAGS" or i[3]=="FLAGS"):
                    print("Illegal use of FLAGS register")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
            elif(i[1] in imm_register):
                if(i[2]=="FLAGS"):
                    print("Illegal use of FLAGS register")
                    print("line no",data_for_error_function_list.index(i)+1)
                    quit()
        elif(i[0]=="mov" and i[1]=="FLAGS"):
            print("Illegal use of FLAGS register")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()



# ---------------------------------------------          E                ---------------------------------------
    for i in data_for_error_function_list:
        if(i[0] in register_dollar):
            if(int(i[2][1:])>128):
                print("Illegal Immediate values (more than 7 bits)")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
        elif((i[0])[:len(i[0])-1] in label_list):
            if(i[1] in register_dollar and int(i[3][1:])>128):
                print("Illegal Immediate values (more than 7 bits)")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()

# -----------------------------------------------            F                   --------------------------------------
    for i in data_for_error_function_list:
        if((i[0] in register_with_variables and i[2] in label_list) or (i[0])[:len(i[0])-1] in var_list):
            print("Misuse of labels as variables or vice-versa")
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

# -----------------------------------------     G                     --------------------------------------------------------------------
    k=0
    for i in data_for_error_function_list:
        if(i[0]=="var"):
            k+=1
        else:
            k=0
        if(k==1 and data_for_error_function_list.index(i)!=0):
            print("Variables not declared at the beginning")    
            print("line no",data_for_error_function_list.index(i)+1)
            quit()

#--------------------------------------------------------      I               ----------------------------------
    for i in data_for_error_function_list:
        if(i[0]=="hlt"):
            if(data_for_error_function_list.index(i)!=len(data_for_error_function_list)-1):
                print("hlt not being used as the last instruction")
                print("line no",data_for_error_function_list.index(i)+1)
                quit()
# ----------------------------------------------            H               --------------------------------------------
    try:
        if((data_for_error_function_list[len(data_for_error_function_list)-1][1]!="hlt")):
            print("Missing hlt instruction")
            print("Last line")
            quit()

    except:
        if((data_for_error_function_list[len(data_for_error_function_list)-1][0]!="hlt")):
            # print(data_for_error_function_list[len(data_for_error_function_list)-1][1])
            # print(data_for_error_function_list[len(data_for_error_function_list)-1][0])
            print("Missing hlt instruction")
            print("Last line")
            quit()
    





        

        
# --------------------------creating a list of all registers-------------------------
reg_lst = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]


# --------------------------returns registers address-------------------
def register(r):
    if(r=="R0"):
        return "000"
    elif(r=="R1"):
        return "001"
    elif(r=="R2"):
        return "010"
    elif(r=="R3"):
        return "011"
    elif(r=="R4"):
        return "100"
    elif(r=="R5"):
        return "101"
    elif(r=="R6"):
        return "110"
    elif(r=="FLAGS"):
        return "111"

# --------------------------------------------------return variable address----------------------------------------------
def variable(var,var_dic):
    for i in var_dic.keys():
        if(i==var):
            return var_dic[var]


# ----------------------------------integer_to_binary_with_padding(used in satwik's funtion)----------------------
def integer_to_binary_with_padding(value):
    binary_number=format(int(value),'b')
    return str(binary_number).rjust(7,'0')



# --------------------------taking_input_in_label_dictionary with value as line number(used in satwik's function)----------------
def taking_input_in_label_dictionary(key,label_name_dictionary,data):
    k=0
    for i in data:
        k+=1
        if((i[0])[:len(key)]==key):
            value=integer_to_binary_with_padding(k-1)
    
    label_name_dictionary[key]=value
# -----------------------------------------------------Satkeerat Singh end--------------------------------------------
