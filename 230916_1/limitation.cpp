# include<iostream>
# include<cmath>
# include<iomanip>
using namespace std;

int main()
{
    double r = sqrt(2.0);
    if (r * r == 2.0)
    {
        cout << "sqrt(2) * sqrt(2) = 2";
    }
    else
    {
        cout << "sqrt(2) * sqrt(2) != 2 but is " << setprecision(18) << r * r << endl;
    }
    return 0;
}