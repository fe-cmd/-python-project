Store = []
def read_data(filename):
   lines = []
   data = []
   with open(filename,'r') as f:
      lines = f.read().splitlines()
   for line in lines:
     item = line.split(', ')
     item[0] = item[0].strip("'")
     item[1] = int(item[1].strip("'"))
     item[2] = int(item[2].strip("'"))
     data.append(item)
   return data
Store = read_data('data.csv')
#print Store
for item in Store:
	print(item)
	
name = str(input('pls enter name here:'))
print('you are welcome here' + name)
print('Choose Access\n1.Admin\n2.User\n3.Exit')

access = int(input('Enter a number:'))
if access == 1:
   print('ADMINS ACCESS\n1.display items\n2.set item price\n3.add items\n4.updates item\n5.return')
access_input = int(input('select a number:'))
if access_input == 5:
	print('Choose Access\n1.Admin\n2.User\n3.Exit')
	
user_item = int(input('Enter a number:'))
if user_item == 2:
   print('USER ACCESS\n1.display items\n2.buy items\n3.return')
elif user_item == 3:
   print('ACCESS CLOSED') 
user_item = int(input('Enter a number:'))
if user_item == 2:
	print('Do you wish to buy an item?\n1.yes\n.no')
user_choice = int(input('select your choice:'))
if user_choice == 1:
	print('WELCOME PLS VIEW ITEM LIST BELOW')
	def my_print():
         print('%1s %-30s %-10s %-10s' %('Id','items','quantity','price'))
         for I,item in zip(range(len(Store)),Store):
             print('{:<2d}{:<30}{:^10d}{:>10,.2f}'.format(I,*item))
    
my_print()

print('please select your needed items')
first_item = str(input('Enter item name here:'))
second_item = str(input('Enter item name here:'))
third_item = str(input('Enter item name here:'))
select_one =str(input('Do you wish to buy more?  (yes/no):'))
if select_one == 'yes':
	fourth_item = str(input('Enter item:'))
else:
	print('thank you, please log out.')
	
select_two =str(input('Do you wish to buy more item? (yes/no):'))
if select_two == 'yes':
	fifth_item = str(input('Enter item:'))
else:
	print('thank you!, you may log out')
print('you selected these items:' +first_item + second_item + third_item + fourth_item + fifth_item)
choice = str(input('(yes/no)?:'))
if choice == 'yes':
    print('pls input needed item quantity')

first_qty = str(input('Enter number of item needed:'))
second_qty = str(input('Enter number of item needed:'))
third_qty = str(input('Enter number of item needed:'))
fourth_qty = str(input('Enter number of item needed:'))
fifth_qty = str(input('Enter number of item needed:'))
print('you selected these item quantities:' + first_qty + second_qty + third_qty + fourth_qty + fifth_qty)
choice = str(input('(yes/no)?:'))
if choice == 'yes':
   print('Thank you for partnering with us @MAIADAMUIFERETAILSTORE, TRANSACTION SUCCESSFUL, kindly receive your receipt.')
else:
	print('kindly re-check item input again')
print("=======================================================")
print('MAI ADAMU IFE RETAIL STORE\nStock receipt')	
Stock = [
['Sugar',10,50,500], ['Bread(sliced)',2,200,400],['Egg',10,50,500],['Milo(tin)',2,500,1000],['Fanta(big)',20,150,3000],['TotalAmount[N]',1,2,5400]
]
def my_print():
         print('%1s %-22s %-10s %-2s %-3s' %('S/N','items','quantity','price[N]','amount[N]'))
         for I,item in zip(range(len(Stock)),Stock):
             print('{:<2d}{:<30}{:^5d}{:^5d}{:>10,.2f}'.format(I,*item))
    
my_print()
print('TOTAL AMOUNT[N] = 5400\n VAT = 1400  DISCOUNT(50%) = 2700 ')
print("=======================================================")


      
 
     
	
	

 