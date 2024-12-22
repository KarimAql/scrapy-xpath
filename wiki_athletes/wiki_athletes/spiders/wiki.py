import scrapy
import csv

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ["file:///workspaces/scrapy-xpath/html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump"] # Change this to the path of your local HTML file

    def parse(self, response):
        # Locate the table where the data is present
        table = response.xpath('//table')[2]  # Adjust the index if the table is different

        # Extract rows, skipping the header row
        rows = table.xpath('.//tr')[1:]

        # Open CSV file to write the data
        with open('athletes.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write CSV header
            writer.writerow(['Rank', 'Name', 'Nationality', 'Result'])

            # Loop through each row and extract the required information
            for row in rows:
                rank = row.xpath('.//td[1]//text()').get()
                name = row.xpath('.//td[2]//a/text()').get()
                nationality = row.xpath('.//td[3]//span/text()').get()
                result = row.xpath('.//td[4]//b/text()').get()

                # Write the row to the CSV file
                if rank and name and nationality and result:
                    writer.writerow([rank.strip(), name.strip(), nationality.strip(), result.strip()])

        self.log('Data has been extracted to athletes.csv')