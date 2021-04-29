#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define NUMBER_WAIT_INTERVAL 5
 
int main(void)
 {
  void sigint_handler(int sig); //to get the prompt command if press CTRL+C
  char X[200]; //input string

	if(signal(SIGINT, sigint_handler) == SIG_ERR)
	{
	perror("signal");
	}

		int pipefds[2], buffer;

		if(pipe(pipefds) == -1)
		{
			perror("pipe");
			exit(EXIT_FAILURE);
		}

		int x, flag=0; //X is the input for user in integer.

		printf("Please enter a number is it a prime number or not:\n");
		scanf("%d",&x);

		printf("Writing number to the parent...\n");
		write(pipefds[1], &x, sizeof(x));

		sleep(NUMBER_WAIT_INTERVAL); //create a delay between process

		printf("Ok it Done!.\n\n");

		printf("Reading number from Child...\n");
		read(pipefds[0], &buffer, sizeof(buffer));

		sleep(NUMBER_WAIT_INTERVAL);
		
		printf("Done.\n\n");

		if((buffer>0)&&((buffer==1)||(buffer%2==0)))
		{
			printf("%d is not a prime number.\n",buffer);
			flag=1;
		}

		else if((buffer>0)&&(buffer%2!=0))
			{
			  printf("%d it is a prime number.\n",buffer);
			  flag=0;
			}

			else
			{
			  printf("I think there is error in your Code.\n");
			}


		return 0;
	}


   void sigint_handler(int sig)
{
	printf("Sabo lah kejap jangan duk tekan CTRL+C tu!!!!.\n");
  	EXIT_SUCCESS;
}
