def rent(movie_no,cust_no,Rental_T): 
    if movie_no not in Rental_T:
        Rental_T.append({movie_no:cust_no})
        i=i+1
    else:
        print("Movie already rented.....")
    
def rent(movie_no,cust_no,Rental_T): 
    if movie_no in Rental_T:
        Rental_T.delete({movie_no:cust_no})
        i=i-1
    else:
        print("Movie not returned.....")
        
def customers_d(customers):
    print(customers)
    
def available(Rental_T,available,movie_no):
    if movie_no not in Rental_T:
        available.append(movie_no)
        print(movie_no)
    
def details(Rental_T):
    print(Rental_T)
    
int main()
{
    print("Choose an option:")
    print("1.Rent")
    print("2.Return")
    print("3.Generate rental report")
    choice=int(input("Enter"))
    
    movies=[{1:"DDLJ"},{2,"K3G"},{3,"Singham"}]
    customers=[{1,"Raj"},{2,"Ram"},{3,"Suman"}]
    
    Rental_t=[]
    available=[]
    
    if choice==1:
        m=int(input("Enter movie no:"))
        n=int(input("Enter customer id:"))
        rent(m,n,Rental_T)
    else if choice==2:
        m=int(input("Enter movie no:"))
        n=int(input("Enter customer id:"))
        rent(m,n,Rental_T)
    else if choice==3:
        details(Rental_T)
    else:
        print("Choose a right option")
     
    
}
