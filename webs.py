import requests
from bs4 import BeautifulSoup

result = requests.get("http://www.sportingnews.com/us/nba/news/lebron-james-stunned-magic-johnson-resignation-from-lakers/1ih84sn0hamqo18hucphisucrg")
print(result.status_code)

print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

    print(urls)

    #using objects 
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>SPORTING NEWS</title></head>
<body>
<p class="title"><b>lebron james stunned after magic johnson retires</b></p>

<p class="story">LeBron James was "stunned" by Johnson's decision. Additionally, Johnson and general manager Rob Pelinka met Saturday with James and his agent, Rich Paul, and there was no indication Johnson was going to make such a big announcement. 
<a href="http://www.sportingnews.com/us/nba/news/lebron-james-stunned-magic-johnson-resignation-from-lakers/1ih84sn0hamqo18hucphisucrg" class="sister" id="link">Lebron james</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Sporting news<a/a>;
With the sudden change in the Lakers' front office, ESPN reports the plan right now is for Pelinka to stay in his position and he likely will earn more power.  

</p>
<p class="story">....</p>

<b class="boldest">More news</b>
<blockquote class="boldest">"I was happier when I wasn’t the president. When you have to make trades, you’re not happy, when you like people. I think Luke is a good man. I like Luke a lot. So what we have different opinions about different things. That’s ok. My concern is my relationship with my sister, Jeanie Buss. That’s all I care about. All the rest of the stuff doesn’t matter."</blockquote>
<b id="1">Malvin Johnson hearbreaking Quote</b>
<blockquote class="boldest">"<blockquote class="boldest">"I was happier when I wasn’t the president. When you have to make trades, you’re not happy, when you like people. I think Luke is a good man. I like Luke a lot. So what we have different opinions about different things. That’s ok. My concern is my relationship with my sister, Jeanie Buss. That’s all I care about. All the rest of the stuff doesn’t matter."</blockquote>"</blockquote>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

with open('dataFromSportinggoods.txt', 'w') as f:
    f.write(html_doc)

    soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())
# for link in links:
#     if "about" in link.text:
#         print(link)
#         print(link.attrs['href'])
# =========================================================================================
# Website 2
#==========================================================================================
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.theverge.com/tech")
print(result.status_code)

print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

    print(urls)

    #using objects 
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>Today's Top Picks: Two motivation plays for NBA's regular season finale, plus an MLB total to jump on</title></head>
<body>
<p class="title"><b>Amazon’s Alexa isn’t just AI — thousands of humans are listening</b></p>

<p class="story">Amazon, like many other tech companies investing heavily in artificial intelligence, has always been forthright about its Alexa assistant being a work in progress. “The more data we use to train these systems, the better Alexa works, and training Alexa with voice recordings from a diverse range of customers helps ensure Alexa works well for everyone,” reads the company’s Alexa FAQ.


<a href="https://www.theverge.com/2019/4/10/18305378/amazon-alexa-ai-voice-assistant-annotation-listen-private-recordings" class="sister" id="link">Lebron james</a>,
# <a href="https://www.theverge.com/tech" class="sister" id="link2">Tech News<a/a>;
n many cases, human beings make those calls, by listening to a recording of the exchange and correctly labeling the data so that it can be fed back into the system. That process is very broadly known as supervised learning, and in some cases it’s paired with other, more autonomous techniques in what’s known as semi-supervised learning. Apple, Google, and Facebook all make use of these techniques in similar ways, and both Siri and Google Assistant improve over time thanks to supervised learning requiring human eyes and ears

</p>
<p class="story">....</p>

<b class="boldest">More news</b>
<blockquote class="boldest">"In this case, Bloomberg is shedding light on the army of literal thousands of Amazon employees, some contractors and some full-time workers, around the world that are tasked with parsing Alexa recordings to help improve the assistant over time. While there’s certainly nothing inherently nefarious about this approach, Bloomberg does point out that most customers don’t often realize this is occurring. Additionally, there’s room for abuse. Recordings might contain obviously identifiable characteristics and biographical information about who is speaking. It’s also not known how long exactly these recordings are stored, and whether the information has ever been stolen by a malicious third party or misused by an employee."</blockquote>
<b id="1">AMAZON STORES THOUSANDS OF VOICE RECORDINGS, AND IT’S UNCLEAR IF THERE’S EVER BEEN MISUSE</b>
<blockquote class="boldest">"<blockquote class="boldest">"Amazon is actively looking for ways to move away from the kind of supervised learning that that requires extensive transcribing and annotation. Wired noted in a report late last year about how Amazon is using new, more cutting-edge techniques like so-called active learning and transfer learning to cut down on error rates and to expand Alexa’s knowledge base, even as it adds more skills, without requiring it add more humans into the mix."</blockquote>"</blockquote>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

with open('dataFromVergeNews.txt', 'w') as f:
    f.write(html_doc)

    soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())
# for link in links:
#     if "about" in link.text:
#         print(link)
#         print(link.attrs['href'])
# =================================================================
# Website 3
#==================================================================

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.foxnews.com/politics/dems-rage-against-barr-for-backing-claims-of-trump-campaign-spying-by-fbi")
print(result.status_code)

print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

    print(urls)

    #using objects 
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>FoxNews</title></head>
<body>
<p class="title"><b>Dems rage against Barr for backing claims of Trump campaign ‘spying’ by FBI</b></p>

<p class="story">Prominent Democrats lined up to hammer Attorney General Bill Barr for testifying Wednesday that federal authorities had spied on the Trump campaign in 2016, with one top House Democrat charging that Barr is not acting "in the best interest of the DOJ or the country."


<a href="https://www.foxnews.com/politics/dems-rage-against-barr-for-backing-claims-of-trump-campaign-spying-by-fbi" class="sister" id="link">Lebron james</a>,
# <a href="https://www.foxnews.com/politics/dems-rage-against-barr-for-backing-claims-of-trump-campaign-spying-by-fbi" class="sister" id="link2">Tech News<a/a>;
Despite mounting evidence that the FBI pursued an array of efforts to gather intelligence from within the Trump campaign -- and the fact that the FBI successfully pursued warrants to surveil a former Trump aide in 2016 -- House Majority Leader Steny Hoyer, D-Md., told Fox News that Barr's loyalties were compromised.

</p>
<p class="story">....</p>

<b class="boldest">More news</b>
<blockquote class="boldest">"House Intelligence Committee Chairman Adam Schiff, D-Calif., added in a statement that Barr "should not casually suggest that those under his purview engaged in ‘spying’ on a political campaign.""</blockquote>
<b id="1">COMEY MEMOS CONTAINED FAR MORE CLASSIFIED INFO THAN PREVIOUSLY KNOWN</b>
<blockquote class="boldest">"Trump, for his part, has vowed to release surveillance warrant applications used to monitor his former aide, Carter Page, beginning in October 2016. The FBI's partisan sources in those applications have come under scrutiny, and FBI text messages obtained by Fox News show high-level concerns at the DOJ as to the credibility of sources presented to the Foreign Intelligence Surveillance Act (FISA) court."</blockquote>"</blockquote>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

with open('dataFromFox.txt', 'w') as f:
    f.write(html_doc)

    soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())
# for link in links:
#     if "about" in link.text:
#         print(link)
#         print(link.attrs['href'])

# ====================================================
# Website 4
#====================================================
import requests
from bs4 import BeautifulSoup

result = requests.get("https://wsuathletics.com/")
print(result.status_code)

print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

    print(urls)

    #using objects 
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>wayne state university </title></head>
<body>
<p class="title"><b>Women's Basketball Reads at Hamilton Elementary</b></p>

<p class="story">Eleven (11) of the Warrior student-athletes and head coach Carrie Lohr took time to read to students between kindergarten and fifth grade.  During the three hours they spent at the school, WSU divided into groups and rotated every 20 minutes, reading in 18 different classrooms.


<a href="https://wsuathletics.com/" class="sister" id="link">Lebron james</a>,
# <a href="https://wsuathletics.com/" class="sister" id="link2">Tech News<a/a>;
Reading to the students at Hamilton Elementary was a wonderful experience," commented freshman Alexis Miller (Howell, Mich.).  "It was amazing to help educate younger students on the importance of hard work and determination.  I had so much fun with the kids and I was happy to give back to the community."

</p>
<p class="story">....</p>

<b class="boldest">More news</b>
<blockquote class="boldest">"What was once a vacant retail space in the heart of campus was transformed into the W Food Pantry, which has provided students in need with free access to nutritious food and basic necessities, all while uniting the campus community and breaking down stigmas.""</blockquote>
<b id="1">Helping where it’s needed most: The W Food Pantry celebrates anniversary, growing impact</b>
<blockquote class="boldest">"“It’s incredible to see how the campus community has embraced The W so fully, so soon,” said Rainesha Williams-Fox, coordinator of student life wellness. “The reality is that there are college students — here and across the country — experiencing food insecurity.  Wayne State is working to remove that barrier and provide assistance, without judgment, wherever possible. No student should have to choose between buying textbooks or buying food.”"</blockquote>"</blockquote>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

with open('datafromWayneStateUniverity.txt', 'w') as f:
    f.write(html_doc)

    soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())
# for link in links:
#     if "about" in link.text:
#         print(link)
#         print(link.attrs['href'])

#============================================
# Website 5
#============================================
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.forbes.com/sites/gordonkelly/2019/04/09/apple-iphone-pro-upgrade-new-iphone-xs-max-xr-price-cost/#10c5861044de")
print(result.status_code)

print(result.headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

    print(urls)

    #using objects 
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>FORBES NEWS </title></head>
<body>
<p class="title"><b>'iPhone Pro' Leak Reveals Apple's Expensive Surprise</b></p>

<p class="story">Alongside the expected iPhone XS, iPhone XS Max and iPhone XR updates, Mac Otakara says Apple is preparing additional 6.1-inch and 6.5-inch models with OLED displays, thinner chassis, similar triple array cameras but with larger sensors, reverse wireless charging and bundled 18W Lightning-to-USB-C fast chargers.


<a href="https://www.forbes.com/sites/gordonkelly/2019/04/09/apple-iphone-pro-upgrade-new-iphone-xs-max-xr-price-cost/#10c5861044de" class="sister" id="link">Lebron james</a>,
# <a href="https://www.forbes.com/sites/gordonkelly/2019/04/09/apple-iphone-pro-upgrade-new-iphone-xs-max-xr-price-cost/#10c5861044de" class="sister" id="link2">Tech News<a/a>;
Mac Otakara previously stated the new XS, XS Max and XR updates will ship with slow chargers and identical chassis while the XR will retain its cheaper LCD display. All of which indicates the introduction of a new flagship iPhone tier above the XSes - potentially the long expected ‘iPhone Pro’ range.

</p>
<p class="story">....</p>

<b class="boldest">More news</b>
<blockquote class="boldest">"If correct, I think this is madness. Yes, Samsung has launched four Galaxy S10 models and no less than four Galaxy Note 10 models are expected to join them, but this is because of a split between 5G and 4G versions. 5G isn’t available everywhere and the hardware carries a significant price premium, so the additional versions make sense.

""</blockquote>
<b id="1">But iPhones will not have 5G this year</b>
<blockquote class="boldest">"“Yes, Apple has one truly radical folding iPhone in development and a crowd-pleasing iPhone SE2 may arrive in 2020. But jacking up prices for an incrementally improved new flagship iPhone range is not how you win fans while they wait…

”"</blockquote>"</blockquote>
<b another-attribute="1" id="verybold">Test 2</b>
<p id="my id"></p>
"""

with open('dataFromForbesNews.txt', 'w') as f:
    f.write(html_doc)

    soup = BeautifulSoup(html_doc, "lxml")

print(soup.prettify())
# for link in links:
#     if "about" in link.text:
#         print(link)
#         print(link.attrs['href'])