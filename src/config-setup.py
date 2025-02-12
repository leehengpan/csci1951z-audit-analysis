import json

initializer_bank = {
    'School Name': ['Brown University', 'Massachusetts Institute of Technology', 'University of Chicago',
                    'Boston University', 'University of Rhode Island', 'Illinois Institute of Technology',
                    'Peking University', 'National Taiwan University', 'Central University'],
    'Degree': ["Bachelor's", "Master's", 'PhD'],
    'Location': ['02912', '78712', '48226', '33101', '06520', '43004', '15213', '47401', '98039', '10001', '02108'],
    'Gender': ['M', 'F', 'N/A'],
    'Veteran status': [1, 0, 'N/A'],
    'Work authorization': [1, 0],
    'Disability': [1, 0, 'N/A'],
    'Ethnicity': ['White', 'Black', 'Native American', 'Asian', 'Pacific Islander'],
    'GPA': None, 'job_histories': {
        '0': ['Financial Manager', '11/22', 'N/A', 'Senior Financial Analyst', '11/18', '10/22',
              'Junior Financial Analyst', '11/16', '09/18'],
        '1': ['Analyst', '10/17', '12/19', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        '2': ['Lead Analyst', '10/23', 'N/A', 'Senior Analyst', '10/22', '10/23', 'N/A', 'N/A', 'N/A'],
        '3': ['Junior Financial Analyst', '10/22', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        '4': ['Financial Manager', '12/23', 'N/A', 'Senior Financial Analyst', '11/22', '12/23',
              'Junior Financial Analyst', '10/20', '10/22'],
        '5': ['Junior Economist', '12/20', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        '6': ['Senior Recruiter', '10/21', '12/23', 'Assistant Recruiter', '10/19', '9/21', 'Secretary', '8/16',
              '9/19'],
        '7': ['Senior Financial Manager', '12/22', 'N/A', 'Lead Financial Analyst', '11/20', '12/22',
              'Senior Financial Analyst', '10/18', '10/20'],
        '8': ['VP of Finance', '11/23', 'N/A', 'Senior Financial Manager', '12/19', '10/23', 'Financial Manager',
              '10/16', '12/19'],
        '9': ['Financial Manager', '12/18', '01/24', 'Senior Financial Analyst', '11/15', '12/18',
              'Junior Financial Analyst', '10/12', '10/15'],
        '10': ['Financial Manager', '12/13', '01/24', 'Senior Financial Analyst', '10/11', '12/13',
               'Junior Financial Analyst', '10/08', '10/11'],
        '11': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']}}

with open("../data/datagen-config.json", "w+") as f:
    json.dump(initializer_bank, f)
