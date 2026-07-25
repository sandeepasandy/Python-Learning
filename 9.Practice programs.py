'''1.Tables
table_=int(input('Enter a num: '))
for j in range(1,11):
    print(f'{table_} x {j} = {table_*j}')
2.153 = 1**3 + 5**3 + 3**3 Armstrong
num = int(input('enter a number: '))
length_ =len(str(num))
am_= 0
for j in str(num):
    am_ = int(j) ** length_ + am_
if am_ == num:
    print(f'{num} is armstrong')
else:
    print(f'{num} is not armstrong')
3.Fibbnocci series:
limit_ = int(input('Enter limit: '))
num = 0
num_2 = 1
print(num,num_2,end=' ')
for j in range(1,limit_+1):
    all_add = num + num_2
    num = num_2
    num_2 = all_add
    print(all_add,end=' ')
4.Calculator:
num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))
opt_ = int(input('Enter \n1.Add \n2.subtract \n3.multiply \n4.division : '))
if opt_ == 1:
    print(num_1 + num_2)
elif opt_ == 2:
    print(num_1 - num_2)
elif opt_ == 3:
    print(num_1 * num_2)
elif opt_ == 4:
    print(num_1 % num_2)
5.ATM:'''
SBI_Sandeepa = {'name' : 'Sandeepa',
                'Adr' : "1356897",
                'Pan' : 'gh565httdb',
                'ATM PIN' : '1212',
                'Balance' : 45000}
remain_A = 3
while remain_A > 0:
    pin_ = input("Enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in SBI_Sandeepa['ATM PIN']:
            opt_ = int(input('Enter \n1.Withdraw \n2.Deposite \n3.Balance: '))
            if opt_ == 1:
                Withdraw_m = int(input('Enter the amount to Withdraw: '))
                if Withdraw_m <=  SBI_Sandeepa['Balance'] and Withdraw_m % 100 == 0:
                     SBI_Sandeepa['Balance'] -= Withdraw_m
                     print(f"you have withdraw {Withdraw_m} and the total balance is {SBI_Sandeepa['Balance']}")
                     break
                else:
                    print('Can not provide change or no balance')
                    break
            elif opt_ == 2:
                pass
            elif opt_ == 3:
                pass
            else:
                remain_A -=1
            if remain_A > 0:
                print(f'Incorrect pin you have only {remain_A}')
            else:
                print('Card is block')
                break
    else:
        print('Please enter 4 digit atm pin')


















