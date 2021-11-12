#include<string>
#include<iostream>

using std::string;

string subject = "Suedois 1";
string start = "15:20" ;
string end = "" ;
string teacher = "Ana Euberge" ;
string classroom = "312\n" ;
string delimiter = "+----------+";

int main(){


	
	string wtable[5][5] = {  {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} };
	int i,j;
	
	for(i=0;i<5;i++) {
		for(j=0;j<5;j++) {
			std::cout << "	" <<wtable[i][j];
		}
	}
	
	return 0;

}
