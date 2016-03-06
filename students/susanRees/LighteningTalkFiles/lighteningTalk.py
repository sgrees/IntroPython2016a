# the program opens the workbook by importing the openpyxl module and calling the openpyxl.load_workbook() function.
import openpyxl
    wb = openpyxl.load_workbook('surveyData.xls')

# calls the get_sheet_by_name function to get the worksheet object
sheet = wb.get_sheet_by_name('Sheet1')

# Use indexing or the cell() sheet method with row and column keyword arguments to pull values from all cells in one column.  puts them into a list (I think the default for this method is a tuple, does that work here or do we need to push it into a list instead)?
rawAgeData = sheet.columns[‘S’]

# puts them in order (alphabetically for strings or numerically for integers) using sorting?  Look up dictionary/list labs
ageDataOrdered = sorted(rawAgeData):

# Using a for loop?  counts the total number of entries, creates dictionary with unique entries (age) as keys, and the number of times each entry appears as value?
for i in ageDataOrdered:
    counts = Counter(ageDataOrdered)

# in new dictionary? iterates through dict values and divides by total number of entries to provide the percentage (new value) of the whole that each unique entry group (keys) represents
# sorts entries (keys) by percentage (value) so we can see the order of importance.
    def report():
    for key, values in (ageDataOrdered.items()):
        numAges = len(key)
        percentAge = int(value/numAges)

# Displays them in a pie (lol) chart or bar graph of some sort?
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
for i in range(1, 11):         # create some data in column A
    sheet['A' + str(i)] = i

refObj = openpyxl.charts.Reference(sheet, (1, 1), (10, 1))

seriesObj = openpyxl.charts.Series(refObj, title='First series')

chartObj = openpyxl.charts.PieChart()   # can also use BarChart
chartObj.append(seriesObj)
chartObj.drawing.top = 50       # set the position
chartObj.drawing.left = 100
chartObj.drawing.width = 300    # set the size
chartObj.drawing.height = 200

sheet.add_chart(chartObj)
wb.save('sampleChart.xlsx')
