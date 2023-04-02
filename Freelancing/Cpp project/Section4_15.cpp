#include <iostream>
#include <iomanip>
using namespace std;
int main() {
 int n;
 int sum=0;
 float avg=0;
 int max=0;
 int number=0 ;
 while(true){
    cin>>n;
    
    
    if(n<0){
        break;
    }
    if(max<n){
        max=n;
    }
    sum=sum+n;
    number = number+1;
 }
 avg = sum/number;
 cout<<max<<" "<<setprecision(3)<<avg<<"\n";
 return 0;
}