#include <iostream>

using namespace std;

int main(){
    int amount;
    cin>> amount;
    int quaters, dimes, dollars, pennies, nickel;
    if(amount<=0){
        cout<<"No change\n";
    }
    else{
        dollars = amount/100;
        if(dollars>0){
            if(dollars==1){
                cout<<"1 Dollar\n";
            }
            else{
                cout<<dollars<<" Dollars\n";
            }
            amount = amount-dollars*100;
        }

        quaters =amount/25;
        if(quaters>0){
            if(quaters==1){
            cout<<"1 Quarter\n";
            }
            else{
                cout<<quaters<<" Quarters\n";
            }
            amount = amount-25*quaters;
        }
        
        dimes = amount/10;
        if(dimes>0){
            if(dimes==1){
                cout<<"1 Dime\n";
            }
            else{
                cout<<dimes<<" Dimes\n";
            }
            amount = amount-10*dimes;
        }

        nickel = amount/5;
        if(nickel>0){
            if(nickel ==1){
                cout<<"1 Nickel\n";
            }
            else{
                cout<<nickel<<" Nickels\n";
            }
            amount = amount -nickel*5;
        }

        pennies = amount;
        if(pennies>0){
            if(pennies==1){
                cout<<"1 Penny\n";
            }
            else{
                cout<<pennies<<" Pennies\n";
            }
        }
    }
    return 0;
}