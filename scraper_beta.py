import scrapy 
import logging

#f = open('items.csv', 'w').close()

class Beta_scraper(scrapy.Spider):
	name = "SCRAPER MEDICAL V.0"
	start_urls = ['https://www.vulgaris-medical.com/forum-sante/zolpidem-stilnox']
	handle_httpstatus_list = [404]


	# def parse(self, response ):
	# 	parse_forum(self, response)

	# def parse_forum(self, response):

	# 	post_selector='.forum-row-wrapper'
	# 	for post in response.css(post_selector):
	# 		post_link_selector = 'a ::attr(href)'
	# 		post_link = response.css(post_link_selector).extract_first()
	# 		if post_link:
	# 			yield self.parse_post(response.urljoin(post_link))


	def parse(self, response):
		
		#retrieve first post
		post_selector = '.forum-post-content-wrapper'
		for message in response.css(post_selector):
			sentence_selector = ' p ::text'
			yield {
				'sentence (OP)': message.css(sentence_selector).getall()
			}
		#retrieve comments 
		comment_selector='.comment-body-wrapper'
		for comment in response.css(comment_selector):
			sentence_selector = ' p ::text'
			yield {
				'sentence (comment)': comment.css(sentence_selector).getall()
			}
			
		next_page_selector = '.pager-next a ::attr(href)'
		next_page = response.css(next_page_selector).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse
			)
