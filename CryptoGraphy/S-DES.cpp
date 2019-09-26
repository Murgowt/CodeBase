#include<iostream>
#include<string>
using namespace std;
string xor_gate(string temp2,string key1,int n)
{
	string key=temp2,bools;
	bools.assign("10");
	for(int i=0;i<n;i++)
	{
		if(temp2[i]!=key1[i])
		key[i]=bools[0];
		else
		key[i]=bools[1];
	}
	return(key);
}
int position(string t)
{
	if(t=="00")
	return 0;
	else if(t=="01")
	return 1;
	else if(t=="10")
	return 2;
	else if(t=="11")
	return 3;
}
string Data(int i)
{
	switch (i)
	{
		case 0:
			{
				return "00";	
			}
		case 1:
			{
				return "01";
			}
		case 2:
			{
				return "10";	
			}
		case 3:
			{
				return "11";	
			}			
	}
}
string sbox(int s[][4],string temp)
{
	
	string key,tempo="  ";
	int row,col;
	tempo[0]=temp[0];tempo[1]=temp[3];
	row=position(tempo);
	tempo[0]=temp[1];tempo[1]=temp[2];
	col=position(tempo);
	key=Data(s[row][col]);
	return(key);
}
void SDES(string plain,string key1,string key2)
{
	

	//Initial Declarations
	int i,IP[8]={2,6,3,1,4,8,5,7},EP[8]={4,1,2,3,2,3,4,1},p4[4]={2,4,3,1},INV[8]={4,1,3,5,7,2,8,6};
	string temp=plain;
	
	//   IP
	for(i=0;i<8;i++)
	{
		plain[i]=temp[IP[i]-1];
	}
	cout<<"   Initial Permutations :"<<plain<<endl;
	string temp1=plain.substr(0,4);
	string temp2=plain.substr(4,8);
	temp=temp2;
	cout<<endl<<"Round-1"<<endl;
	//  EP
	temp2.resize(8);
	for(i=0;i<8;i++)
	{
		temp2[i]=temp[EP[i]-1];
	}
	cout<<endl<<"   E/P output: "<<temp2<<endl;
	// XOR-temp2 & Key
	temp2=xor_gate(temp2,key1,8);
	cout<<"   Xor with Key output: "<<temp2<<endl;
	//S-Box
	string temp2_1=temp2.substr(0,4);
	string temp2_2=temp2.substr(4,8);
	int s0[4][4]={{1,0,3,2},{3,2,1,0},{0,2,1,3},{3,1,3,2}};
	int s1[4][4]={{0,1,2,3},{2,0,1,3},{3,0,1,0},{2,1,0,3}};
	temp2_1=sbox(s0,temp2_1);
	temp2_2=sbox(s1,temp2_2);
	temp2=temp2_1+temp2_2;
	
	//  P4
	string temperoroy;
	temperoroy=temp2;
	for(i=0;i<4;i++)
	{
		temp2[i]=temperoroy[p4[i]-1];
	}
	cout<<"   P4 output: "<<temp2<<endl;
	//   XOR
	temp2=xor_gate(temp2,temp1,4);
	//SWAP
	temperoroy=temp;
	temp=temp2;
	temp2=temperoroy;
	//cout<<"temp2 "<<temp2<<endl;
	string temp_r2;
	temp_r2=temp;
	temp.resize(8);
	cout<<endl<<"Round-2! "<<endl;
	//   EP
	for(i=0;i<8;i++)
	{
		temp[i]=temp_r2[EP[i]-1];
	}
	cout<<endl<<"   E/P output: "<<temp<<endl;
	// XOR with Key
	temp=xor_gate(temp,key2,8);
	cout<<"   Xor with Key output: "<<temp<<endl;
	string temp_l=temp.substr(0,4),temp_r=temp.substr(4,8);
	// S-Box 
	temp_l=sbox(s0,temp_l);
	temp_r=sbox(s1,temp_r);
	temp=temp_l+temp_r;
	temperoroy=temp;
	// P4 
	for(i=0;i<4;i++)
	{
		temp[i]=temperoroy[p4[i]-1];
	}
	cout<<"   P4 output: "<<temp<<endl;
	//cout<<"temp2 "<<temp2<<endl;
	temp2=xor_gate(temp2,temp,4);
	
	string cipher=temp2+temp_r2;
	temperoroy=cipher;
	for(i=0;i<8;i++)
	{
		cipher[i]=temperoroy[INV[i]-1];
	}
	cout<<endl<<"Result : "<<cipher;
}
string ls(string key,int s,int n);
string ls(string key,int s,int n)
{
	int i,l;
	for(l=0;l<s;l++)
	{
		int temp=key[i];
		for(i=0;i<n-1;i++)
		{
			key[i]=key[i+1];
		}
		key[n-1]=temp;
	}
	return(key);
}
int main()
{
//Key Generation
	//Initial Declarations
	string key,key1;
	int i,p10[10]={3,5,2,7,4,10,1,9,8,6},p8[8]={6,3,7,4,8,5,10,9};
	cout<<"Enter the Key: ";
	cin>>key;
	string temp=key;
	//Applying P10 permutations
	for(i=0;i<10;i++)
	{
		key[i]=temp[p10[i]-1];
	}
	//Left-Shift-1
	string temp1=ls(key.substr(0,5),1,5);
	string temp2=ls(key.substr(5,10),1,5);
	key1=temp1+temp2;
	temp=key1;
	//Applying P8 permutations
	for(i=0;i<10;i++)
	{
		key1[i]=temp[p8[i]-1];
	}	
	key1=key1.substr(0,8);
	cout<<"Generating Keys..."<<endl;
	string key2;
	//Left-Shift-2
	string temp3=ls(temp1,2,temp1.length());
    cout<<"Key1 Generated!"<<endl;
	string temp4=ls(temp2,2,temp2.length());
	key2=temp3+temp4;
	temp=key2;
	//Applying P8 permutations
	for(i=0;i<8;i++)
	{
		key2[i]=temp[p8[i]-1];
	}
	key2=key2.substr(0,8);
	cout<<"Key2 Generated!"<<endl;
//	cout<<key1<<endl<<key2;
//Keys Generated.

//Encryption
	int choice;
	cout<<"1.Encrypt\n2.Decrypt\nEnter your Choice:";
	cin>>choice;
	string plain,cipher;
	switch(choice)
	{
		case 1:
			{
				cout<<"Enter the Plain Text: ";
				cin>>plain;
				SDES(plain,key1,key2);
				break;
			}
		case 2:
			{
				cout<<"Enter the Cipher Text: ";
				cin>>cipher;
				SDES(cipher,key2,key1);
				break;
			}	
	}
}
