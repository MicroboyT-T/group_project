#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(void)
 {
  int pipefds[2];
  int buffer;

  if(pipe(pipefds) == -1) {
    perror("pipe");
    exit(EXIT_FAILURE);
  }
	int nombor = 22;
	
	printf("Writing a number to pipe....\n");
	write(pipefds[1],& nombor, sizeof(nombor));
	printf("Done.\n\n");
	
	printf("Number from pipe: %d\n", buffer);
	return EXIT_SUCCESS;
}
