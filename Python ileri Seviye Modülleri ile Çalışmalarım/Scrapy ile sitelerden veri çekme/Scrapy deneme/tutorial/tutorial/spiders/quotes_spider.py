import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    a_count = 1
    file = open("data.txt" ,"a" ,encoding="UTF-8")
    start_urls = [
            'http://quotes.toscrape.com/page/1/'
            
        ]
    """def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """
    def parse(self, response):

        
        

        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()

            self.file.write("**************"+ str(self.a_count) + "****************\n")
            self.file.write("ALıntı : " + title +"\n")
            self.file.write("Alıntının sahibi :" + author + "\n" )
            self.file.write("Etiketler" + str(tags) + "\n" )
            self.file.write("******************************\n")
            self.a_count += 1

            yield {
                "title" : title,
                "author" : author,
                "tags" : tags
            }


        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            next_page = "http://quotes.toscrape.com" + next_page
            yield scrapy.Request(url = next_page,callback = self.parse)


        else:

            self.file.close()

    
        
