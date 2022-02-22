import datasheet as datasheet

class student(datasheet):

    name = ''
    gender = ''
    datasheet = datasheet
    image_url = ''


    def __init__(self,name, gender, datasheet, image_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url




def get_avg_grade():
    print("")