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
            result = 10e308
    
    return result

def reclamation_distribution1( n ): # M
    
    try:
        res= (1/2)**n
        return res
    except:
        return 10e-308
    

def reclamation_distribution2(xi):
    
    if xi == 0:
        xi+=1
    
    return 1-(1/xi)
        
def amount_reclamation_distribution( n ): # F
    
    complaint_number=0
    
    for xi in range(n):
        
        if (n - (xi+1)) % 2 == 0: # people complaint if half of clients complaint
                
            try:
                combinations= int(int(factorial(n)/ (factorial(xi+1)*factorial(n-(xi+1))))) 
            except:
                combinations=10e308
            
            recl = reclamation_distribution1(n) 
            
            pq=( recl** (xi+1) )*(( 1 - recl )**( n - (xi+1) )) # number of complaits for a client that complaints with probability of p
            
            complaint_number += int(combinations*pq)
        
        else:
            
            try:
                combinations= (int(factorial(n)/ (factorial((xi+1))*factorial(n-(xi+1))))) # people complaint if there are many clients
            except:
                combinations=10e308
                
            recl = reclamation_distribution2((xi+1)) 
            
            pq=( recl** (xi+1) )*(( 1 - recl )**( n - (xi+1) )) # number of complaits for a client that complaints with probability of p
            
            complaint_number += int(combinations*pq)
            
    return complaint_number

def time_client_arrive( amount_reclamations ): # v

        if amount_reclamations < 2:
            return 1
        
        return int(mt.log2(amount_reclamations))

def number_client_time( n , reclamation_number , time): # u
    
    client_left=client_time( reclamation_number , n)
    
    return int( client_left*time )    
    
def client_time( reclamation_number , n ):
    
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
    
    last_time=0
    start = time.time()
    while n != 0:
        
        arrive_time = time_client_arrive( amount_reclamations = reclamation_number )
        
        if t-last_time >= arrive_time: 
            n += 1
            n_in +=1  
            last_time = t
        
        a0 += n * capital        
        
        
        reclamation_number = amount_reclamation_distribution( n )
        
        
        total_reclamation += reclamation_number
        
        
        cleft= number_client_time(n , reclamation_number , t - last_time)


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

company( 100 , 500 , .1 )





