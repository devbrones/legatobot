#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

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
      if (fgets(buffer, max_buffer, stream) != NULL) data.append(buffer);
    pclose(stream);
  }
  return data;
}

string usertourl(const string user, const string cookie){
	string out = exec("curl -s 'https://schoolity.com/rpc?method=encrypt' -H 'content-type: text/x-gwt-rpc; charset=UTF-8' -H 'namespace: MediaGymnasiet' -H 'x-gwt-permutation: 6C70D254A3DFC8B28CD4A45AC1B3D654' -H 'accept: */*' "+ cookie +" --data-raw '7|0|6|https://schoolity.com/appimpl/|0000000000000000000000000000000|schoolutil.client.RPCService|encrypt|java.lang.String/2004016611|"+ user +"@mediagymnasiet.se|1|2|3|4|1|5|6|' --compressed");
	out.erase(0,9);
	out.erase(64, 70);
	string url = "https://schoolity.com/icalendar?id=" + out;
	return url;
}
