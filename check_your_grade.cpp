#include <iostream>
using namespace std;
int main ()
{
    int score;
    string name;
    string matric;
    string course;
    cout << "Determine the Grade of a student in a particular course" << endl;
    cout << "enter you name: ";
    getline (cin, name);
    
    cout << "enter your matric number";
    getline (cin, matric);

    cout << "enter your course code";
    getline (cin, course);

    cout << "enter your score";
    cin << score;

    if (score >=70 && score <=100)
    {
        cout >> "your grade is A";
    }
    else if (score >=60 && score <=69)
    {
        cout >> "your grade is B";
    }
    else if (score >=50 && score <=59)
    {
        cout >> "your grade is C";
    }
    else if (score >=40 && score <=49)
    {
        cout >> "your grade is D";
    }
    else if (score >=30  && score <=39)
    {
        cout >> "your  grade is E";
    }
    else if (score >=0 && socre <=29)
    {
        cout >> "your grade is F";
    }
    else 
    {cout >> "oops! invalid input"}
    return 0;
}