#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> //include <unistd.h> for unix systems only.

int vm_score = 0;

void number_of_cores();
void run_command();
void registry_check();

int main(int argc, const char * argv[]) {
    /*run number_of_cores() function first, 
    as it runs on both windows and unix machines.
    */
    number_of_cores();
  
  //run the dmesg command and pipe to find hypervisor, 34 is how long string should be.
    run_command("dmesg |grep -i hypervisor", "[   0.000000 Hypervisor detected]", 34);
    
    //run dmidecode command and find system manufacturer, 6 is how long the string should be.
    run_command("sudo dmidecode -s system-manufacturer", "VMware", 6);
    
    /*If vm_score is less than 3, we are likely running on physical hardware*/
    if(vm_score < 3){
      printf("No virtual machine detected");
    }

    printf("Virtual Machine detected.");
  
    return 0;
}

void number_of_cores() {
      //run sysconf function outlined in the man pages.
    if(sysconf(_SC_NPROCESSORS_ONLN) <= 1){
        //check if number of processors is less than or equal to one. If it is,
        //we assume virtual, and increment vm_score by 1.
        vm_score++;
    }
}

void run_command(char *cmd, char *detphrase, int dp_length){
    #define BUFSIZE 128
    char buf[BUFSIZE];
    FILE *fp;

    /*popen() is essentially the same as system()
    but it saves the output to a file. If the output
    is null, the command didn't work.
    */
    if((fp = popen(cmd, "r")) == NULL){
        printf("Error");
    }

    
    if(fgets(buf, BUFSIZE, fp) != NULL){
        char detection[(dp_length +1 )]; //one extra char for null terminator
        strncpy(detection, detphrase, dp_length);
        detection[dp_length] = '\0'; //place the null terminator

        if(strcmp(detphrase, detection) == 0){ //0 means detphrase = detection
            vm_score++; //increment the vm_score variable.
        }
    }

    if(pclose(fp)){
        printf("Command not found or exited with error status \n");
    }
}
