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
		if( !in.is_open()){
          		cout << "E[crit] [comptime] - Input file failed to open" << endl;
    		}
		string line = getline(csvF,1);
		int len = line.length();
		line.erase(25, len);
		if (loglevel == 1) { 
			cout << "L[nmal] [comptime] - Successfully opened, read and stored time of row 1: " << line << " Proceeding..." << endl;
		}

		/*
    		// now open temp output file
		std::ofstream out("outfile.txt");
    		// loop to read/write the file.  Note that you need to add code here to check
    		// if you want to write the line
    		while( getline(in,line) )
    		{
         		out << line << "\n";
    		}
    		in.close();
    		out.close();    
    		// delete the original file
		std::remove("infile.txt");
    		// rename old to new
		std::rename("outfile.txt","infile.txt");

		
		 * */


		int len1 = line.length();
		line.erase(len1 - 8, len1);
		string currTime = rtime();
		int len2 = currTime.length();
		currTime.erase(len2 - 8, len2);
		if (line.compare(currTime) == 0){
			
		}


		


	}
	catch (const std::exception& e) {
		cout << "E[expt] - " << e.what() << endl;
	}
}


