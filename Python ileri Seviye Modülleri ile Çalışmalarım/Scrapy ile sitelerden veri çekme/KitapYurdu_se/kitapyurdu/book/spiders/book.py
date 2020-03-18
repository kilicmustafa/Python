import scrapy 

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls= [
            "http://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&page=1"
        ]

    file = open("dosya.txt" ,"a" ,encoding="UTF-8")
    k_count = 1
    p_count = 0


    def parse(self ,response):
        names = response.css("div.name.ellipsis  a span::text").extract()
        authors = response.css("div.author span a span::text").extract()
        publishers = response.css("div.publisher span a span::text").extract()


        try:
            i = 0
            while (i < len(names)):
                self.file.write("***************" + str(self.k_count) +  "********************\n")
                self.file.write("Kitap İsmi : " + names[i] + ".\n")
                self.file.write("Yazar : " + authors[i] + ".\n")
                self.file.write("Kitap türü : " + publishers[i] + ".\n")
                self.file.write("********************************************************\n")
                self.k_count += 1
                i += 1
        except:
            continue

        


        next_url = response.css("a.next::attr(href)").extract_first()
        self.p_count += 1

        if next_url is not None and self.p_count != 5:
            yield scrapy.Request(url = next_url,callback = self.parse)
        else:
            self.file.close()