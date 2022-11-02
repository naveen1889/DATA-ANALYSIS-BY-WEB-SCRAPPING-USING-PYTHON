import scrapy


class makaan_spider(scrapy.Spider):
    name = 'MAKAAN'
    allowed_domains = ['www.makaan.com']
    #start_urls=['https://www.makaan.com/hyderabad-residential-property/buy-property-in-hyderabad-city?page=2']

    url = 'https://www.makaan.com/hyderabad-residential-property/buy-property-in-hyderabad-city?page={}'

    def start_requests(self):
        for i in range(2,4):
            yield scrapy.Request(url=self.url.format(i))

    def parse(self, response):
        properties=response.css('li.cardholder')
        for property in properties:
            title= ' '.join(property.css('div.title-line  a[data-type="listing-link"] strong span::text').getall())
            projectname= property.css('div.title-line  strong a.projName span::text').get()
            builder= property.css('a.seller-name span::text').get()
            val=float(property.css('div[data-type="price-link"] span.val::text').get())
            uni=property.css('div[data-type="price-link"] span.unit::text').get()
            if uni==' L':
                    val=val*100000
            if uni==' Cr':
                    val=val*10000000
            price=int(val)
            per_sqft=property.css('td.lbl.rate::text').get()
            area= property.css('td.size span::text').get()
            status=property.css('tr.hcol.w44 td.val::text').get()
            place=property.css('a.loclink span strong::text').get()

            item={
                'title':title,
                'projectname':projectname,
                'builder':builder,
                'price':price,
                'per_sqft':per_sqft,
                'area':area,
                'status':status,
                'place':place,
            }
            yield item
       