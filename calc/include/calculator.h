#pragma once
#include "stack.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "exeptions.h"
#include "calcresult.h"
char it_is_operator(char);
unsigned char check(char* string);
char* copy_delete_space(char* string);
unsigned char help_calc_op(token* a,token* b, token* op);
calcresult calc(char* str);