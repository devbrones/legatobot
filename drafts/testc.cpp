#include<string>
#include<iostream>

using std::string;

string subject = "Svenska 1";
string start = "15:20" ;
string end = "16:15" ;
string teacher = "Hanna Åberg" ;
string classroom = "312" ;
string delimiter;

int main(){

	
	subject.append(" |");
	start.append(" |");
	end.append(" |");
	teacher.append(" |");
	classroom.append(" |\n");
	subject.insert(0,"| ");
	start.insert(0,"| ");
	end.insert(0,"| ");
	teacher.insert(0,"| ");
	classroom.insert(0,"| ");

	int x;

	string length;

	length.append(subject);
	length.append(start);
	length.append(end);
	length.append(teacher);
	length.append(classroom);
	std::cout << length.length() << "\n";

	for (x=0;x<=length.length()+1;) {
		delimiter.append("≡");
		x++;
	}
	std::cout << " "<< delimiter << "\n";
	
	string wtable[5][5] = {  {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} };
	int i,j;
	
	for(i=0;i<5;i++) {
		for(j=0;j<5;j++) {
			std::cout << " " <<wtable[i][j];
		}
		std::cout << " " << delimiter << "\n";	
	}
	return 0;

}
