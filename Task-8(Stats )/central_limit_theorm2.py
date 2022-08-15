from math import erf,sqrt

tickets = int(input())
students = int(input())
mean = float(input())
sigma = float(input())

def cdf(x,mu,sig):
    return ( 1 + erf((x - mu)/ sqrt(2) / sig )) / 2

mu = mean * students
sig = sigma * sqrt(students)

print(round(cdf(tickets,mu,sig) , 4 ))