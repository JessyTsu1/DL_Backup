#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<>
int main(){
	char str[2048] = {0};//输入的字符串(其中可能包含关键字)
	char Keywords[8][10] = {"if", "else", "for", "while", "do", "return", "break", "continue"};
	char *ptr = NULL;
	char *fast = NULL;
	char t;
	int KeyNum[8] = {0};
	int i;

	gets(str);//输入
	ptr = str;
	while (*ptr){
		while (*ptr && *ptr == ' ')
			ptr++;//跳过空格
		fast = ptr;
		while (*fast){
			if (!*fast || *fast == ' ')
				break;
			fast++;
		}
		t = *fast;
		*fast = 0;
		for (i=0;i<32;i++){
			if (strcmp(ptr,Keywords[i]) == 0)
				KeyNum[i]++;
		}
		*fast = t;
		ptr = fast;
	}
	for (i=0;i<32;i++){
		if (KeyNum[i])
			printf("Number of keyword \" %s \" is %d\n",Keywords[i],KeyNum[i]);
	}
	system("pause");
	return 0;
}