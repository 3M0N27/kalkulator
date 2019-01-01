
# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";


print ""
print ""
print R+"Kalkulator by Mr.3M0N27"
print R+"Semoga Membantu ea:v"
print W+"btw belajar menghitung dengan rajin ea:v biar pinter:v"
print G+"Okehh langsung saja"
print R+"      ------"
print G+"      |    |"
print G+"      |    |"
print R+"      |    |"
print R+" -- ---    ---- ---"
print G+"  \              /"
print G+"   \ Mr. 3M0N27 /"
print R+"    \          /"
print R+"     \        /"
print G+"      \      /"
print G+"       \    /"
print B+"        \  /"
print B+"         \/"
print R+"Mr. 3M0N27"

print ""

print "kalkulator"
# fungsi penjumlahan
def add(x, y):
   return x + y
# fungsi pengurangan
def subtract(x, y):
   return x - y
# fungsi perkalian
def multiply(x, y):
   return x * y
# fungsi pembagian
def divide(x, y):
   return x / y
# menu oprasi
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# meminta input dari user
choice = input ("masukan pilihan(1/2/3/4): ")

num1 = int(input("Masukan bilangan pertama: "))
num2 = int(input("Masukan bilangan kedua: "))

if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
  print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 4:
  print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("input salah kamvank")
