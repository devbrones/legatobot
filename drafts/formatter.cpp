#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <chrono>
std::string subject;
std::string start;
std::string end;
std::string classroom;
std::string teachers;
std::string agenda;
std::string url;
int len;
int found;

std::string a = "E[null] [formatter] - No Subject Found";	
/*
int SepFindPos(string &in) {
	for (int i = 0; i < strlen(in); i++)
	{
		char *position_ptr = strchr(in, in[i]);
		char *r_
	}
}
*/

std::string format(std::string self, std::string csvTmp) {
	if (loglevel == 1){
		std::cout << "L[nmal] [formatter] - Formatter initialized." << std::endl; // prints a init just so i can keep track of my own 3 braincells
		std::cout << "L[nmal] [formatter] - Formatter passed option: " << self << std::endl; // god help us all
		std::cout << "L[nmal] [formatter] - Formatter passed string: " << csvTmp << std::endl; // oh fuck
	}

	if (self == "start") {
		std::string csv = csvTmp.erase (0, 11);
		int len = csv.length();
		if (loglevel == 1){
			std::cout << "L[nmal] [formatter] - String length is: " << len << std::endl;
		}
//		std::cout << csv << std::endl;
		csv.erase(5, len); // remove guckies
//		std::cout << csv << std::endl;
		csv.replace(2, 1, ""); //remove guckies pt. 2 electric boogaloo
//		std::cout << csv << std::endl;
		std::stringstream timeIn(csv); // this is probably illegal in some countries but i do it anyways
		int timeInt;
		timeIn >> timeInt;
//		std::cout << timeInt << std::endl;
		int timePostInt = timeInt + 100; // i calibrated the compasses to offset for the anomaly
//		std::cout << timePostInt << std::endl;
		std::stringstream to;
		to << timePostInt;
		std::string tos = to.str();
		if (tos.length() < 4 ) {
			tos.insert(1, ":"); //insert that guckie baby, ooh yeeaa
		}
		else if (tos.length() == 4) {
			tos.insert(2, ":");
		}
		else {std::cout << "E[crit] [formatter] - invalid time" << std::endl;} // we have successfully broken the space time continuum
//		std::cout << tos << std::endl;
		return tos;
	}
	else if (self == "end") {
		std::string csv = csvTmp.erase (0, 38);
		int len = csv.length();
//		std::cout << len << std::endl;
//		std::cout << csv << std::endl;
		csv.erase(5, len);
//		std::cout << csv << std::endl;
		csv.replace(2, 1, "");
//		std::cout << csv << std::endl;
		std::stringstream timeIn(csv);
		int timeInt;
		timeIn >> timeInt;
//		std::cout << timeInt << std::endl;
		int timePostInt = timeInt + 100;
//		std::cout << timePostInt << std::endl;
		std::stringstream to;
		to << timePostInt;
		std::string tos = to.str();
		if (tos.length() < 4 ) { // time has a fuck, like the off!
			tos.insert(1, ":");
		}
		else if (tos.length() == 4) {
			tos.insert(2, ":");
		}
		else {std::cout << "E[crit] [formatter] - invalid time" << std::endl;} // it will break
//		std::cout << tos << std::endl;
		return tos;
/*		int len = csv.length();
		csv.erase(5, len);
		csv.replace(2, 3, "");
		std::stringstream timeIn(csv);
		int timeInt;
		timeIn >> timeInt;
		int timePostInt = timeInt + 200;
		std::stringstream to;
		to << timePostInt;
		return to.str(); */
	}
	else if (self == "subject") {
		std::string csv = csvTmp.erase (0, 54);
//		std::cout << csv << std::endl;
		int len = csv.length();
//		std::cout << len << std::endl;
		int found = csv.find("¤");
  		if (found!=std::string::npos){
			std::string subject = csv.erase(found, len);
//			std::cout << subject << std::endl;
			return subject;		
			}
		else {
			std::string a = "[E][NULL] [formatter] - No Subject Found";	
			return a;
		}
	}
	else if (self == "teacher") { // i love bindesstreck <3
		std::string csv = csvTmp.erase(0, 54);
		int found = csvTmp.find("¤");
		int len = csvTmp.length();
  		if (found!=std::string::npos){
			std::string psubj = csv.erase(0, found + 2);
			int at2 = psubj.find(" -");
			std::string posub = psubj.erase(at2,len);
//			std::cout << psubj << std::endl;
			return psubj;
		}
	}
	else if (self == "agenda") { // oh god, yes i realise this will break at some time
		int found = csvTmp.find (" - ");
		csvTmp.erase(0, found);
		csvTmp.erase(0, 3);
		int len = csvTmp.length();
		int f1 = csvTmp.find("¤");
		csvTmp.erase(f1 , len);
//		std::cout << csv << std::endl;
		return csvTmp;
	}
	else if (self == "classroom") { //this thing is so short and cute it makes my will to live look like empire state
		int len = csvTmp.length();
		csvTmp.erase(0, 80);
		int found = csvTmp.find("¤");
		csvTmp.erase(0, found+2);
		int l1 = csvTmp.length();
		csvTmp.erase(3,l1);
//		std::cout << csvTmp << std::endl;	
		return csvTmp;
	}



	return self;					/*[0:csvTmp.find(char '¤') - 1]*/
}
