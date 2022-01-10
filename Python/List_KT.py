import random

def KhoiTaoList():
    global My_List #Biến toàn cục
    My_List = list() # khởi tạo list[]
    return
#--------------------THEM PHAN TU-----------------------
def ThemN_PhanTu_List():
    # Nhap n Phan tu
    n = int( input('Nhập vào số phần tử cần thêm : '))
    for i in range(n): # [1,2,3,4,5]
        My_List.append(random.randrange(1,100))
    return 
# Them 1 phần từ vào cuối List 
def Them_1_PhanTu_Append_List():
    a = int( input('Nhập vào số phần tử cần thêm : '))
    #a = input('Nhập vào số phần tử cần thêm : ')
    My_List.append(a)
    return 
# Để chèn một mục danh sách tại một chỉ mục được chỉ định
def Them_1_PhanTu_VaoViTri_Insert_List():
    b = int(input('Nhập vào  vị trí '))
    a = int( input('Nhập vào số phần tử cần thêm : '))
    My_List.insert(b,a) # b == vị trí , a là giá trị thêm.
    return 
# Để nối các phần tử từ một List khác vào List hiện tại
def Them_List_PhanTu_Extend():
    # (tuples, sets, dictionaries etc.) có thể thêm
    b = [1,2,5,8,9]
    My_List.extend(b)
    return
#-----------------------XOA PHAN TU------------------------
def Xoa_b_remove_list():
    n = int(0)
    b = int(input('Nhập vào phần tử để xóa : '))
    #b = input('Nhập vào phần tử để xóa : ')
    for i in My_List:
        if i == b:
            My_List.remove(b) # tìm và xóa cho mình
            n += 1
    return n
# Xóa vị trí củ thể
def Xoa_PhanTuO_VT_b_pop_List():
    b = int(input('Nhập vào vị trí phần tử để xóa : '))
    if (len( My_List) <= b ) or (b <= len(My_List)*(-1)): 
        print('----Không thể xóa!------')
        print('----Không có vị trí-----')
    else:
        My_List.pop(b)
    return
# Xóa Phần Tử cuối cùng.
def Xoa_PhanTu_Cuoi_pop_list():
    My_List.pop()
    return

# Xóa vị trí cụ thể del
def Xoa_PhanTu_Vt_b_del_List():
    b = int(input('Nhập vào vị trí phần tử để xóa : '))
    if (len( My_List) <= b ) or (b <= len(My_List)*(-1)): 
        print('----Không thể xóa!------')
        print('----Không có vị trí-----')
    else:
        del My_List[b]
    return

# Xóa toàn bộ danh sách del
def Xoa_List_del():
    del My_List [:]
    return
def Xoa_NoDung_List_clear():
    My_List.clear()
    return
#----------------------TIM KIEM TRONG LIST-------------------------
def TimKiem_PT_b_List():
    b = int(input('Nhập vào số cần Tìm: '))
    a = My_List.count(b)
    if a != 0:
        return True 
    return False
#-----------------------DUYET LIST------------------------
def DuyetList():
    for i in My_List:
        print('    ',i, end = '')
    return
#-----------------------MỘT SỐ CÁCH KHÁC------------------
def SoLuongPhanTuTrong_List():
    b = len(My_List)
    return b
def SapXepTrong_List_Tang():
    My_List.sort()
    return
def SapXepTrong_List_Giam():
    My_List.sort(reverse = True)# 1 5 6 -> 6 5 1
    return
def DaoNguoc_List():
    My_List.reverse() # 1 5 4 7 8 2  -> 2 8 7 4 5 1
    return
def  myFunc(n):
    return abs(n - z)

def SapXepDuaTrenN_List():
    global z
    z = int(input('Nhập vào số cần Xắp xếp gần nhất : '))
    My_List.sort(key = myFunc)
    return
#-----------------------------------------------
def MeNu_List():
    filename = open('menu_List.txt', encoding = 'UTF-8')
    str = filename.readlines()
    for i in str:
        print(i,end = '')
    return


def main_Phu_List():
    MeNu_List()
    chon = -1
    while chon != 0:
        print("\n<<<--------------------->>>")
        chon = int( input('Nhập vào bài cần làm : '))
        chonList_ = List_Switch()
        chonList_.chon_Case(chon)
    return

class List_Switch:
    def chon_Case(self, ChonBai):
        default = "Câu bạn chọn không tồn tại!!!"
        return getattr(self, 'case_' + str(ChonBai), lambda: default)()
    def case_0(seft):
        print("Thoát Khỏi Chương Trình !!!")
        print("  ----- Xin Cảm Ơn -----")
        print("<<<--------------------->>>")
    def case_1(self):
        KhoiTaoList()
        print(My_List)
        return
    def case_2(self):
        Them_1_PhanTu_Append_List()
        print(My_List)
        return 
    def case_3(self):
        Them_1_PhanTu_VaoViTri_Insert_List()
        print(My_List)
        return
    def case_4(self):
       Them_List_PhanTu_Extend()
       print(My_List)
       return 
    def case_5(self):
        ThemN_PhanTu_List()
        print(My_List)
        return 
    def case_6(self):
        c = Xoa_b_remove_list()
        if c != 0:
            print(My_List)
        else:
            print('Không có phần tử xóa !!!!')
        return 
    def case_7(self):
        Xoa_PhanTuO_VT_b_pop_List()
        print(My_List)
        return 
    def case_8(self):
        Xoa_PhanTu_Cuoi_pop_list()
        print(My_List)
        return 
    def case_9(self):
        Xoa_PhanTu_Vt_b_del_List()
        print(My_List)
       
        return 
    def case_10(self):
        Xoa_List_del()
        print('Đã Xóa !')
        print(My_List)
        return 

    def case_11(self):
        Xoa_NoDung_List_clear()
        print(My_List)
        
        return 
    def case_12(self):
        kq = TimKiem_PT_b_List()
        if kq == True:
            print('Có trong List!!')
        else:
            print('Không có trong List !')
        return 
    def case_13(self):
        DuyetList()
        return 
    def case_14(self):
        b = SoLuongPhanTuTrong_List()
        print('Có số lượng phần tử trong Array là : ',b)
        
        return 
    def case_15(self):
        SapXepTrong_List_Giam()
        print(My_List)
       
        return 
    def case_16(self):
        SapXepTrong_List_Tang()
        print(My_List)
       
        return 
    def case_17(self):
        DaoNguoc_List()
        print(My_List)
       
        return 
    def case_18(self):
        SapXepDuaTrenN_List()
        print(My_List)
        return 

if __name__ == "__main__":
    main_Phu_List()