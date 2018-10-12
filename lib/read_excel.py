import xlrd
import sys

excel = xlrd.open_workbook("C:/Users/olllg/PycharmProjects/unitest_jyk-testcase-homework_ld/data/data1.xlsx") #打开excel
# sheet = excel.sheet_by_index(0)
sheet = excel.sheet_by_name("TestAddFuleCade") #获取excel表
# print(sheet.cell(0,0).value) #打印指定行和列
# print(sheet.cell(1,1).value) #打印指定行和列
#
# print(sheet.nrows) #打印表中的所有行数
# print(sheet.ncols) #打印表中的所有列数
#
# 打印单元格所有数据,range是前闭后开
# for i in range(0,sheet.nrows):
#     for j in range(0,sheet.ncols):
#         print(sheet.cell(i, j).value)
# print(sheet.row_values(0))


# 打印所有行的数据
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))

# 找出用例名为test_user_login_normal的测试数据
# for i in range(sheet.nrows):
#     if sheet.cell(i,0).value == "test_user_login_normal":
#         print(sheet.row_values(i))

# 找出用例名为test_user_login_normal的测试数据
# for i in range(sheet.nrows):
#     if sheet.cell(i, 4).value == "<h1>登录成功</h1>":
#         print(sheet.row_values(i))

# 把所有数据都添加到一个列表中（返回excel sheet中的所有数据）使每个测试类只需要打开一次就可以
# def excel_to_list(data_file,sheet_name):
#     excel = xlrd.open_workbook(data_file)
#     sheet = excel.sheet_by_name(sheet_name)
#     result = []
#     for i in range(1,sheet.nrows):
#         result.append(sheet.row_values(i))
#     return result
#
# def get_test_data(data_list,case_name):
#     for case_data in data_list:
#         if case_data[0] == case_name:
#             return case_data

# 简化方法：从excel中读取file,sheet_name,case_name
def get_data(file,sheet_name,case_name):
    wb = xlrd.open_workbook("C:/Users/olllg/PycharmProjects/unitest_jyk-testcase-homework_ld/data/data1.xlsx") #打开excel
    sh = wb.sheet_by_name(sheet_name) #找到工作表

    for i in range(1,sh.nrows): #遍历
        return sh.row_values(i)

if __name__ == "__main__":
    # print(excel_to_list('data.xlsx','TestUserLogin'))
    # print(get_test_data('TestUserLogin','test_user_login_normal'))
    a = get_data('C:/Users/olllg/PycharmProjects/unitest_jyk-testcase-homework_ld/data/data1.xlsx','TestAddFuleCade','test_add_fule_cade_mormal')
    print(a)
    # b = url = a[1]
    # c = data  = a[3]
    # d = expect_res = a[4]
    # print(b)
    # print(c)
    # print(d)



