#include <iostream>

using namespace std;
int main() {
 int highwayNumber;

 cin >> highwayNumber;
 if(highwayNumber<=0 || highwayNumber>999){
    cout<<highwayNumber<<" is not a valid interstate highway number.\n";
 }
 else{
    if(highwayNumber%100==0){
        cout<<highwayNumber<<" is not a valid interstate highway number.\n";
    }
    else{
        if(highwayNumber<100){
            if(highwayNumber%2==0){
                cout<<"I-"<<highwayNumber<<" is primary, going east/west.\n";
            }
            else{
                cout<<"I-"<<highwayNumber<<" is primary, going north/south.\n";
            }
        }
        else{
            int highway = highwayNumber%100;
            if(highway%2==0){
                cout<<"I-"<<highwayNumber<<" is auxiliary, serving I-"<<highway<<", going east/west.\n";
            }
            else{
                cout<<"I-"<<highwayNumber<<" is auxiliary, serving I-"<<highway<<", going north/south.\n";
            }
        }
    }
 }
 return 0;
}