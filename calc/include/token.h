#pragma once
#include <stdlib.h>
#include <stdarg.h>
#define DIGIT 1
#define OPERATOR 2
#define FUNCTION 3

typedef struct{
    char type;
    
    union{
        int digit;
        struct
        {
            int priority;
            char ch;
        } op;
    } element;
} token;

token* create_token_d(int);
token* create_token_op(char);