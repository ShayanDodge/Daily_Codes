# include<iostream>
# include<cmath>
# include<iomanip>
using namespace std;

int main()
{
    double price, limit;
    limit = 128;
    cout << "please enter the total prce = ";
    cin >> price;

    if (price < limit)
    {
        cout << "the total price after discount is " << price - (0.08 * price);
    }
    else
    {
        cout << "the total price after discount is " 
        << (128 - (0.08 * 128)) + ((price-128) - (0.16 * (price-128)));
    }
    return 0;
}