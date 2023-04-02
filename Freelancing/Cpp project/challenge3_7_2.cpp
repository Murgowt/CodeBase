#include <iostream>

using namespace std;

int main(){
    int myMoney;

    cin >> myMoney;
    if(myMoney>=20){
        cout<<"Buy new shoes."<<endl;
    }
    if(myMoney>=25){
        cout<<"Buy a new coat."<<endl;
    }
    
    if (myMoney<=1){
        cout<<"Save money."<<endl;
    }
    return 0;

}
