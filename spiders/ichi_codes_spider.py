import scrapy
import json
import couchdb
import time
import csv

class ichi_spider(scrapy.Spider):

    name='ichi_spider'

    def __init__(self):
        couchserver = couchdb.Server("http://127.0.0.1:5984/")
        self.db = couchserver["ichi_codes"]

    def start_requests(self):
        code_urls = []

        for uri in range(11663, 17455):
    	   code_url="https://mitel.dimi.uniud.it/ichi/php/ajax/entities/load_entity.php?vid=4&entity=ichi&uri=" + str(uri)
           code_urls.append(code_url)

        for url in code_urls:  
    	   yield scrapy.Request(
    		url = url
    		, 
    		headers={
    	 	'Host': 'mitel.dimi.uniud.it'
    	 	,'Accept': 'application/json, text/javascript, */*; q=0.01'
    	 	,'X-Requested-With': 'XMLHttpRequest'
    	 	,'Referer': 'https://mitel.dimi.uniud.it/ichi/'
    	 	})
           time.sleep(0.1)

    def parse(self, response):
        data = json.loads(response.text)
    	content = data['data']['content']

        codes_json = 'codes.json'
        # self.db.save(content)
    	with open(codes_json, 'ab') as f:
    	 	f.write(json.dumps(content))

        # save json 

        codes_csv = 'codes.csv'
        # csf_writer.writerow(["Code","Target","Action","Means","Descriptor","Inclusion Terms"])
        with open(codes_csv, 'ab') as f:
            csf_writer = csv.writer(f)
            csf_writer.writerow([content["code"], 
                content["target_code"] + "-" + content["target_title"], 
                content["action_code"] + "-" + content["action_title"], 
                content["means_code"] + "-" + content["means_title"],
                content["descriptor"],
                content["inclusion_terms"],
                content["includes_notes"],
                content["excludes_notes"]])
            