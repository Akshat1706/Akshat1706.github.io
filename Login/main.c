#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main() {

    FILE *ptr = NULL;
    ptr = fopen("tex.txt", "a");
    char method[10];
    char userid[100];
    char psw[8];
    char confirmation[10];
    char checkuser[100];
    char checkpsw[100];
    printf("Please Choose Login Or Register \n");
    scanf("%s", &method);
  if (strcmp(method, "register") == 0 || strcmp(method, "Register") == 0)
  {
    printf("PLease Enter Your  8 letter Username\n");
    scanf("%s", &userid);
    fprintf(ptr, "%s " ,userid);
    printf("Please Enter 8 letter Password \n");
    scanf("%s", &psw);
    fprintf(ptr, "%s " ,psw);
    printf("Username: %s\n", userid);
    printf("Password: %s\n", psw);
    printf("Please Write 'Confirm' to finalize \n");
    scanf("%s", &confirmation);

    if (strcmp(confirmation, "Confirm") == 0)
    {
        printf("You Are Now Registered \n");
        


        fclose(ptr);
        exit;
    }
    else
    {
        printf("Please Start Over \n");
        exit;
    }
    
    

  }
  else if (strcmp(method, "login") == 0 || strcmp(method, "Login" ) == 0){
    FILE *ptr = NULL;
    ptr = fopen("tex.txt", "r");
   printf("please enter your 8 digit Username \n");
    scanf("%s", &userid);
    fscanf(ptr , "%s", &checkuser);
    if (strcmp(userid, checkuser) == 0)
    {
     printf("Please Enter Your Password \n");
     scanf("%s", &psw);
     fscanf(ptr, "%s", &checkpsw);
     if (strcmp(psw, checkpsw) == 0)
     {
      printf("Succesfull Login ");

     }
     else {
      printf("Wrong Password");
     }
     
    }
  }
  
    return 0;
}