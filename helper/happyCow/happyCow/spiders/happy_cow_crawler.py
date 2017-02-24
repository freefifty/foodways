import scrapy
import csv
import os

# To Run this crawler, navigate to twitterAPI/happyCow
# and execute > scrapy crawl happy_cow_listings
# in terminal

class QuotesSpider(scrapy.Spider):
    name = "happy_cow_listings"

    def start_requests(self):
        urls = [
            'https://www.happycow.net/europe/portugal/lisbon/',
            'https://www.happycow.net/europe/portugal/lisbon/?page=2', 
            'https://www.happycow.net/europe/portugal/lisbon/?page=3',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # write each listing on a separate row in an csv file
        first_row = ["name", "address", "phone", "description", "tags"]
        parent_dir = os.path.abspath(os.path.join(__file__, os.pardir))
        # print(parent_dir + "/../../../../data")
        with open(parent_dir + "/../../../../data/foodways/happy_cow_listings.csv", "a+") as ofile:
            writer = csv.writer(ofile, delimiter=';')
            writer.writerow(first_row);    
            listings = response.css('div.venue-list-item')
            for listing in listings:
                try:
                    name = listing.css('div ul li h4 a::text').extract_first()
                    paragraphs = listing.css('div p::text').extract()
                    address = paragraphs[0]
                    phone = paragraphs[1]
                    tags = paragraphs[4][8:]
                    description = paragraphs[5]
                    # find the lat, long coordinates of each address
                    # print(name, address.strip(), phone, tags, description)
                    # print("________________________________________________________")
                    writer.writerow([name.strip(), address.strip(), phone.strip(), description.strip(), tags.strip()])
                except:
                    print('ERROR crawling a listing....')