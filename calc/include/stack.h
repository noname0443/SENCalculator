#pragma once
#include "exeptions.h"
#include "token.h"
typedef struct StackElement{
    token* token;
    struct StackElement* next;
    struct StackElement* prev;
} StackElement;

typedef struct {
    StackElement* first;
    StackElement* last;
} Stack;

Stack* create_stack();
unsigned char push_back(Stack*, token*);
token* pop_back(Stack* S);
void stack_printf(Stack* S);
void delete_stack(Stack* S);