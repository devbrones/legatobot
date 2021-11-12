int loglevel = 1;
#include"comptime.cpp"
#include<iostream>
#include<string>
std::string cs = comptime("don");

int main(){
	std::cout << cs << endl;
}
