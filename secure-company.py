import math as mt

def factorial(n):
    
    if n==1 or n == 0:
        return 1
    
    return n*factorial(n-1)

def reclamation_distribution1( n ): # M
    
    if n == 1:
        return 1/2
    
    return (1/2)*reclamation_distribution1(n-1)

def reclamation_distribution2(xi):

    return 1-(1/xi)
        
def amount_reclamation_distribution( n ): # F
    
    complaint_number=0
    
    for xi in range(n):
        
        if n - xi % 2 == 0: # people complaint if half of clients complaint
                
            combinations= int(int(factorial(n)/ (factorial(xi)*factorial(n-xi)))) 
            
            recl = reclamation_distribution1(n) 
            
            pq=( recl** xi )*(( 1 - recl )**( n - xi )) # number of complaits for a client that complaints with probability of p
            
            complaint_number += combinations*pq
            
        
        else:
            
            combinations= (int(factorial(n)/ (factorial(xi)*factorial(n-xi)))) # people complaint if there are many clients
            
            recl = reclamation_distribution2(xi) 
            
            pq=( recl** xi )*(( 1 - recl )**( n - xi )) # number of complaits for a client that complaints with probability of p
            
            complaint_number += combinations*pq
            
            
    return complaint_number

def time_client_arrive( amount_reclamations ): # v
    
    return int(factorial(amount_reclamations)*mt.e) # poisson distribution using alpha=1

def number_client_time( n , reclamation_number , time): # u
    
    client_left=client_time( reclamation_number , n)
    
    return int( client_left*time )    
    

def client_time( reclamation_number , n ):
    
    if n % 2 == 0:
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
    while n != 0:
        
        arrive_time = time_client_arrive( amount_reclamations = reclamation_number )
        
        if t-last_time >= arrive_time: 
            n += 1
            n_in +=1  
            print(f"total clients assisted: {n_in}")
            last_time = t
            print( f"client:{n} ")
        
        a0 += n * capital        
        
        print(f"total money{a0}")
        
        reclamation_number = amount_reclamation_distribution( n )
        
        print(f"number of reclamations for time{t}: {reclamation_number}")
        
        total_reclamation += reclamation_number
        
        print(f"total reclamations: {total_reclamation}")
        
        n -= number_client_time(n , reclamation_number , t - last_time)
    
        t += arrive_time
    
    pass





