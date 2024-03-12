#include "../include/stack.h"

token* create_token_d(int d)
{
    token* t=(token*)malloc(sizeof(token));
    if (t == NULL) return NULL;
    t->type=DIGIT;
    t->element.digit=d;
    return t;
}
token* create_token_op(char ch)
{
    token* t=(token*)malloc(sizeof(token));
    if (t == NULL) return NULL;
    t->type=OPERATOR;
    if(ch=='('||ch==')')
        t->element.op.priority=0;
    else if(ch=='+'||ch=='-')
        t->element.op.priority=1;
    else if(ch=='*'||ch=='/')
        t->element.op.priority=2;
    else if(ch=='^')
        t->element.op.priority=3;
    else
        t->element.op.priority=-1;
    t->element.op.ch=ch;
    return t;
}