import requests
import dataset
from bs4 import BeautifulSoup
from pprint import pprint
from urlparse import urljoin

# Create a basic database 
db = dataset.connect('sqlite:///data.db')

# The base url target
BASE_URL = 'http://www.alexa.com/'

def scrape_referrals():
    """ Scrape all the referrals from a list """
    
    #get website content, usually a page with many link targets
    response = requests.get(BASE_URL + "topsites/")

    # parse HTML using Beautiful Soup
    soup = BeautifulSoup(response.content)

    # find all the target links on the page.
    referrals = soup.find_all('p', {'class':'desc-paragraph'})

    # Get all the links to missed connection pages:
    for referral in referrals:
        
        # for each span list, find the "a" tag which represents the link to the missed connection page.
        link = referral.find('a').attrs['href']
        
        # join this relative link with the BASE_URL to create an absolute link
        url = urljoin(BASE_URL, link)
        
        # pass this url to a function (defined below) to scrape info about that referral
        scrape_referral(url)
        
def scrape_referral(url):
    """ Extract referral urls from page. """

    # retrieve the missed connection with requests
    response = requests.get(url)

    # Parse the html of the missed connection post
    soup = BeautifulSoup(response.content)

    # Site Profile
    target = soup.find("h2", text="Site Overview")
    site_url = target.find_next("a")
    
    # Bounce Rate
    target = soup.find("h4", text="Bounce Rate")    
    bounce_rate = target.find_next("strong")
    bounce_rate_change = bounce_rate.find_next("span")

    # Daily Pageviews  
    target = soup.find("h4", text="Daily Pageviews per Visitor")   
    daily_pageviews = target.find_next("strong")
    #print daily_pageviews.text
    daily_pageviews_change = daily_pageviews.find_next("span")
    #print daily_pageviews_change.text

    # Average Time on Site
    target = soup.find("h4", text="Daily Time on Site")   
    daily_time_on_site = target.find_next("strong")
    #print daily_time_on_site.text
    daily_time_on_site_change = target.find_next("span")
    #print daily_time_on_site_change.text

    # referral sites
    target = soup.find("strong", text="Upstream Sites")
    
    referral1 = target.find_next("a")
    #print referral1.text
    referral1_pct = referral1.find_next("span") 
    #print referral1_pct.text
    
    referral2 = referral1_pct.find_next("a")
    #print referral2.text
    referral2_pct = referral2.find_next("span") 
    #print referral2_pct.text
    
    referral3 = referral2_pct.find_next("a")
    #print referral3.text
    referral3_pct = referral3.find_next("span") 
    #print referral3_pct.text    
    
    referral4 = referral3_pct.find_next("a")
    #print referral4.text
    referral4_pct = referral4.find_next("span") 
    #print referral4_pct.text 
    
    referral5 = referral4_pct.find_next("a")
    #print referral5.text
    referral5_pct = referral5.find_next("span") 
    #print referral5_pct.text
    
    # inbound domains
    target = soup.find("h5", text="Total Sites Linking In")
    total_inbound_domains = target.find_next("span")
    #print total_inbound_domains.text

    #referral pages
    referral_page1 = total_inbound_domains.find_next('a', class_="word-wrap")
    #print referral_page1.text
    
    referral_page2 = referral_page1.find_next('a', class_="word-wrap")
    #print referral_page2.text
    
    referral_page3 = referral_page2.find_next('a', class_="word-wrap")
    #print referral_page3.text
    
    referral_page4 = referral_page3.find_next('a', class_="word-wrap")
    #print referral_page4.text
    
    referral_page5 = referral_page4.find_next('a', class_="word-wrap")
    #print referral_page5.text
    
    #top_subdomains
    target = soup.find("th", text="Subdomain")
    
    subdomain1 = target.find_next('span')
    #print subdomain1.text
    subdomain1_pct = subdomain1.find_next('span')
    #print subdomain1_pct.text
    
    subdomain2 = subdomain1_pct.find_next('span')
    #print subdomain2.text
    subdomain2_pct = subdomain2.find_next('span')
    #print subdomain2_pct.text
    
    subdomain3 = subdomain2_pct.find_next('span')
    #print subdomain3.text
    subdomain3_pct = subdomain3.find_next('span')
    #print subdomain3_pct.text
    
    subdomain4 = subdomain3_pct.find_next('span')
    #print subdomain4.text
    subdomain4_pct = subdomain4.find_next('span')
    #print subdomain4_pct.text
    
    subdomain5 = subdomain4_pct.find_next('span')
    #print subdomain5.text
    subdomain5_pct = subdomain5.find_next('span')
    #print subdomain5_pct.text
    
    data = {
        #Site Profile
        'site_url':site_url.text,
        
        #Engagement metrics
        'bounce_rate': bounce_rate.text,
        'bounce_rate_change': bounce_rate_change.text,
    
        'daily_pageviews': daily_pageviews.text,
        'daily_pageviews_change': daily_pageviews_change.text,
        
        'daily_time_on_site': daily_time_on_site.text,
        'daily_time_on_site_change': daily_time_on_site_change.text,
        
        #Top Referral Domains
        'referral1': referral1.text,
        'referral1_pct': referral1_pct.text,
        
        'referral2': referral2.text,
        'referral2_pct': referral2_pct.text,
        
        'referral3': referral3.text,
        'referral3_pct': referral3_pct.text,
        
        'referral4': referral4.text,
        'referral4_pct': referral4_pct.text,
        
        'referral5': referral5.text,
        'referral5_pct': referral5_pct.text,
        
        #Total Referral Domains
        'total_inbound_domains': total_inbound_domains.text,
    
        #Top Referral Pages
        'referral_page1': referral_page1.text,
        'referral_page2': referral_page2.text,
        'referral_page3': referral_page3.text,
        'referral_page4': referral_page4.text,
        'referral_page5': referral_page5.text,
    
        #Top Subdomains
        'subdomain1': subdomain1.text,
        'subdomain1_pct': subdomain1_pct.text,
        
        'subdomain2': subdomain2.text,
        'subdomain2_pct': subdomain2_pct.text,
        
        'subdomain3': subdomain3.text,
        'subdomain3_pct': subdomain3_pct.text,
        
        'subdomain4': subdomain4.text,
        'subdomain4_pct': subdomain4_pct.text,
        
        'subdomain5': subdomain5.text,
        'subdomain5_pct': subdomain5_pct.text,
    }
    
    pprint(data)
    
    # Upsert the data into our database 
    db['posts'].upsert(data, ['site_url'])
    
if __name__ == '__main__':
    scrape_referrals()