#include <iostream>
#include "urltojson.cpp"

using namespace std;
int main(){
cout << urltojson("https://schoolity.com/icalendar?id=2f1695b15cdc8bd0329656e44ca407ff2070f5740f1b0f458d01961bda23a247") << endl;
return 0;
}
