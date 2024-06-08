a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i) == 5 and 'o' in i]
print(b)