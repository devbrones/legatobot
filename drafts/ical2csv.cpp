#include<iostream>
#include<stdio>
#include<fstream>
using std::string;

string ical2csv(string calfile, string oname, int sort_type){
	
	string arr[10000];
	ifstream cal;
	cal.open(calfile, std::ios::app);
	if (cal.is_open()){
		while(!cal.eof() && i < 10000) {
			getline(cal, arr);
		}
		
	}

}

/*	Pseudocode:
 *	___________
 *
 *	Read all entries in the ical file, find different categories using regex searching. then load all entries into a 2d array format, {c1,c2,c3,c4,c5,c6}
 *	Then sort said entries after STTIME, and convert all entry prefixes to what we need to have in the csv
 *	then, using a for loop. print out the array to a file and change the name to $name$.csv
 */


