#include <iostream>
#include <stdexcept>
#include <string>
#include <stdio.h>



using namespace std;

//def getUrlFromUser(user):
//    proc=subprocess.Popen("curl -s 'https://schoolity.com/rpc?method=encrypt' -H 'content-type: text/x-gwt-rpc; charset=UTF-8' -H 'namespace: MediaGymnasiet' -H 'x-gwt-permutation: 6C70D254A3DFC8B28CD4A45AC1B3D654' -H 'accept: */*' -H 'cookie: _ga=GA1.2.390327794.1637258232; _fbp=fb.1.1637258231838.1225661349; light=yes; server-version=20211118t140346.439493461563813025; _gid=GA1.2.681735551.1637571736; JSESSIONID=OMm2FbvnVygYsdwakRPzdw; login-provider=google; session-email=21jogudm@mediagymnasiet.se' --data-raw '7|0|6|https://schoolity.com/appimpl/|0000000000000000000000000000000|schoolutil.client.RPCService|encrypt|java.lang.String/2004016611|"+ user +"@mediagymnasiet.se|1|2|3|4|1|5|6|' --compressed", shell=True, stdout=subprocess.PIPE, )
//    output=proc.communicate()[0]
//    url = "https://schoolity.com/icalendar?id=" + output[9:-7].decode('ascii')
//    print("Url for user: " + user + " is: " + url)
//    return url

string exec(string command) {
   char buffer[128];
   string result = "";

   // Open pipe to file
   FILE* pipe = popen(command.c_str(), "r");
   if (!pipe) {
      return "popen failed!";
   }

   // read till end of process:
   while (!feof(pipe)) {

      // use buffer to read and add to result
      if (fgets(buffer, 128, pipe) != NULL)
         result += buffer;
   }

   pclose(pipe);
   return result;
}


string user2cal(string userid, string format){
	if(userid == ""){
		cout << "E[crit][user2cal] - Null or invalid userid passed: " << userid << endl;
		return "E";
	}
	if (format == ""){
		cout << "E[crit][user2cal] - Null of invalid format passed: " << format << endl;
		return "E";
	}
	string outp = exec("ls");
	cout << outp;

}
