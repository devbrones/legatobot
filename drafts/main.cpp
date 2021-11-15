int loglevel = 1;
#include"comptime.cpp"
#include<iostream>
#include"formatter.cpp"
#include<string>
std::string cs = format("classroom",comptime("don"));

int main(){
	std::cout << cs << endl;
}
