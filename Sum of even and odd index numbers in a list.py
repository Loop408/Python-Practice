#Sum of even and odd index numbers in a list
n=list(map(int,input("Enter numbers: ").split(',')))
even_index_sum=0
odd_index_sum=0
for i in range(len(n)):
    if n[i]%2==0:   
        even_index_sum +=i
    else:             
        odd_index_sum +=i
print("Even number index sum =",even_index_sum)
print("Odd number index sum =",odd_index_sum)
