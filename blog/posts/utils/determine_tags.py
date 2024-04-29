from collections import Counter
from bs4 import BeautifulSoup

import string
import re

#"can", "since" and "like" all feel like they should not be tags, and therefore, maybe should be in this list
STOP_WORDS = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]

def most_common_words(text, stop_words, n=5):
    soup = BeautifulSoup(text, 'html.parser')

    text_without_tags = soup.get_text()
    words = text_without_tags.lower()
    words = re.sub(r"[^a-zA-Z0-9]+", ' ', words)
    words = [word for word in words.split() if word not in stop_words]
    word_counts = Counter(words)
    
    return [word for word, _ in word_counts.most_common(n)]

## this is my very hacky way of getting the tags to build the database for testing the GET endpoint, ideally this logic would be used in a POST endpoint for creating blogs, outside the scope of this exercise
if __name__ == "__main__":
    text_to_print = []
    text_to_print.append("""# A brief history of the web
Back in the hazy days of 1999, Microsoft introduced an ActiveX component into Internet Explorer 5 that for the first time allowed Javascript within a page to fetch additional content from the server without reloading the entire page. These were heady days, and I remember writing a lot of Internet Explorer-only applications that leveraged this technology to load specific regions of content in response to user interactions.
We never considered writing a whole application like that however; navigation still fetched a brand new page from the server, causing a full reload. There were still multiple `<SCRIPT>` tags per page to load the different Javascript files required, and as this was before build pipe-lines, none of it was minified or compressed.
By 2005, the phrase *Single Page App* (SPA) had started to surface. The entire application could be loaded once, then handled by Javascript on the client. The only round-trips required to the server would be to fetch specific pieces of data used to generate content. 2010 saw the release of BackboneJS and AngularJS, two frameworks that not only provided the building blocks to construct SPAs more effectively, but also provide some organisation for the mountain of Javascript developers had started to write. In 2011 SproutCore 2.0 was renamed to EmberJS, 2013 saw the first version of React, and in 2016 the new version of Angular was released.
SPAs have come in for a lot of justified criticism, in part due to the heavy churn we saw in Javascript frameworks throughout those six years from 2010, and the fact that for a long while many of them offered an objectively worse experience than a traditional server rendered app. However, the last few years have seen a consolidation of ideas, less large breaking changes and a general maturing of the platform.
Are we now ready to see SPAs replace traditional server side rendered (SSR) apps wholesale? """)
    
    text_to_print.append("""One of the most common questions I have been asked since moving here in 2014, is how the work culture between Singapore and New Zealand compares. To be frank, I still don’t feel like I’m qualified to make that comparison, since Media Suite is the first and only place I’ve worked at in New Zealand. I think I’ve struck it lucky! 
I can go on about how Media Suite’s a great place to work, and how awesome the team is, but I feel like that’s now well established in previous blog posts by myself and the team. So I thought, maybe I can share what life is like in Singapore, and how it prepared me for working in NZ instead.
# The Little Red Dot
First up, a bit of background. Singapore is a city-state in South-east Asia, just 1 degree north of the equator. It’s also affectionately called the ‘Little Red Dot’ by Singaporeans, because that’s all you’ll see on a map most of the time. Since way before independence from Britain in 1965, it was (and still is) a major trading port due to its strategic location between the Indian Ocean and South China Sea. 
It merely covers a slightly larger area than Lake Taupo, but has a total population of 5.64 million in 2018, of which 39% are foreign nationals. The citizen population is made up mostly of ethnic Chinese (76.2%), Malays (15.0%), ethnic Indians (7.4%) and Eurasians/others. """)
    
    text_to_print.append("""# Technologies we use
Here at Media Suite we use a range of technologies for our web applications.  Many of our large bespoke projects typically use either Loopback or Django on the server, and [Ember](https://www.emberjs.com/), React or Angular on the client. However, we also have a large number of exciting projects that make use of SilverStripe, a PHP framework designed and built right here in New Zealand.""")
    
    text_to_print.append("""# When 531 People Do Good
Of the 634 people who held an orange Lego brick in their hand yesterday, **531** of them cared enough to give it back.
Those 531 people made a conscious decision to make sure it got to the right place. They decided that making a quick detour to our [Canterbury Tech Summit](http://www.techsummit.nz/) booth was worth it.
This year, Summit-goers showed us we were right to put our faith in people. In the end, 84% of attendees decided to do the right thing.
For those who don’t know, at the Tech Summit this year (just like last year), we opted out of swag bags, and opted in to giving.""")

    text_to_print.append("""Graphic designers are encouraged to tell stories with their designs which take the viewer beyond the surface and resonates more deeply with them. 
However, in practice what does this actually mean, and how does this manifest in the graphic and design process? 
Storytelling in literature takes the form of narrative where the reader journeys through exposition, conflict, rising action and denouement. Looking more broadly at the field of visual design you can easily see the parallels between creating narratives with character and creating scenarios and personas.  A key reference point in literature on this subject is Greek philosopher Aristotle’s writings on persuasion. 
The Interaction Design Foundation outlines in the list below how Aristotle’s seven elements of good storytelling can be applied to planning a project.
* Plot – what are users trying to achieve/overcome?
* Character – who are the users: not just demographically, but what insights do you require to understand what they’re truly like and their real needs?
* Theme – how can you establish a trustworthy presence to them and still set yourself apart from competitors? How do you reflect the overall obstacles users must overcome?
* Diction – what will your design say to users and how? Does a formal/informal tone match what they’d expect to find? How much text is appropriate?
* Melody – will the overall design pattern appear pleasant and predictable to users, moving them emotionally?
* Décor – how will you present everything so the graphics match the setting the users can sense? Is a classic design or a stylised, niche layout in step with their expectations?
* Spectacle – how can you make your design outstanding so users will remember it?""")

    text_to_print.append("""If your only reason for coming to work is to earn some money, then you're missing an opportunity.
Your job should be **fulfilling**<sup>1</sup>
----
1. And fun, and stimulating, and rewarding.  In both senses.""")


    for blog in text_to_print:
        print('--------------------------------')
        print(most_common_words(blog, STOP_WORDS, 5))
        print('--------------------------------')