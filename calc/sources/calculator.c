#include "../include/calculator.h"
#define _USE_MATH_DEFINES


char it_is_operator(char c)
{
    return c=='+'||c=='-'||c=='*'||c=='/'||c=='('||c==')';
}


unsigned char check(char* str)
{
    char flag=0;
    for(int i=0; str[i];i++)
    {
        if (str[i] == ' ') continue;

        if(!it_is_operator(str[i])&&!(str[i]>='0'&&str[i]<='9')&&str[i]!=' ')
        {
            return INVALID_CHARACTER;
        }
        flag = 1;
    }
    if(!flag)
    {
        return EMPTY_STR;
    }
    int bracket = 0;
    for(int i=0; str[i];i++)
    {
        if(str[i]=='(')
        {
            bracket++;
            i++;
            while(str[i]==' ') i++;
            if(str[i]==')')
            {
                return BRACKET_ERROR;
                //printf("%s - Ошибка, в скобках '( )' ничего нет \n",str);
            }
            else if (it_is_operator(str[i]) && str[i] != '-' && str[i] != '(')
            {
                return BRACKET_ERROR;
                //printf("%s - Ошибка, после '(', встреченно '%c'\n",str,str[i]);
            }
            i--;
        }
        else if(str[i]==')')
        {
            bracket--;
            if(bracket<0)
            {
                return BRACKET_ERROR;
                //printf("%s - Ошибка, встреченно ')', хотя до этого не было '('\n",str);
            }
            i++;
            while(str[i]==' ') i++;
            if(str[i]!=0&&(!it_is_operator(str[i])||str[i]=='('))
            {
                return STREAM_ERROR;
                //printf("%s - Ошибка, после ')' встреченно '%c', хотя ожидался оператор \n", str, str[i]);
            }
            i--;
        }
    }
    if(bracket>0)
    {
        return BRACKET_ERROR;
        //printf("%s - Ошибка, отсутствует закрывающая(-ие) скобка(-и) ')'\n",str);
    }
    for(int i=0;str[i];i++)
        if(it_is_operator(str[i])&&str[i]!='('&&str[i]!=')')
        {
            i++;
            while(str[i]==' ') i++;
            
            if(it_is_operator(str[i])&&str[i]!='(')
            {
                return STREAM_ERROR;
                //printf("%s - Ошибка, после оператора встреченно '%c'\n", str, str[i]);

            }
            else if(str[i]==0)
            {
                return STREAM_ERROR;
                //printf("%s - Ошибка, после оператора идет конец строки'\n", str);
            }
            i--;
        }
   return 1;
}




char* copy_delete_space(char* str)
{
    char* str_copy=(char*)malloc((strlen(str)+3)*sizeof(char));
    if (str_copy == NULL) return NULL;

    {
        str_copy[0]='(';
        int j=1;
        for(int i=0;str[i];i++)
        {
            if(str[i]!=' ')
            {
                str_copy[j]=str[i];
                j++;
            }
        }
        str_copy[j]=')';
        str_copy[j+1]=0;
    }
    return str_copy;
}


unsigned char help_calc_op(token* a,token* b, token* op)
{
    if (a == NULL || b == NULL || op == NULL)
        return ALLOCATION_ERROR;
    if(op->element.op.ch=='*')
        a->element.digit=a->element.digit*b->element.digit;
    else if(op->element.op.ch=='/')
    {
        a->element.digit=a->element.digit/b->element.digit;
        if(b->element.digit==0) return DIV_ZERO;
    }
    else if(op->element.op.ch=='+')
        a->element.digit=a->element.digit+b->element.digit;
    else if(op->element.op.ch=='-')
        a->element.digit=a->element.digit-b->element.digit;
    free(b);
    free(op);
    return NONE;
}

calcresult calc(char* str)
{
    Stack* SV=create_stack();
    Stack* SO=create_stack();
    unsigned char error = NONE;
    for (int i = 0; str[i]; i++)
    {
        if(str[i]>='0'&&str[i]<='9')
        {
            error = push_back(SV, create_token_d(atoi(str + i)));
            if (error != NONE) break;
            while(str[i+1]>='0'&&str[i+1]<='9') i++;
        }
        else if(str[i]=='-'&&(i==0||str[i-1]=='('))
        {
            unsigned char error = push_back(SV, create_token_d(0));
            if (error != NONE) break;
            if (error != NONE)
            {
                delete_stack(SV);
                delete_stack(SO);
                calcresult res = { error, 0 };
                return res;
            }
            error=push_back(SO, create_token_op('-'));
            if (error != NONE) break;
        }
        else if(it_is_operator(str[i]))
        {
            token* t=create_token_op(str[i]);
            while(SO->last&&(SO->last->token->element.op.priority>=t->element.op.priority&&SO->last->token->element.op.ch!='(')&&str[i]!='(')
            {
                token* b=pop_back(SV);
                token* a=pop_back(SV);
                token* op=pop_back(SO);
                error = help_calc_op(a,b,op);
                if (error != NONE) break;
                error = push_back(SV, a);
                if (error != NONE) break;
            }
            if(str[i]==')')
            {
                free(t);
                pop_back(SO);
            }
            else
                push_back(SO, t);
        }
    }
    if (error != NONE)
    {
        delete_stack(SV);
        delete_stack(SO);
        calcresult res = { error, 0 };
        return res;
    }
    int result=SV->first->token->element.digit;
    delete_stack(SV);
    delete_stack(SO);
    calcresult res = { NONE, result };
    return res;
}