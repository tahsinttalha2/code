#include <iostream>

using namespace std;

class Addition {
    int a, b;

public:
    // default constructor
    Addition() {
        a = 0;
        b = 0;
    }

    // parameterized constructor
    Addition(int real, int imaginary) {
        a = real;
        b = imaginary;
    }

    Addition operator+ (Addition c) {
        Addition temp;
        temp.a = a + c.a;
        temp.b = b + c.b;

        return temp;
    }

    void display() {
        cout << a << " + " << b << "j" << endl;
    }
};

int main()
{
    Addition num1(1, 2);
    Addition num2(3, 4);
    Addition num3;

    num3 = num1 + num2;

    cout << "num1: "; num1.display();
    cout << "num2: "; num2.display();
    cout << "num3: "; num3.display();
}