#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI


#Author: T Shrinivasan <tshrinivasan@gmail.com>


# get api from here  https://developers.facebook.com/tools/explorer


api = "EAAUtBuKRRrYBACE8fzyK4KWeZA3bqoRKupVkhMZC8k7d7hywZCLJjiDX5qalrqf40qNzsh7aLkvxotdxQr12Uy4mgI4gBYPB7dcHwaKwrCdZA41hoJGwQ5UwD3oZAEtWohX92USofSyUpkXbnsD9urLbdbncy5enzuQEezEljb6wZBGZCRhURxWsGeropPHYjS9OSFfIqZAZArgZDZD"







graph = GraphAPI(api)

message = 'Check out my gigs for ecommerce, shopify store, woocommerce, web scraping, automation, etc from the following links:' \
		  '1. https://www.fiverr.com/s2/111b4b9ca6?utm_source=CopyLink_Mobile' \
		  '2. https://www.fiverr.com/s2/e18771789c?utm_source=CopyLink_Mobile' \
		  '3. https://www.fiverr.com/s2/ffecd19e9b?utm_source=CopyLink_Mobile' \
		  '4. https://www.fiverr.com/s2/c6a538bd13?utm_source=CopyLink_Mobile'


# Find the ids of your desired groups from http://lookup-id.com/  
# and add this in this array groups

groups = [ 'https://www.facebook.com/groups/getprojectsupwork/?ref=br_rs', 'https://www.facebook.com/groups/1048698711880571/?ref=br_rs', 'https://www.facebook.com/groups/DSEntrepreneurs/?ref=br_rs', 'https://www.facebook.com/groups/580879455292090/?ref=br_rs', 'https://www.facebook.com/groups/fiverrhelpbangladesh/?ref=br_rs', 'https://www.facebook.com/groups/121968305178198/?ref=br_rs', 'https://www.facebook.com/groups/474434189348407/?ref=br_rs', 'https://www.facebook.com/groups/769584619785908/?ref=br_rs', 'https://www.facebook.com/groups/entrepreneurshiptrends/?ref=br_rs']



for group_id in groups:
	print("Posting to " + 'http://www.facebook.com/groups/' + str(group_id))
	graph.post(path=str(group_id) + '/feed', message=message)
	time.sleep(10)
print("Done")
