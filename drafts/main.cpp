int loglevel = 0;
#include"comptime.cpp"
#include<iostream>
#include"formatter.cpp"
#include<string>

std::string b = comptime("don");


std::string sb = format("subject",fullLine);
std::string st = format("start",fullLine);
std::string et = format("end",fullLine);
std::string tc = format("teacher",fullLine);
std::string ag = format("agenda",fullLine);
std::string cs = format("classroom",fullLine);


int main(){
	std::cout << "L[NMAL] [main] - Subject: " << sb << endl;
	std::cout << "L[NMAL] [main] - Start Time: " << st << endl;
	std::cout << "L[NMAL] [main] - End Time: " << et << endl;
	std::cout << "L[NMAL] [main] - Teacher: " << tc << endl;
	std::cout << "L[NMAL] [main] - Agenda: " << ag << endl;
	std::cout << "L[NMAL] [main] - Classroom: " << cs << endl;
}
