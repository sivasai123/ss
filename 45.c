#include <stdio.h>

int main(void) {
	// your code goes here
	int num,count=0;
	scanf("%d",&num);
	while(num!=0)
	{
		num=num/10;
		count++;
	}
	printf("%d",count);
}
