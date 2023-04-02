#include <iostream>
#include <string>
using namespace std;
int main() {
 char ch;
 string str;
 cin>>ch;
 cin>>str;
 int number = 0;
 for (int i = 0; i < str.size(); i++)
    {
        if (str[i] ==  ch)
        {
            ++ number;
        }
    }
    if(number == 1){
        cout<<number<<ch<<"\n";
    }
    else{
        cout<<number<<ch<<"'s\n";
    }
 return 0;

}