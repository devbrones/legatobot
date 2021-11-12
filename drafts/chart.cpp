#include<iostream>
#include<iomanip>
#include"formatter.cpp"

using std::string;

string week(string type; int length; int style; ) {

	/*  +--------+--------+--------+--------+
	 *  |  CLASS |  TIME  | TEACHER| CLASRM |
	 *  +--------+--------+--------+--------+
	 *  
	 *  We want to generate these table structures, how? good question i dont know
	 *  In all seriousness there is a for loop in there somewhere.
	 *  
	 *  Im seriously concidering giving up on this cuz it be pain in the arse rn.
	 *  But im stronk :3
	 *
	 *
	 *
	 *
	 *
	 *  */
	

	int cols = ;
	if (subject) {cols++;}
	if (start) {cols++;}
	if (end) {cols++;}
	if (teacher) {cols++;}
	if (classroom) {cols++;}
	if (cols < 1) {
		std::cout << "E[crit] [chart] - No values passed to chart. Cant generate table, exiting." << std::endl;
	}
	else {
		std::cout << "L[nmal] [chart] - Values passed to chart, continuing..." << std::endl;
	}



	int rows; // oh no oh no, this causes the need to rewrite formatter, why may you ask? well because it needs to be passed how many classes there is in said day. This of course is easy to do using say a looper that loops through the day value and iterates a counter, say classes++. Then it stops when it stumbles upon a different day value (09 /= 10)
	if (style == 1) {
		std::cout << "L[nmal] [chart] - Style set to 1." << std::endl;
	}
	else if (style == 2) {
		std::cout << "L[nmal] [chart] - Style set to 2." << std::endl;
	}
	else {
		std::cout << "E[errr] [chart] - No style defined, assuming 1." << std::endl;
	}
	
	for () {}


}

string week( string type, int length, int style ) {
	
	string wtable[5][5] = {  {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {course,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} , {subject,start,end,teacher,classroom} }
	int i,j;
	
	for(i=0;i<5;i++) {
		for(j=0;j<5;j++) {
			std::cout << "\t" <<wtable[i][j];
		}
	}

	
}
