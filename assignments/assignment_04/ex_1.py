"""
    Open the file './data/befkbhalderstatkode.csv'
    Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
    Using this data:

    neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
           5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
           10: 'Amager Vest', 99: 'Udenfor'}

    Find out how many people lived in each of the 11 areas in 2015
NOT DONE     Make a bar plot to show the size of each city area from the smallest to the largest in 2015
    Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
NOT DONE    How many of those were from the other nordic countries (not dk). Hint: see notebook: "04 Numpy"
NOT DONE    Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015
"""
import numpy as np

neighb = {
    1: 'Indre By', 
    2: 'Østerbro', 
    3: 'Nørrebro', 
    4: 'Vesterbro/Kgs. Enghave', 
    5: 'Valby', 
    6: 'Vanløse', 
    7: 'Brønshøj-Husum', 
    8: 'Bispebjerg', 
    9: 'Amager Øst', 
    10: 'Amager Vest', 
    99: 'Udenfor'
    }

filename = './data/befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = bef_stats_df

 #mask1 = (dd[:,0] ==  2015) & (dd[:,2] == 0) & (dd[:,3] == 5180)
 #print (dd[mask1])



def people_by_area():
    year_mask = dd[:, 0] == 2015
    set_of_areas = np.unique(dd[:, 1])
    freq_areas = np.array(
        [np.sum(dd[year_mask & (dd[:, 1] == area)][:, 4]) for area in set_of_areas]
    )
    dict_from_list = dict(zip(set_of_areas, freq_areas))
    return dict_from_list




def people_over_sixtyfive():
    mask = (dd[:,0] == 2015) & (dd[:,2] > 65)
    return int(sum(dd[mask][:, 4]))



if __name__ == "__main__":
    #print(people_by_area())
    print(people_over_sixtyfive())