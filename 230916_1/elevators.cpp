# include<iostream>
using namespace std;

int main()
{
    int floor, actual_floor;
    cout << "please enter the number of foor = ";
    cin >> floor;
    cout << "actual floor : "<< (floor>13 ? floor-1 : floor);


    // if (floor > 13)
    // {
    //     actual_floor = floor - 1;
    // }
    // else
    // {
    //     actual_floor = floor;
    // }
    // cout << "the elevator will travel to the " << actual_floor;
    return 0;
}