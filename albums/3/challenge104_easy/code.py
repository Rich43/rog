''' A powerplant for the city of Redmond goes offline every third day because of local demands.
Ontop of this, the powerplant has to go offline for maintenance every 100 days. Keeping things
complicated, on every 14th day, the powerplant is turned off for refueling. Your goal is to
write a function which returns the number of days the powerplant is operational given a
number of days to simulate.

Formal Inputs & Outputs:

Input Description:

Integer days - the number of days we want to simulate the powerplant

Output Description:

Return the number of days the powerplant is operational.

Sample Inputs & Outputs:

The function, given 10, should return 7 (3 days removed because of maintenance every third day).
'''

def outage(n):

    for x in range(1, n + 1):
        if x % 3 == 0 or x % 100 == 0 or x % 14 == 0:
            n -= 1
    return n

if __name__ == '__main__':

    ans = outage(365)
    print('Power plant operational on ', ans, ' days per year!')