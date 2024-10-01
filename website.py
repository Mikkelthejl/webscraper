import requests
import asyncio, aiohttp, json

class Website:
    global website_dictionary
    website_dictionary = {'Bauhaus':'https://www.bauhaus.dk/','Jem&Fix':'jemogfix.dk'}
    
    def __init__(self,website):
        self.site = website_dictionary[f'{website}']
        if website == 'Bauhaus':
            self.sites = ['gulve-fliser','bad-vvs','haven','el-belysning',
                          'trae-byggematerialer','maskiner','maling-tapet','bolig','fritid','vaerktoej-vaerksted','opvarmning','restsalg','varemaerker']
        else:
            return None
            
