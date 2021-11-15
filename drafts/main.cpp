int loglevel = 1;
#include"comptime.cpp"
#include<iostream>
#include"formatter.cpp"
#include<string>

std::string sb = format("subject",comptime("don"));
std::string st = format("start",comptime("don"));
std::string et = format("end",comptime("don"));
std::string tc = format("teacher",comptime("don"));
std::string ag = format("agenda",comptime("don"));
std::string cs = format("classroom",comptime("don"));


int main(){
	std::cout << "L[NMAL] [main] - Subject: " << sb << endl;
	std::cout << "L[NMAL] [main] - Start Time: " << st << endl;
	std::cout << "L[NMAL] [main] - End Time: " << et << endl;
	std::cout << "L[NMAL] [main] - Teacher: " << tc << endl;
	std::cout << "L[NMAL] [main] - Agenda: " << ag << endl;
	std::cout << "L[NMAL] [main] - Classroom: " << cs << endl;
}
