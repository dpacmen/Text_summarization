# coding: utf-8
import pysummarizer.summarizer as Module

py = Module.PySummarizer()

#text = "But using a little bit of sense I feel you should not have tried to project yourself as a political superstar with the eight pm announcement of withdrawal as legal tender especially when it is something that affects the common man’s daily transactions. If at all there was something called secrecy that you and your government should have maintained it should have been the surgical strike for the Uri incident. It should have remained as a military secret. Having travelled in trains and conversed with some militarymen I am aware that there are more happening in the border than what we are supposed to know."
#text = "Firstly let us come to Kashmir stone pelting incidents. It has been more than two months since we heard of any stone pelting. Your action to send our soldiers into Kashmir was good. They brought the area under control and with a few bullets that took the life of stone pelters and their stone pelting children our army gave out a clear message that if the stone pelters continue being committed to Sayeed Hafiz for the money he is giving and pelt stones then our army will be committed to the nation they serve and shoot bullets and it can take more lives. The stone pelting had to stop because stone pelters realized that soliders are not like policemen who have to deal with lathi but the ones who are trained to kill. We are proud of General Bakshi and Major Gaurav Arya who have expressed the soldier’s side too. To apply medicine on bruised wound our soldiers even started the “school chalo” initiative and children of areas brought under control had to go to the schools where our army men have undertaken educating the children too"

text = '''Lior Degani, the Co-Founder and head of Marketing of Swayy, pinged me last week when I was in California to tell me about his startup and give me beta access. I heard his pitch and was skeptical. I was also tired, cranky and missing my kids – so my frame of mind wasn’t the most positive.

    I went into Swayy to check it out, and when it asked for access to my Twitter and permission to tweet from my account, all I could think was, “If this thing spams my Twitter account I am going to bitch-slap him all over the Internet.” Fortunately that thought stayed in my head, and not out of my mouth.

    One week later, I’m totally addicted to Swayy and glad I said nothing about the spam (it doesn’t send out spam tweets but I liked the line too much to not use it for this article). I pinged Lior on Facebook with a request for a beta access code for TNW readers. I also asked how soon can I write about it. It’s that good. Seriously. I use every content curation service online. It really is That Good.

    What is Swayy? It’s like Percolate and LinkedIn recommended articles, mixed with trending keywords for the topics you find interesting, combined with an analytics dashboard that shows the trends of what you do and how people react to it. I like it for the simplicity and accuracy of the content curation. Everything I’m actually interested in reading is in one place – I don’t have to skip from another major tech blog over to Harvard Business Review then hop over to another major tech or business blog. It’s all in there. And it has saved me So Much Time



    After I decided that I trusted the service, I added my Facebook and LinkedIn accounts. The content just got That Much Better. I can share from the service itself, but I generally prefer reading the actual post first – so I end up sharing it from the main link, using Swayy more as a service for discovery.

    I’m also finding myself checking out trending keywords more often (more often than never, which is how often I do it on Twitter.com).



    The analytics side isn’t as interesting for me right now, but that could be due to the fact that I’ve barely been online since I came back from the US last weekend. The graphs also haven’t given me any particularly special insights as I can’t see which post got the actual feedback on the graph side (however there are numbers on the Timeline side.) This is a Beta though, and new features are being added and improved daily. I’m sure this is on the list. As they say, if you aren’t launching with something you’re embarrassed by, you’ve waited too long to launch.

    It was the suggested content that impressed me the most. The articles really are spot on – which is why I pinged Lior again to ask a few questions:

    How do you choose the articles listed on the site? Is there an algorithm involved? And is there any IP?

    Yes, we’re in the process of filing a patent for it. But basically the system works with a Natural Language Processing Engine. Actually, there are several parts for the content matching, but besides analyzing what topics the articles are talking about, we have machine learning algorithms that match you to the relevant suggested stuff. For example, if you shared an article about Zuck that got a good reaction from your followers, we might offer you another one about Kevin Systrom (just a simple example).

    Who came up with the idea for Swayy, and why? And what’s your business model?

    Our business model is a subscription model for extra social accounts (extra Facebook / Twitter, etc) and team collaboration.

    The idea was born from our day-to-day need to be active on social media, look for the best content to share with our followers, grow them, and measure what content works best.

    Who is on the team?

    Ohad Frankfurt is the CEO, Shlomi Babluki is the CTO and Oz Katz does Product and Engineering, and I [Lior Degani] do Marketing. The four of us are the founders. Oz and I were in 8200 [an elite Israeli army unit] together. Emily Engelson does Community Management and Graphic Design.

    If you use Percolate or read LinkedIn’s recommended posts I think you’ll love Swayy.

    ➤ Want to try Swayy out without having to wait? Go to this secret URL and enter the promotion code thenextweb . The first 300 people to use the code will get access.

    Image credit: Thinkstock
'''

print(text)
print("Summary")
#infile = open("/home/deepak/pytext/PySummarizer-master/text.txt", 'r')
#text = infile.read()
#print(text)

summary1 = py.summarize(text)
print(summary1)

print "Original Length %s" % (len(text))
print "Summary Length %s" % len(summary1)
