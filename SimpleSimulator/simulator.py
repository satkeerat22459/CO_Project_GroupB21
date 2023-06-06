
# -------------------------------------------Sarthak srivastav starts--------------------------------------------
def sub(i,c):
    # print("sub")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1 = reg_dic(str(i[7:10]))
    reg2 = reg_dic(str(i[10:13]))
    reg3 = reg_dic(str(i[13:]))
    reg1 = reg2 - reg3
    if(reg1<0 or reg1>127):
        FLAGS="0000000000001000"
        reg1=0
        assigning_value_in_global_var(i[7:10],reg1)
    else:
        assigning_value_in_global_var(i[7:10],reg1)
        FLAGS="0000000000000000"
    print_output(i,c)

def mov_imm(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    # print("mov_imm")
    # print(i)
    reg = reg_dic(str(i[6:9]))
    imm_bin = ((i[9:]))
    imm_int = int(imm_bin, 2)
    reg = imm_int
    # print(reg)
    assigning_value_in_global_var(i[6:9], reg)
    FLAGS="0000000000000000"
    # print(reg_dic)
    print_output(i,c)

def mov_reg(i,c):
    # print("mov_reg")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1 = reg_dic(str(i[10:13]))
    reg2 = reg_dic(str(i[13:]))
    # print("reg1",reg1)
    # print("reg2",int(reg2))
    reg1 = int(reg2)
    
    assigning_value_in_global_var(i[10:13],reg1)
    FLAGS="0000000000000000"
    print_output(i,c)

def load(i,c):
    # print("load")
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg = reg_dic(str(i[6:9]))
    mem_addr = int(i[9:],2)
    reg=mem_dump[mem_addr]
    assigning_value_in_global_var(str(i[6:9]), reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print(i)

def store(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg = reg_dic(str(i[6:9]))
    mem_addr = int(i[9:],2)
    mem_dump[mem_addr]=integer_to_binary_with_padding(reg)
    assigning_value_in_global_var(str(i[6:9]), reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print("store")
    # print(i)

def multiply(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg1=reg_dic(i[10:13])*reg_dic(i[13:])
    assigning_value_in_global_var(i[7:10],reg1)
    FLAGS="0000000000000000"
    if(reg1<0 or reg1>127):
        FLAGS="0000000000001000"
        reg1=0
    
    print_output(i,c)
    # print("mulyiply")
    # print(i)

def divide(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    if(reg_dic(i[13:])==0):
        FLAGS="0000000000001000"
        reg0=0
        reg1=0
        assigning_value_in_global_var("000", reg0)
        assigning_value_in_global_var("001", reg1)
    else:
        reg0=reg_dic(i[10:13])//reg_dic(i[13:])
        reg1=reg_dic(i[10:13])%reg_dic(i[13:])
        assigning_value_in_global_var("000", reg0)
        assigning_value_in_global_var("001", reg1)
        FLAGS="0000000000000000"
    print_output(i,c)
    # print("divide")
    # print(i)

def right_shift(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg=reg_dic(i[6:9])
    # print(reg)
    imm=int((i[9:]),2)
    # print(imm)
    # # imm=int(imm,2)
    reg=reg>>imm
    # print(reg)
    assigning_value_in_global_var(i[6:9], reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print("right shift")
    # print(i)

def left_shift(i,c):
    global FLAGS,R1,R2,R3,R4,R5,R6,R0
    reg=reg_dic(i[6:9])
    # print(reg)
    imm=int((i[9:]),2)
    # print(imm)
    # # imm=int(imm,2)
    reg=reg<<imm
    # print(reg)
    assigning_value_in_global_var(i[6:9], reg)
    FLAGS="0000000000000000"
    print_output(i,c)
    # print("left shift")

    # print(i)

# -------------------------------------------Sarthak srivastav ends------------------------------------------------------------
