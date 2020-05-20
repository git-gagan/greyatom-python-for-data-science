# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record=np.asarray(new_record)
print(new_record)
census=np.concatenate((data,new_record),axis=0)
print(census)



# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=age.max()
min_age=age.min()
print(max_age,min_age,sep='\n')
age_mean=age.mean()
print(age_mean,sep='\n')
age_std=np.std(age)


# --------------
#Code starts here
race=census[:,2] #print(race)
#race_0,race_1,race_2,race_3,race_4=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
'''for i in race:
    if(i==4):
        race_4=np.append(race_4,i)
    if(i==3):
        race_3=np.append(race_3,i)
    if(i==2):
        race_2=np.append(race_2,i)
    if(i==1):
        race_1=np.append(race_1,i)
    if(i==0):
        race_0=np.append(race_0,i)'''#print(race_0,race_1,race_2,race_3,race_4,sep='\n')
len_0,len_1,len_2,len_3,len_4=len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)
length=np.array([len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)])
print(length,end='\n')
minority=length.min()
minority_race=list(length).index(minority)
print(minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
#print(senior_citizens)
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print('\n',avg_working_hours)


# --------------
#Code starts here
high,low=census[census[:,1]>10],census[census[:,1]<=10]
print(high,low)
avg_pay_high=high.mean(axis=0)[7]
avg_pay_low=low.mean(axis=0)[7]
print(avg_pay_high,avg_pay_low,sep='\n')


