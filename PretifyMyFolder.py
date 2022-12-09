import os
# os.chdir("D:/ravi")
# print(os.getcwd())
# list = os.listdir()
# print(list)
# num=0
# for item in list:
#     if item.endswith(".jpg"):
#         os.rename(item,f"{num}.jpg")
#         num=num+1
#     else:
#         y = item
#         x = item.capitalize()
#         os.rename(y, x)
# print(os.listdir())
def pretify_my_folder():
    path = input("enter full path of folder")
    formate=input("enter the formate of file you want to initialize them with number start from 0")
    if os.path.exists(path):
        os.chdir(path)
        print("you have successfully enter in this folder")
        list = os.listdir()
        print("your all item in this folder ",list)
        num=0
        for item in list:
            if item.endswith(formate):
                os.rename(item, f"{num}.{formate}")
                num = num + 1
            else:
                y = item
                x = item.capitalize()
                os.rename(y, x)
        print("your all item pretified successfully")
        print("your all item in this folder now become ", os.listdir())
    else:
        print("enter correct path")

if __name__ == '__main__':
    pretify_my_folder()






