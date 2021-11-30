#include <stdlib.h>
#include <string>
#include <cstring>

using namespace std;

string cal2arr(string user){
    FILE *ics;
    char line[100];
    string arr[10000];
    ics = fopen("%s.ics" user, "r");
    if (ics == NULL)
        return "E[crit][cal2arr] - File open error, " + user;
    while (fgets(line, sizeof(line), ics) != NULL)
    {
        char *separator;
        char *key;
        char *tail;
        char *value;

        if ((tail = strchr(line, '\n')) != NULL)
            *tail = '\0'; // Remove the trailing '\n'
        separator = strpbrk(line, ":;");
        if (separator == NULL)
            continue;
        *separator = '\0';

        key = line; // Maybe you want to strip surrounding white spaces
        value = separator + 1; // Maybe you want to strip surrounding white spaces

	//for loop goes here that scans through
	while( key != BEGIN ){
	
		for (int i; i<10000){
			arr[i][1] = key;
			arr[i][2] = value;
			i++;
		}
	}

        fprintf(stdout, "%s --> %s\n", key, value);
    }
    fclose(ics);
}


int main(void)
{
    FILE *ics;
    char line[100];

    ics = fopen("example.ics", "r");
    if (ics == NULL)
        return -1;
    while (fgets(line, sizeof(line), ics) != NULL)
    {
        char *separator;
        char *key;
        char *tail;
        char *value;

        if ((tail = strchr(line, '\n')) != NULL)
            *tail = '\0'; // Remove the trailing '\n'
        separator = strpbrk(line, ":;");
        if (separator == NULL)
            continue;
        *separator = '\0';

        key = line; // Maybe you want to strip surrounding white spaces
        value = separator + 1; // Maybe you want to strip surrounding white spaces

        fprintf(stdout, "%s --> %s\n", key, value);
    }
    fclose(ics);

    return 0;
}

// if it occurs, BEGINVEVENT, then iterate counter in 2d array for second dimension
//
