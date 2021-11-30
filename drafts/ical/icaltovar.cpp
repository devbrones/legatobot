#include <stdlib.h>
#include <string.h>

int
main(void)
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
