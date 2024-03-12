#include "calcresult.h"
#ifdef WIN32
	#define CALC_API __declspec(dllexport)
#else
	#define CALC_API
#endif
CALC_API calcresult calculate(char* str);
CALC_API unsigned char checkstring(char* str);