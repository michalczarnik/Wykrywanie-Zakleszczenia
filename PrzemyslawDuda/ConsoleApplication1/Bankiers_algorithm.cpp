    #include<stdio.h>
    #include<stdlib.h>
    #include<string.h>
     
    int max[20][20];
    int allocated[20][20];
    int need[20][20];
    int available[20];
    int n, m;
    int safe[20];
    int issafe();
    int memcp(int*, int*, int);
     
    void print(int (*a)[20], int n, int m)
    {
      int i, j;
      for(i = 0; i < n; i++)
        {
          printf("\n");
        for(j = 0; j < m; j++)
          {
    	printf("%d\t", a[i][j]);
          }
        }
    }
     
    int main()
    {
      int i, j, p, request[20];
      int *avail, *alloc, *nd;
      printf("Enter the no. of processes and resources: ");
      scanf("%d%d", &n, &m);
      printf("Enter the max. need matrix\n");
      for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
          {
    	printf("MaxNeed[%d][%d]: ", i+1, j+1); 
    	scanf("%d", &max[i][j]);
          }
      printf("Enter the available resource vector: \n");
      for(i = 0; i < m; i++)
        {
          printf("Resource[%d]: ", i+1);
          scanf("%d", &available[i]);
        }
      printf("Enter the  allocation matrix\n");
      for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
          {
            printf("Allocated[%d][%d]: ", i+1, j+1);
            scanf("%d", &allocated[i][j]);
          }
      for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
          {
            need[i][j] = max[i][j] - allocated[i][j];
          }
     
      while(1)
        {
          printf("Enter the id of the requesting process: ");
          scanf("%d", &p);
          p--;
          printf("Enter the request vector\n");
          for(i = 0; i < m; i++)
    	{
    	  printf("Resource[%d] :", i+1);
    	  scanf("%d", &request[i]);
    	}
          if(isless(request, need[p]))
    	{
    	  if(isless(request, available))
    	    {
    	      avail = malloc(4*m);
    	      alloc = malloc(4*m);
    	      nd = malloc(4*m);
    	      memcp(avail,available,m);
    	      memcp(alloc,allocated[p],m);
    	      memcp(nd,need[p],m);
    	      sub(available,request);
    	      add(allocated[p],request);
    	      sub(need[p],request);
    	      //     print(allocated,n,m);
    	      //print(need,n,m);
    	      if(issafe())
    		{
    		  printf("Request Accepted!!!\n");
    		}
    	      else
    		{
    		  printf("Request Pending!!!\nSystem cannot be in safe state if the request is accepted now\n");
    		  {
    		    memcp(available,avail,m);
    		    memcp(allocated[p],alloc,m);
    		    memcp(need[p],nd,m);
    		  }
    		}
    	      free(avail);
    	      free(alloc);
    	      free(nd);
    	    }
    	  else
    	    {
    	      printf("Request Pending!!!\nNot enough available resources\n");
    	    } 
    	}
          else
    	{
    	  printf("Invalid request!!!\n");
    	}
          printf("Enter 0 to stop or any other number to continue: ");
          scanf("%d", &p);
    	if(!p)
    	  break;
        }
    } 
     
    int memcp(int *a,int *b, int n)
    {
      int i;
      for(i = 0;i < n; i++)
        a[i] = b[i];
    }
     
    int isless(int *a,int *b)
    {
      int i;
      for(i = 0; i < m; i++)
          if(a[i] > b[i])
    	  return 0;
      return 1;
    }
     
    int issafe()
    {
      int i, *work, *finish;
      char out[50];
      work = malloc(m*4);
      finish = malloc(n*4);
      memset(finish, 0, n);
      memcp(work, available, m);
      sprintf(out, "<");
      for(i = 0; i < n; i++)
        {
          if(isless(need[i], work) && !finish[i])
    	{
    	  add(work, allocated[i]);
    	  finish[i] = 1;
    	  sprintf(out + strlen(out), "P%d, ", i+1);
    	  i = -1;
    	}
        }
      printf("\n");
      for(i = 0; i < n; i++)
        if(!finish[i])
          break;
      free(work);
      free(finish);
      if(i == n)
        {
          sprintf(out + strlen(out) - 2, ">");
          printf("%s\n", out);
        return 1;
        }
      else
        return 0;
    }
     
    int add(int *a, int *b)
    {
      int i;
      for(i = 0; i < m; i++)
        a[i] += b[i];
      return 1;
    }
     
     int sub(int *a, int *b)
     {
       int i;
       for(i = 0; i < m; i++)
         a[i] -= b[i];
       return 1;
     }