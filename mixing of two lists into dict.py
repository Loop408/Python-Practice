#mixing of two lists
M=['Mumbai', "Hyd", "delhi", 'Dubai', "Jaipur", 'Chennai','Kolkata', "Dadar", 'Danish', "Goa", "Pune", "Banglore"]
J= [50,40,30,20,100,350,280,200]
my_dict={}
for i in range(min(len(M),len(J))):
    my_dict[M[i]]=J[i]
print(my_dict)
