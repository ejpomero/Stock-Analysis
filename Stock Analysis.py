#Evan Pomeroy 6/3/2022

import matplotlib.pyplot as plt
import datetime as dt

def totalL():
    """
    Creates list of data for every day the stock is traded
  
    Asks for file then iterates through line to create list of lines from csv
  
    Parameters:
        none
    
    Input:
        File name
    
    Returns:
        List of stock info by day
  
    """
    x=True
    while x:
        try:
            stock = open(input("Enter file name (hint:'UA-2021.csv'): "), "r")
            x=False
        except:
            #make sure right file
            print("Error: File not found\tHint: Try 'UA-2021.csv'")
    LL = []
    ct = 0
    for line in stock:
        if ct ==0:
            ct =1
        else:
            d = line.split(",")
            LL.append(d)
    stock.seek(0,0)
    return LL


def datesL(listall):
    """
    Creates a list of dates stock was traded from list of trading day info
  
    Parameters:
        List of info from trading day
    
    Returns:
        List of dates
  
    """
    dates = []
    for i in listall:
        dates.append(i[0])
    return dates

def openL(listall):
    """
    Creates a list of open prices when stock was traded
  
    Parameters:
        List of info from trading day
    
    Returns:
        List opening prices
  
    """
    opens = []
    for i in listall:
        o = i[1]
        o2 = o.replace('"','')
        opens.append(float(o2))
    return opens

def closeL(listall):
    """
    Creates a list of closing prices when stock was traded
  
    Parameters:
        List of info from trading day
    
    Returns:
        List closing prices
  
    """
    closes = []
    for i in listall:
        c = i[4]
        c2 = c.replace('"','')
        closes.append(float(c2))
    return closes

def high_close(close, date):
    """
    Finds max stock price at closing from the year
    
    uses similar indexes to find date from a maximum close price index
  
    Parameters:
        List of dates
        List of closing prices
    
    Returns:
        none
    
    Prints:
        String with max price and date
  
    """
    maxc = 0
    index = 0
    dref = 0
    for i in close:
        if i > maxc:
            maxc = i
            dref = index
        index += 1
    print(f'The highest closing price was ${maxc} on {date[dref]}')

def low_open(openp, date):
    """
    Finds min stock price at open from the year
    
    uses similar indexes to find date from a min open price index
  
    Parameters:
        List of dates
        List of opening prices
    
    Returns:
        none
    
    Prints:
        String with min price and date
  
    """
    mino = 999
    index = 0
    dref = 0
    for i in openp:
        if i < mino:
            mino = i
            dref = index
        index += 1
    print(f'The lowest opening price was ${mino} on {date[dref]}')

def high_close10(close, date):
    """
    Finds 10 max stock price at closing from the year
    
    uses similar indexes to find date from a maximum close price index.
    Prices and dates are stored in a list then current max price and date are
    removed from list.  It does this 9 more times to find the max 10 times.
  
    Parameters:
        List of dates
        List of closing prices
    
    Returns:
        none
    
    Prints:
        String with 10 max prices and dates
  
    """
    high = []
    dateL = []
    for x in range(10):
        maxc = 0
        index = 0
        dref = 0
        for i in close:
            if i > maxc:
                maxc = i
                dref = index
            index += 1
        high.append(maxc)
        dateL.append(date[dref])
        close.pop(dref)
        date.pop(dref)
    print('10 Highest Closing Prices:\n')
    for i in range(10):
        print(f'Price: ${high[i]}\tDate: {dateL[i]}')
        
def low_open10(openL, date):
    """
    Finds 10 min stock price at open from the year
    
    uses similar indexes to find date from a min close price index.
    Prices and dates are stored in a list then current min price and date are
    removed from list.  It does this 9 more times to find the min 10 times.
  
    Parameters:
        List of dates
        List of opening prices
    
    Returns:
        none
    
    Prints:
        String with 10 min prices and dates
  
    """
    low = []
    dateL = []
    for x in range(10):
        mino = 999
        index = 0
        dref = 0
        for i in openL:
            if i < mino:
                mino = i
                dref = index
            index += 1
        low.append(mino)
        dateL.append(date[dref])
        openL.pop(dref)
        date.pop(dref)
    print('10 Lowest Opening Prices:\n')
    for i in range(10):
        print(f'Price: ${low[i]} \tDate: {dateL[i]}')
        

def openchart(openL, date):
    """
    Creates graph of average opening price by month
    
    When the first 2 characters (month) match the iterator date, the price is 
    added to a temporary total to find the average.  The average is added to
    a list and this happend 12 times (12 months).  The numbers are put into a
    pyplot and x axis is substituted for strings of months.
  
    Parameters:
        List of dates
        List of opening prices
    
    Returns:
        none
    
    Prints:
        Confirmation of graph creation
    
    Produces:
        png file of graph
  
    """
    mlist = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug','Sep','Oct','Nov','Dec']
    avgo = []
    month = []
    #range of months
    for i in range(1,13):
        Ltot = 0
        ct = 0
        for x in range(len(date)):
            #test if date matches current iteration date
            if int(date[x][0:2]) == i:
                Ltot += openL[x]
                ct+=1
        avgo.append(round(Ltot/ct,2))
        month.append(i)
    plt.xticks(month, mlist)
    plt.plot(month, avgo)
    plt.ylabel('Stock Price ($)')
    plt.title("Average Opening Price by Month")
    plt.savefig('Open Price by Month.png')
    plt.show()
    print("Graph saved as 'Open Price by Month.png'")
                    

    
def closechart(close, date):
    """
    Creates graph of average close price by month
    
    When the first 2 characters (month) match the iterator date, the price is 
    added to a temporary total to find the average.  The average is added to
    a list and this happend 12 times (12 months).  The numbers are put into a
    pyplot and x axis is substituted for strings of months.
  
    Parameters:
        List of dates
        List of closing prices
    
    Returns:
        none
    
    Prints:
        Confirmation of graph creation
    
    Produces:
        png file of graph
  
    """
    mlist = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug','Sep','Oct','Nov','Dec']
    avgo = []
    month = []
    for i in range(1,13):
        Ltot = 0
        ct = 0
        for x in range(len(date)):
            if int(date[x][0:2]) == i:
                Ltot += close[x]
                ct+=1
        avgo.append(round(Ltot/ct,2))
        month.append(i)
    plt.xticks(month, mlist)
    plt.plot(month, avgo)
    plt.ylabel('Stock Price ($)')
    plt.title("Average Closing Price by Month")
    plt.savefig("Close Price by Month.png")
    plt.show()
    print("Graph saved as 'Close Price by Month.png'")

def main():
    try:
        file = totalL()
        print("\n")
        high_close(closeL(file),datesL(file))
        print("\n")
        low_open(openL(file),datesL(file))
        print("\n")
        high_close10(closeL(file),datesL(file))
        print("\n")
        low_open10(openL(file),datesL(file))
        print("\n")
        openchart(openL(file),datesL(file))
        print("\n")
        closechart(closeL(file),datesL(file))
    except:
        print("Error!\tMake sure to use the file submitted through canvas (UA-2021.csv")

if __name__ == '__main__':
    main()
    


#I worked very hard on this