/* ky033 tracking driver user_space program */

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

int main(){

        char Sen_status[2];
        int fd;
        printf("Start Sensing Line with ky033...\n");

        fd = open ("/dev/TracK", O_RDONLY);

        if (fd < 0){
                printf ("Failed to open device...\n");
                return errno;
        }

        while (1){

                read (fd, Sen_status, 1);

                if (Sen_status[0] == '1'){
                        printf ("WHITE LINE DETECTED\n");
                        sleep (1);
                }
                else {
                        printf ("..BLACK LINE DETECTED\n");
                        sleep (1);
                }
        }

        return 0;
}