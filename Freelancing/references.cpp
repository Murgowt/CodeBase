#include<iostream>
#include<string>
using namespace std;

//Function to decode the code
bool toASCII(string code,int &num1,int &num2, int &num3)
{
    // if the code is not of 9 character length, return false
    if(code.length()!=9){
        return false;
    }
    //for the first three characters, add value to num1, for next 3 characters, add to num2 and the last 3 characters are added to num3
    for(int i=0;i<code.length();i++){
        int value = int(code.at(i));
        if(i<3){
            num1= num1+value;
        }
        else if(i<6){
           num2= num2+value;
        }
        else{
            num3=num3+value;
        }
    }
    return true;
}

int main(){
    // Get the code input
    cout<<"Enter a sequence to decode"<<endl;
    string code;
    cin>>code;
    int num1=0,num2=0,num3=0;
    //Call the function to validate and decode the code
    if(toASCII(code,num1,num2,num3)){
    cout<<"Your sequence decoded is"<<endl;
    cout<<"Num1 = "<<num1<<endl;
    cout<<"Num2 = "<<num2<<endl;
    cout<<"Num3 = "<<num3<<endl;
    }
    else{
        cout<<"Invalid sequence.";
    }
    

    return 0;
}