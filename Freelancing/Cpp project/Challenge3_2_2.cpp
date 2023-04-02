#include <iostream>

using namespace std;

int main(){
    int awardPoints;
    int userTickets;
    cin >> userTickets;
    if(userTickets==8){
        awardPoints = userTickets;
    }
    else{
        awardPoints = 10;
    }
    cout << awardPoints << endl;
    return 0;

}