
import statistics as stats

#import this without the code.stockdata for it to work
from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        averages = []
        
        
        for row in self.data:
            data_row = row[1:]
            
            y = []
            for x in data_row:
                try:
                    y.append(float(x))
                except ValueError: 
                    continue #pass #break
                
            new_average = stats.mean(y)
            
            rounded_average = round(new_average, 3)
            averages.append(rounded_average)
        return averages 

#float is turning our numbers from string to integers 
#

    def median02(self):
        """pt2
        """
        median_values = []
            
        for rows in self.data:
            data_row = rows[1:] #returns data no headers
            
            z = []
            for numb in data_row:
                try:
                    z.append(float(numb))
                except ValueError:
                    continue 
            median_values_calc = stats.median(z)
            
            median_values.append(median_values_calc)
            
        return median_values
        

    def stddev03(self):
        """pt3
        """
        stddev = []
        
        for rows in self.data:
            data_row = rows[1:]
            
            z = []
            for numb in data_row:
                try:
                    z.append(float(numb))
                except ValueError:
                    continue
            stddev_new = stats.stdev(z)
            
            stddev_new_rounded = round((stddev_new), 3)
            
            stddev.append(stddev_new_rounded)
        
        return stddev 
