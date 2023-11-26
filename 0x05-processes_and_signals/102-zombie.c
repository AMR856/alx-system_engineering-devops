#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - entry point of the program
 *
 * Return: 0 or 1
*/

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d", getpid());
			exit(0);
		}
		else
		{
			perror("Fork failed");
			exit(1);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - A function to loop to infinity and beyond
 *
 * Return: Nothing (void)
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
