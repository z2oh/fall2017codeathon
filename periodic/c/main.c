#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_elem(int cc) {
	switch(cc)
	{
		case 24931:
		case 24935:
		case 24940:
		case 24941:
		case 24946:
		case 24947:
		case 24948:
		case 24949:
		case 98:
		case 25185:
		case 25189:
		case 25192:
		case 25193:
		case 25195:
		case 25202:
		case 99:
		case 25441:
		case 25444:
		case 25445:
		case 25446:
		case 25452:
		case 25453:
		case 25454:
		case 25455:
		case 25458:
		case 25459:
		case 25461:
		case 25698:
		case 25715:
		case 25721:
		case 25970:
		case 25971:
		case 25973:
		case 102:
		case 26213:
		case 26220:
		case 26221:
		case 26226:
		case 26465:
		case 26468:
		case 26469:
		case 104:
		case 26725:
		case 26726:
		case 26727:
		case 26735:
		case 26739:
		case 105:
		case 26990:
		case 26994:
		case 107:
		case 27506:
		case 27745:
		case 27753:
		case 27762:
		case 27765:
		case 27766:
		case 28003:
		case 28004:
		case 28007:
		case 28014:
		case 28015:
		case 28020:
		case 110:
		case 28257:
		case 28258:
		case 28260:
		case 28261:
		case 28264:
		case 28265:
		case 28271:
		case 28272:
		case 111:
		case 28519:
		case 28531:
		case 112:
		case 28769:
		case 28770:
		case 28772:
		case 28781:
		case 28783:
		case 28786:
		case 28788:
		case 28789:
		case 29281:
		case 29282:
		case 29285:
		case 29286:
		case 29287:
		case 29288:
		case 29294:
		case 29301:
		case 115:
		case 29538:
		case 29539:
		case 29541:
		case 29543:
		case 29545:
		case 29549:
		case 29550:
		case 29554:
		case 29793:
		case 29794:
		case 29795:
		case 29797:
		case 29800:
		case 29801:
		case 29804:
		case 29805:
		case 29811:
		case 117:
		case 118:
		case 119:
		case 30821:
		case 121:
		case 31074:
		case 31342:
			return cc;
		default:
			return 0;
	}
}

int concat_chars(char c1, char c2)
{
	return (c1 << 8) + c2;
}


int len, arr_size;
int* glyphs;

int count_paths(int start_index)
{
	if(glyphs[start_index] == 0)
	{
		return 0;
	}
	if(start_index == len - 1)
	{
		return 1;
	}
	if(start_index == len - 2)
	{
		return count_paths(start_index + 1);
	}
	if(start_index == arr_size - 1)
	{
		return 1;
	}
	if(start_index == arr_size - 2)
	{
		return count_paths(len - 1);
	}
	if(start_index < len)
	{
		return count_paths(start_index + 1) + count_paths(start_index + len + 1);
	}
	if(start_index >= len)
	{
		return count_paths(start_index - len + 2) + count_paths(start_index + 2);
	}
}

int count(char* input)
{
	len = strlen(input);
	arr_size = 2 * len - 1;
	glyphs = malloc(arr_size * sizeof(int));
	for(int i = 0; i < len - 1; i++)
	{
		glyphs[i] = is_elem(input[i]);
		glyphs[len + i] = is_elem(concat_chars(input[i], input[i+1]));
	}
	glyphs[len - 1] = is_elem(input[len - 1]);
	return count_paths(0) + count_paths(len);
}

int main()
{
	char* line = NULL;
	size_t size = 0;
	ssize_t nread;
	while((nread = getline(&line, &size, stdin)) != -1)
	{
		line[strlen(line) - 1] = '\0';
		printf(line);
		printf(", ");
		printf("%d\n", count(line));
		fflush(stdout);
	}
}
