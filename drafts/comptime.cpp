#include<stdio.h>
#include<fstream>
#include<iostream>
#include <chrono>  // chrono::system_clock
#include <ctime>   // localtime
#include <sstream> // stringstream
#include <iomanip> // put_time
#include <string>  // string
using std::string;
using std::cout;
using std::endl;

string fullLine;

//        		string myArray[6];
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
		std::ifstream csvF((csvfile).c_str());
		if( !csvF.is_open()){
          		cout << "E[crit] [comptime] - Input file failed to open" << endl;
    		}
		string line;
		std::getline(csvF, line);
		int len = line.length();
		if (loglevel == 1) { 
			cout << "L[nmal] [comptime] - Successfully opened, read and stored time of row 1: " << line << " Proceeding..." << endl;
		}

		// we need to add a constant here to make sure that we can still return the line that is passed to log, as it is what our wanted return value is.
		fullLine = line;
		line.erase(25, len);
    		/*if(csvF.is_open()){    			// i <3 ctrlc ctrlv

        		for(int i = 0; i < 6; ++i){
            			csvF >> myArray[i];
        		}
    		}*/



		int len1 = line.length();
		line.erase(len1 - 9, len1);
		string currTime = rtime();
		int len2 = currTime.length();
		currTime.erase(len2 - 9, len2); 		//cout << currTime << " | " << line << endl;
		
								//cout << fullLine << endl;
		if (line.compare(currTime) == 0){		//cout << currTime << " | " << line << endl;
			
			return fullLine;
		}
		else if (line.compare(currTime) == 1){
			return 0;
		}
		else {
			return fullLine;
		}


		


	}
	catch (const std::exception& e) {
		cout << "E[expt][comptime] - Throwed exception: " << e.what() << endl;
	}
}


