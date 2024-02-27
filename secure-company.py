import math as mt
import os
import time

def factorial(n):
    
    if n==1 or n == 0:
        return 1
    
    result=int(1)
    
    for i in range(n):
        try:
            result *= i + 1
        except:
            result = 10e307
    
    return result

def reclamation_distribution( n ): # M
    
    result=0
    for i in range(n):
        
       if n * ((factorial(i)*factorial(n-i))/factorial(n))>=1:
           result+=i
    
    return result
        
def amount_reclamation_distribution( n ): # number of reclamations
    
    return reclamation_distribution(n)

def time_client_arrive( amount_reclamations ): # time for clients to arrive

        if amount_reclamations < 2:
            return 1
        
        return int(mt.log2(amount_reclamations))

def number_client_time( n , reclamation_number , time): # number of clients leaving
    
    client_left=client_time( reclamation_number , n)
    
    if int( client_left*time ) == 0:
        return 1
    else:
        return int( client_left*time )
    
def client_time( reclamation_number , n ): # distribution for a client to leave
    
    if n % 2 == 0:
        
        if reclamation_number == 0:
            return 0
        
        return 1-1/reclamation_number
    else:
        return 1/n

def company( n0 , a0 , capital ):

    t=0
    n=n0
    reclamation_number=0
    total_reclamation=0
    n_in=n0
    
    ''' 
        n0: initial number of clients
        a0: initinal company capital
        n_in: total number of client assisted
        reclamation_number: total number of complaints
    '''

    start = time.time()
    while n != 0:
        
        arrive_time = time_client_arrive( amount_reclamations = reclamation_number )
                
        n += 1
        n_in +=1  
                    
        a0 += n * capital                
        
        reclamation_number = amount_reclamation_distribution( n )        
        
        total_reclamation += reclamation_number        
        
        cleft= number_client_time(n , reclamation_number , arrive_time)

        n-=cleft
    
        t += arrive_time
        
        if time.time() - start >= 1:
            
            os.system("cls")
            print(f"total clients assisted: {n_in}")
            print( f"client:{n} ")
            print(f"total money: {a0}")
            print(f"number of reclamations for time { t }: { reclamation_number }")
            print(f"total reclamations: {total_reclamation}")
            print(f"client left: {cleft}")
            print(f"arriving time for next client: {arrive_time} ")
            print("-------------------------------------------------------------------------------->>>>>")
            
            start +=1
    pass

company( 1000 , 500 , .1 )





