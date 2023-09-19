# include<iostream>
# include<cmath>
# include<iomanip>
using namespace std;

int main()
{
    int mark;
    cout << "please enter your mark = ";
    cin >> mark;
    if (mark >= 90)
    {
        cout << "your grade is A." << endl;
    }
    else if(mark >= 75)
    {
        cout << "your grade is B." << endl;
    }
    else if(mark >= 65)
    {
        cout << "your grade is C." << endl;
    }
    else
    {
        cout << "your grade is F."<< endl;
    }
    return 0;
}