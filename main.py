# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
url = "https://diip.dianliantech.com/diip/api/users/SystemViewTest/"
header = {'Authorization':  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjIwMjEwNjIwMjExMV8xMzcxNTQxNzU4MiIsImV4cCI6MTYyODM5MTY0OH0.seZ9ZxBraFhn3oko4H196gHPvbZbD97dHyfKtBbe5aU',
          'ledger-code': '101',
          'org-code': '101','role-code': '101role_101',
          'tenantry-code': 'yide_jt',
          'Content-Type': 'application/json'}
data = {}
# r = requests.get(url, headers=header)
# print(r.text)

r = requests.post(url, data, headers=header)
print(r.text)


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     for i in range(20):
#         print(i)
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
