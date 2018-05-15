import scrapy
import json
class ichi_spider(scrapy.Spider):

    name='ichi_spider'

    def start_requests(self):
    	ichi_root_url="https://mitel.dimi.uniud.it/ichi/php/ajax/tree/load_branch.php?node=%23&vid=4&tsel=Section"

    	yield scrapy.Request(
    		url = ichi_root_url
    		, 
    		headers={
    	 	'Host': 'mitel.dimi.uniud.it'
    	 	,'Accept': 'application/json, text/javascript, */*; q=0.01'
    	 	,'X-Requested-With': 'XMLHttpRequest'
    	 	,'Referer': 'https://mitel.dimi.uniud.it/ichi/'
    	 	})

    def parse(self, response):
    	data =  json.loads(response.text)
    	filename = 'tree.json'
    	with open(filename, 'wb') as f:
    		f.write(response.text)
		     
