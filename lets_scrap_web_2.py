from bs4 import BeautifulSoup
import requests
import csv

# web address from where data is scraped
source = requests.get('https://clutch.co/web-developers?geona_id=13011').text

soup = BeautifulSoup(source, 'lxml')
# provider-info col-md-10

csv_file = open('scraped_data_2.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company', 'Website', 'Location', 'Rating', 'Review Count', 'Hourly Rate', 'Min Project Size'])

for main_container1 in soup.find_all('li', class_='provider provider-row'):

	# print(main_container1.prettify())

	# 1.name
	name = main_container1.find('h3', class_='company_info').a.text.strip()
	print(name)

	# 2.website Link
	main_container2 = soup.find('div', class_='provider-detail col-md-2')
	website_container = main_container1.find('a', class_='website-link__item')['href']
	website_div1 = website_container.split('/')[0]
	website_div2 = website_container.split('/')[2]
	web_link = f'{website_div1}//{website_div2}'
	print(web_link)

	# 3.location
	location = main_container1.find('span', class_='locality').text
	print(location)

	# 4.rating
	rating = main_container1.find('span', class_='rating sg-rating__number').text.strip()
	print(rating)

	# 5. review count
	review_count = main_container1.find('a', class_='reviews-link sg-rating__reviews').text.strip()
	print(review_count)

	# 6. hourly rate
	hourly_rate = main_container1.find('div', class_='list-item custom_popover').span.text
	print(hourly_rate)

	# 7. min project size
	min_project_size = main_container1.find('div', class_='list-item block_tag custom_popover').span.text
	print(min_project_size)
	print()

	csv_writer.writerow([name, web_link, location, rating, review_count, hourly_rate, min_project_size])
	# csv_writer.writerow([location, hourly_rate, min_project_size])

csv_file.close()