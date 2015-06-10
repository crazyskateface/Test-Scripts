"""
    Author- Travis Boettjer
    
    Run this as a python file in the command prompt or python executor as such 'python freqseq.py' and example will run
    
    
    
    Average runtime: O(n)
        This is because there is one for loop and the rest of the actions are constant time
    
    
    Worst Case runtime: O(n)
        For the same reason
    Worst Case Space Complexity: O(n)
        For the same reason
            


"""



import os

"""
    freqseq - This function takes an input stream and outputs a string
    of the 3 most frequent product id sequences.
"""
def freqseq(fname):
    # open file from string given as the argument
    with open(fname) as f:
        content = f.readlines() # create a list of the lines in the log
        
    dict = {}
    
    # for each line
    for i in content:
        m = 1
        pid = i[len(i)-5:len(i)].rstrip() # get product id
        if pid[0] == 'P':
            pid = pid[1:len(pid)]
        if dict == {}:
            dict[pid]=  1 # if dict is empty add first element
        else:
                          # if dict is not empty append 1 to the value of that entry in the dict
            m = dict.get(pid,0)
            dict[pid]=dict.get(pid,0) + 1
                    
        
                    
    #variables for counting frequencies of pid's
    cnt1 = 1
    one = ""
    cnt2 = 1
    two = ""
    cnt3 = 1
    tre = ""
    # iterate through items and get largest 3 frequencies
    for j in dict.items():
        if j[1] > cnt1:
            cnt3 = cnt2
            cnt2 = cnt1
            cnt1 = j[1]
            one = j[0]
            
        elif j[1] > cnt2:
            cnt3 = cnt2
            cnt2 = j[1]
            two = j[0]
        elif j[1] >=cnt3:
            cnt3 = j[1]
            tre = j[0]
            
    # they got swapped so need to swap back so first largest is first
    if cnt1 == cnt2:
        #swap
        temp = two
        two = one
        one = temp
    elif cnt2 == cnt3:
        # swap
        temp = tre
        tre= two 
        two = temp
    elif cnt1 == cnt1 == cnt3:
        #swap all
        temp = one
        one = tre
        tre = temp
    print 'The most frequently occurring sequence of product pages of length three is:''"P'+ one.rstrip()  +  ' P' +two.rstrip() +  ' P'+tre.rstrip()+'"'
    
        
        
        
# call the function giving the log.txt file as a string 
freqseq('log.txt')
