import requests
class Website:
    global website_dictionary
    website_dictionary = {'Bauhaus':'bauhaus.dk','Jem&Fix':'jemogfix.dk'}
    def __init__(self,website):
        self.site = website_dictionary[f'{website}']