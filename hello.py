print('*' * 100)
print('ATM Machine')
print('Use this ATM machine where you can deposit and withdraw money.')
print('*' * 100)
print(' ')


#define variables
class Account:
    checkingValue = 500
    savingsValue = 1000
    selectedAccount = ''

    def get_checkingValue(self):
        return self.checkingValue

    def set_checkingValue(self, x):
        self.checkingValue = x

    def get_savingsValue(self):
        return self.savingsValue

    def set_selectedAccount(self, x):
        self.selectedAccount = x
        print('account set to: {}'.format(self.selectedAccount))

    def get_selected_account(self):
        print('test entry: ')
        test_ = input()
        return test_

    def Withdraw(self, amount):
        if(self.selectedAccount == 'checking'):
            self.checkingValue-=amount
            print('amount left in {}: {}'.format(self.selectedAccount,self.checkingValue))
        elif(self.selectedAccount == 'savings'):
            self.savingsValue-=amount
            print('amount left in {}: {}'.format(self.selectedAccount,self.savingsValue))

    def Select_Account(self):
        print('Which account would you like to access?')
        print('Enter 1 for checking. Enter 2 for savings.')
        print('Select your account: ')
        accountType = int(input())
        if(accountType == 1):
            self.selectedAccount = "checking"
            print("you selected {} account".format(self.selectedAccount))
        elif(accountType == 2):
            self.selectedAccount = "savings"
            print('you selected {} account'.format(self.selectedAccount))
        else:
            print('you entered something invalid. nice.')

    def Get_PIN(self):
        print('Enter your PIN: ')
        pin = input()
        if(pin == '1234'):
            print('success')
        else:
            print('Fail')


#print('this is what i got: ' + str(acct.get_checkingValue()))

acct = Account()

acct.Get_PIN()
acct.Select_Account()
acct.Withdraw(1)
