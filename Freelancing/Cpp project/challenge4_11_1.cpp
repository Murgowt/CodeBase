#include<iostream>

using namespace std;

int main(){
    enum GroceryItem {GR_APPLES, G_BANANAS, GR_JUICE, GR_WATER};
    GroceryItem userItem;
    userItem = GR_APPLES;
    if(userItem == GR_APPLES || userItem == G_BANANAS ){
        cout<<"Fruit\n";
    }
    else if(userItem == GR_JUICE || userItem == GR_WATER){
        cout<<"Drink\n";
    }
    return 0;
}