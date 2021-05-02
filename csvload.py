import csv
import utils
def createCSVFile(listOfData):
	with open('csv/users.csv', 'w', newline='') as file:
    	 writer = csv.writer(file, delimiter=',')
    	 writer.writerows(listOfData)
 