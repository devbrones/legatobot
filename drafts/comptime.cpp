#include<stdio.h>
#include<string>
#include<chronos>
#include<iostream>
#include <chrono>  // chrono::system_clock
#include <ctime>   // localtime
#include <sstream> // stringstream
#include <iomanip> // put_time
#include <string>  // string
using std::string;
using std::cout;
using std::endl;

string rtime()
{
    auto now = std::chrono::system_clock::now();
    auto in_time_t = std::chrono::system_clock::to_time_t(now);

    std::stringstream ss;
    ss << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d %H:%M:%S+00:00");
    return ss.str();
}


string comptime(std::string aux) {
	try{
		string csvfile = aux.append(".csv");
		if (loglevel == 1) {
			cout << "L[nmal] [comptime] - Successfully appended file extension: "<< aux << " became " << csvfile << endl;
		}
		std::fstream csvF(csvfile);
		string line = getline(csvF,1);
		int len = line.length();
		line.erase(25, len);
		if (loglevel == 1) { 
			cout << "L[nmal] [comptime] - Successfully opened, read and stored time of row 1: " << line << " Proceeding..." << endl;
		}


	}
	catch (const std::exception& e) {
		cout << "E[expt] - " << e.what() << endl;
	}
}


