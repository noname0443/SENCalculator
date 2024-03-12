#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "../include/stack.h"


Stack* create_stack()
{
    Stack* current = (Stack*)malloc(sizeof(Stack));
    if (current == NULL) return NULL;
    current->first=NULL;
    current->last=NULL;
    return current;
}

unsigned char push_back(Stack* S, token* T)
{
    StackElement* current=(StackElement*)malloc(sizeof(StackElement));
    if (current == NULL) return ALLOCATION_ERROR;
    current->token=T;
    if(S->last==NULL)
        S->first=current;
    else
        S->last->next=current;
    current->prev=S->last;
    current->next=NULL;
    S->last=current;
    return NONE;
}

token* pop_back(Stack* S)
{
    if(S->first==NULL) return NULL;
    StackElement* current = S->last;
    if(S->first==S->last)
        S->first=NULL;
    else
        S->last->prev->next=NULL;
    S->last=S->last->prev;
    token* t=current->token;
    free(current);
    return t;
}

void delete_stack(Stack* S)
{
    StackElement* current=S->first;
    free(S);
    if(current==NULL) return;
    while(current->next)
    {
        current=current->next;
        free(current->prev->token);
        free(current->prev);
    }
    free(current->token);
    free(current);
}

void stack_printf(Stack* S)
{
    StackElement* current=S->first;
    while(current)
    {
        if(current->token==NULL)
        {printf("gg ");}
        else if(current->token->type==DIGIT)
        {
            printf("%d ",current->token->element.digit);
        }
        else if(current->token->type==OPERATOR)
        {
            printf("(%d '%c') ", current->token->element.op.priority, current->token->element.op.ch);
        }
        else printf("404");
        current=current->next;
    }
    printf("\n");
}



