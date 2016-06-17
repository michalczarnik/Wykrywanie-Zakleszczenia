package RMIServe;

import java.util.Scanner;
import javax.naming.Context;
import javax.naming.InitialContext;
import java.rmi.*;  
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.server.*;
import java.util.*;
import rmiproject.Chat;
import rmiproject.ChatInterface;


public class Bankers{
    private int need[][],allocate[][],max[][],avail[][],np,nr;
     
    private void input(){
     Scanner sc=new Scanner(System.in);
     System.out.print("Enter no. of processes and resources : ");
     np=sc.nextInt();  //no. of process
     nr=sc.nextInt();  //no. of resources
     need=new int[np][nr];  //initializing arrays
     max=new int[np][nr];
     allocate=new int[np][nr];
     avail=new int[1][nr];
      
     System.out.println("Enter allocation matrix -->");
     for(int i=0;i<np;i++)
          for(int j=0;j<nr;j++)
         allocate[i][j]=sc.nextInt();  //allocation matrix
       
     System.out.println("Enter max matrix -->");
     for(int i=0;i<np;i++)
          for(int j=0;j<nr;j++)
         max[i][j]=sc.nextInt();  //max matrix
       
        System.out.println("Enter available matrix -->");
        for(int j=0;j<nr;j++)
         avail[0][j]=sc.nextInt();  //available matrix
         
        sc.close();
    }
     
    private int[][] calc_need(){
       for(int i=0;i<np;i++)
         for(int j=0;j<nr;j++)  //calculating need matrix
          need[i][j]=max[i][j]-allocate[i][j];
        
       return need;
    }
  
    private boolean check(int i){
       //checking if all resources for ith process can be allocated
       for(int j=0;j<nr;j++) 
       if(avail[0][j]<need[i][j])
          return false;
    
    return true;
    }
 
    public void isSafe(){
       input();
       calc_need();
       boolean done[]=new boolean[np];
       int j=0;
 
       while(j<np){  //until all process allocated
       boolean allocated=false;
       for(int i=0;i<np;i++)
        if(!done[i] && check(i)){  //trying to allocate
            for(int k=0;k<nr;k++)
            avail[0][k]=avail[0][k]-need[i][k]+max[i][k];
         System.out.println("Allocated process : "+i);
         allocated=done[i]=true;
               j++;
             }
          if(!allocated) break;  //if no allocation
       }
       if(j==np)  //if all processes are allocated
        System.out.println("\nSafely allocated");
       else
        System.out.println("All proceess cant be allocated safely");
    }
     
    public static void main(String[] args) throws RemoteException {
      // new Bankers().isSafe();
        //LocateRegistry.createRegistry(8080);
      System.setProperty("java.security.policy","C:\\Users\\LukaBas\\Documents\\NetBeansProjects\\RMIProject\\src\\rmiproject");
	    try {
		    	System.setSecurityManager(new SecurityManager());
		    	Scanner s=new Scanner(System.in);
		    	System.out.println("Enter Your name and press Enter:");
		    	String name=s.nextLine().trim();		    		    	
		    	ChatInterface client = new Chat(name);
 
		    	ChatInterface server = (ChatInterface)Naming.lookup("rmi://localhost/ABC");
		    	String msg="["+client.getName()+"] got connected";
		    	server.send(msg);
		    	System.out.println("[System] Chat Remote Object is ready:");
		    	server.setClient(client);
 
		    	while(true){
		    		msg=s.nextLine().trim();
		    		msg="["+client.getName()+"] "+msg;		    		
	    			server.send(msg);
		    	}
 
	    	}catch (Exception e) {
	    		System.out.println("[System] Server failed: " + e);
	    	}
    }
}