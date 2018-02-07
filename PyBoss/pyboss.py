import csv
import os

def format_csv( path ):
	csvpath = os.path.join( path )

	us_state_abbrev = {
	    'Alabama': 'AL',
	    'Alaska': 'AK',
	    'Arizona': 'AZ',
	    'Arkansas': 'AR',
	    'California': 'CA',
	    'Colorado': 'CO',
	    'Connecticut': 'CT',
	    'Delaware': 'DE',
	    'Florida': 'FL',
	    'Georgia': 'GA',
	    'Hawaii': 'HI',
	    'Idaho': 'ID',
	    'Illinois': 'IL',
	    'Indiana': 'IN',
	    'Iowa': 'IA',
	    'Kansas': 'KS',
	    'Kentucky': 'KY',
	    'Louisiana': 'LA',
	    'Maine': 'ME',
	    'Maryland': 'MD',
	    'Massachusetts': 'MA',
	    'Michigan': 'MI',
	    'Minnesota': 'MN',
	    'Mississippi': 'MS',
	    'Missouri': 'MO',
	    'Montana': 'MT',
	    'Nebraska': 'NE',
	    'Nevada': 'NV',
	    'New Hampshire': 'NH',
	    'New Jersey': 'NJ',
	    'New Mexico': 'NM',
	    'New York': 'NY',
	    'North Carolina': 'NC',
	    'North Dakota': 'ND',
	    'Ohio': 'OH',
	    'Oklahoma': 'OK',
	    'Oregon': 'OR',
	    'Pennsylvania': 'PA',
	    'Rhode Island': 'RI',
	    'South Carolina': 'SC',
	    'South Dakota': 'SD',
	    'Tennessee': 'TN',
	    'Texas': 'TX',
	    'Utah': 'UT',
	    'Vermont': 'VT',
	    'Virginia': 'VA',
	    'Washington': 'WA',
	    'West Virginia': 'WV',
	    'Wisconsin': 'WI',
	    'Wyoming': 'WY',
	}

	print("Emp ID,First Name,Last Name,DOB,SSN,State")
	with open(csvpath) as csvDataFile:
	    csvReader = csv.reader(csvDataFile)
	    next(csvReader)
	    for row in csvReader:

	        id = row[0]
	        name = row[1]
	        dob = row[2]
	        ssn = row[3]
	        state = row[4]


	        first_name = str(name).split(" ")[0]
	        last_name = str(name).split(" ")[1]

	        month = str(dob).split("-")[1]
	        day = str(dob).split("-")[2]
	        year = str(dob).split("-")[0]

	        ssn_part1 = '*' * len(str(ssn).split("-")[0])
	        ssn_part2 = '*' * len(str(ssn).split("-")[1])
	        ssn_part3 = str(ssn).split("-")[2]

	        short_state = us_state_abbrev[state]

	        print(str(id) + ',' + str(first_name) + ',' + str(last_name) + ',' + str(day) + '/' + str(month) + '/' + str(year) + ',' + str(ssn_part1) + '-' + str(ssn_part2) + '-' + str(ssn_part3) + ',' + str(short_state) )

format_csv('employee_data1.csv')
format_csv('employee_data2.csv')



