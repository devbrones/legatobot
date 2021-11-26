#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>
#include <fstream>
using namespace std;

string exec(string cmd) {

  string data;
  FILE * stream;
  const int max_buffer = 256;
  char buffer[max_buffer];
  cmd.append(" 2>&1");
  stream = popen(cmd.c_str(), "r");

  if (stream) {
    while (!feof(stream))
      if (fgets(buffer, max_buffer, stream) != "") data.append(buffer);
    pclose(stream);
  }
  return data;
}

string get(const string url, const string name){
	string out = exec("curl -s " + url);
	string filename = name + ".ics";
	ofstream file;
	file.open(filename, ios::app);
	file.seekp(0,std::ios::end); //to ensure the put pointer is at the end
	file<<out;
	file.close();
	return "err";
}
