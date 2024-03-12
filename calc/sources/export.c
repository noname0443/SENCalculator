#include "../include/export.h"
#include "../include/calculator.h"
calcresult calculate(char* str)
{
	char* copy = copy_delete_space(str);
	if(copy==NULL)
	{
		calcresult result = {ALLOCATION_ERROR, 0};
		return result;
	}
	unsigned char checkresult = check(copy);
	if (checkresult != NONE)
	{
		free(copy);
		calcresult result = { checkresult,0 };
		return result;
	}
	calcresult result = calc(copy);
	free(copy);
	return result;
}
unsigned char checkstring(char* str)
{
	return check(str);
}