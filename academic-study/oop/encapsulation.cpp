#include <iostream>

using namespace std;

class bank_account
{
    private:
    double balance = 0;

    public:
    double deposit(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
        }
        return balance;
    }
};