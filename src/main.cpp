#include"formatter/formatter.cpp"
#include<iostream>
#include<string>
std::string csvteststring = "2021-09-20 10:00:00+00:00¤2021-09-20 11:30:00+00:00¤Idrott och hälsa 1 ¤Don Magnusson - Uppstart friluftsliv uppgift, grupper om 3 personer Ställ upp stolarna, salen ska städas. ¤211";
std::string s = format("start", csvteststring);
std::string e = format("end", csvteststring);
std::string t = format("subject", csvteststring);
std::string c = format("teacher", csvteststring);
std::string g = format("agenda", csvteststring);
std::string u = format("classroom", csvteststring);
int main() {
	std::cout << s << std::endl;
	std::cout << e << std::endl;
	std::cout << t << std::endl;
	std::cout << c << std::endl;
	std::cout << g << std::endl;
	std::cout << u << std::endl;
}

