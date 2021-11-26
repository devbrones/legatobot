#include <iostream>
#include "unturl.cpp"

std::string cookie = "-H 'cookie: _ga=GA1.2.390327794.1637258232; _fbp=fb.1.1637258231838.1225661349; _gid=GA1.2.1715846975.1637828973; server-version=20211123t152509.439610736658047658; light=no; _gat=1; JSESSIONID=EbkWp6--6VbfkwJH6B_SXw; login-provider=google; session-email=21jogudm@mediagymnasiet.se'";
int main(){
	std::cout << usertourl("21jogudm", cookie) << std::endl;
}
