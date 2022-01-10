
import random
from array import *

def KhoiTao_array():
    global My_Array #Biến toàn cục
    My_Array = array('i',[])
    return
#--------------------THEM PHAN TU-----------------------
def ThemN_PhanTu_array():
    # Nhap n Phan tu
    n = int( input('Nhập vào số phần tử cần thêm : '))
    for i in range(n):
        My_Array.append(random.randrange(1,100))
    return 
# Them 1 phần từ vào cuối array 
def Them_1_PhanTu_Append_array():
    a = int( input('Nhập vào số phần tử cần thêm : '))
    My_Array.append(a)
    return 
# Để chèn một mục danh sách tại một chỉ mục được chỉ định
def Them_1_PhanTu_VaoViTri_Insert_array():
    b = int(input('Nhập vào  vị trí '))
    a = int( input('Nhập vào số phần tử cần thêm : '))
    My_Array.insert(b,a) # b == vị trí , a là giá trị thêm.
    return 
# Để nối các phần tử từ một array khác vào Array hiện tại
def Them_array_PhanTu_Extend():
    b = array('i',[1,2,5,8,9])
    My_Array.extend(b)
    return
#----------------------TIM KIEM TRONG ARRAY-------------------------
def TimKiem_PT_b_array():
    b = int(input('Nhập vào số cần Tìm: '))
    for i in My_Array:
        if i == b:
            return True
    return False
#-----------------------XOA PHAN TU------------------------
def Xoa_b_remove_array():
    n = int (0)
    b = int(input('Nhập vào phần tử để xóa : '))
    for i in My_Array:
        if i == b:
            My_Array.remove(b)
            n += 1
    return n
# Xóa vị trí củ thể
def Xoa_PhanTuO_VT_b_pop_array():
    b = int(input('Nhập vào vị trí phần tử để xóa : '))
    if (len( My_Array) <= b ) or (b <= len(My_Array)*(-1)): 
        print('----Không thể xóa!------')
        print('----Không có vị trí-----')
    else:
        My_Array.pop(b)
    return
# Xóa Phần Tử cuối cùng.
def Xoa_PhanTu_Cuoi_pop_array():
    My_Array.pop()
    return
# Xóa vị trí cụ thể del
def Xoa_PhanTu_Vt_b_del_array():
    b = int(input('Nhập vào vị trí phần tử để xóa : '))
    if (len( My_Array) <= b ) or (b <= len(My_Array)*(-1)): 
        print('----Không thể xóa!------')
        print('----Không có vị trí-----')
    else:
        del My_Array[b]
    return

def Xoa_NoDung_Array_del():
   # val.clear(:)
    del My_Array[:]
    return
#-----------------------DUYET ARRAY------------------------
def DuyetArray():
    for i in My_Array:
        print("     ",i,end= '')
    return
#-----------------------MỘT SỐ CÁCH KHÁC------------------
def SoLuongPhanTuTrong_Array():
    return len(My_Array)

#----------
def SapXepTrongArray_Tang():
    for i in range(0, len(My_Array) - 1):
        for u in range(i, len(My_Array)):
            if My_Array[i] < My_Array[u]:
                My_Array[i], My_Array[u] = My_Array[u], My_Array[i]
    return
def SapXepTrongArray_Giam():
    for i in range(0, len(My_Array) - 1):
        for u in range(i, len(My_Array)):
            if My_Array[i] > My_Array[u]:
                My_Array[i], My_Array[u] = My_Array[u], My_Array[i]
    return

def DaoNguocArray():
    My_Array.reverse()
    return
def soLanXuatHienN_TrongArray():
    b = int(input('Nhập vào N để Biết Lần xuất hiện: '))
    return My_Array.count(b) # 1 2 3 4 5 1 2 3 5 1
     
#-----------------------------------------------
def MeNu_array():
    filename = open('menu_Array.txt', encoding = 'UTF-8')
    str = filename.readlines()
    for i in str:
        print(i,end = '')
    return



class Array_Switch:
    def chon_Case(self, ChonBai):
        default = "Câu bạn chọn không tồn tại!!!"
        return getattr(self, 'case_' + str(ChonBai), lambda: default)()
    def case_0(seft):
        print("Thoát Khỏi Chương Trình !!!")
        print("  ----- Xin Cảm Ơn -----")
        print("<<<--------------------->>>")
    def case_1(self):
        KhoiTao_array()
        print(My_Array)
        return
    def case_2(self):
        Them_1_PhanTu_Append_array()
        print(My_Array)
        return 
    def case_3(self):
        Them_1_PhanTu_VaoViTri_Insert_array()
        print(My_Array)
        return
    def case_4(self):
        Them_array_PhanTu_Extend()
        print(My_Array)
        return 
    def case_5(self):
        ThemN_PhanTu_array()
        print(My_Array)
        return 
    def case_6(self):
        c = Xoa_b_remove_array()
        if c != 0:
            print(My_Array)
        else:
            print('Không có phần tử xóa !!!!')
        return 
    def case_7(self):
        Xoa_PhanTuO_VT_b_pop_array()
        print(My_Array)
        return 
    def case_8(self):
        Xoa_PhanTu_Cuoi_pop_array()
        print(My_Array)
        return 
    def case_9(self):
        Xoa_PhanTu_Vt_b_del_array()
        print(My_Array)   
        return 

    def case_10(self):
        Xoa_NoDung_Array_del()
        print(My_Array)
        return 

    def case_11(self):
        kq = TimKiem_PT_b_array()
        if kq == True:
            print('Có trong Array!!')
        else:
            print('Không có trong Array !')
        return 
    def case_12(self):
        DuyetArray()
        return 
    def case_13(self):
        c = SoLuongPhanTuTrong_Array()
        print('Sô lượng có trong mảng là : ',c)
        return 
    def case_14(self):
        SapXepTrongArray_Giam()
        print(My_Array)
        return 
    def case_15(self):
        SapXepTrongArray_Tang()
        print(My_Array)
        return 
    def case_16(self):
        c = soLanXuatHienN_TrongArray()
        print('Số phần tử có trong mảng là :',c)
        return 
    def case_17(self):
        DaoNguocArray()
        print(My_Array)
       
        return 
def main_Phu_array():
    MeNu_array()
    chon = -1
    while chon != 0:
        print("\n<<<--------------------->>>")
        chon = int( input('Nhập vào bài cần làm : '))
        ChonMeNu = Array_Switch()
        ChonMeNu.chon_Case(chon)    
    return
if __name__ == "__main__":
    main_Phu_array()
