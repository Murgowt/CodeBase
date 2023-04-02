

#include <iostream>

using namespace std;

int main(){
    int toolcount;
    cin >> toolcount;
    if(toolcount<14){
         cout<<"Medium tool box"<<endl;
    }
    else if(toolcount>=14 && toolcount<=39){
        cout<<"Large tool box"<<endl;
    }
    else{
        cout<<"Too many for one box"<<endl;
    }
    return 0;

}