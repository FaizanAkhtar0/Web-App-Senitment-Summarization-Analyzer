from Analyzer.models_lib.sentiment_analyzer import SentimentAnalyzer
from Analyzer.models_lib.summarization_analyzer import SummarizationAnalyzer

analyzer = SentimentAnalyzer()

analyzer_summaray = SummarizationAnalyzer()

text = """sir now we have no trust on u anymore really you r a liar man nd liar politician u nt deserve respect anymore coz liar man have no respect at all u loss ur respect by ignoring the voice of youth."""

print(analyzer.Sentiment(text))

txt_2 = """We Are Living In A Society Where Instead Of Finding Solutions For A Problem Our Government
@ImranKhanPTI

 Just Bans It . Sadly We Don't Have Any Platforms Like Amazon, PayPal,BC And Many More Instead Of Making A development Progress We Are Going Downward"""

print(analyzer.Sentiment(txt_2))

txt_3 = """I haven't had Dominos pizza in at least 20 years! I only visited this time because they were promoting their annual Sick Kids hospital day. You can buy a pepperoni or cheese pizza, medium (14 inch) for $4.65 ($5.00 incl tax) and they will donate $2.00 to Sick Kids Hospital. They freshly made the pizza. We bought the pepperoni pizza. It was extremely fresh. The crust was crunchy and the dough was chewy, just the way I like Amazing! I loved it It is the best plain pepperoni pizza I've ever had! We ordered 2 more to bring home. The place itself was on the small side but very clean."""

print(analyzer.Sentiment(txt_3))

txt_4 = """When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, now the co-founder and CEO of online higher education startup Udacity, in an interview with Recode earlier this week.

A little less than a decade later, dozens of self-driving startups have cropped up while automakers around the world clamor, wallet in hand, to secure their place in the fast-moving world of fully automated transportation."""


paragraph = """In the near term, the goal of keeping AI’s impact on society beneficial motivates research in many areas, from economics and law to technical topics such as verification, validity, security and control.
Whereas it may be little more than a minor nuisance if your laptop crashes or gets hacked, it becomes all the more important that an AI system does what you want it to do if it controls your car, your airplane, your pacemaker, your automated trading system or your power grid.
Another short-term challenge is preventing a devastating arms race in lethal autonomous weapons.
In the long term, an important question is what will happen if the quest for strong AI succeeds and an AI system becomes better than humans at all cognitive tasks. As pointed out by I.J.
Good in 1965, designing smarter AI systems is itself a cognitive task. Such a system could potentially undergo recursive self-improvement, triggering an intelligence explosion leaving human intellect far behind.
By inventing revolutionary new technologies, such a superintelligence might help us eradicate war, disease, and poverty, and so the creation of strong AI might be the biggest event in human history.
Some experts have expressed concern, though, that it might also be the last, unless we learn to align the goals of the AI with ours before it becomes superintelligent.
There are some who question whether strong AI will ever be achieved, and others who insist that the creation of superintelligent AI is guaranteed to be beneficial. At FLI we recognize both of these possibilities, but also recognize the potential for an artificial intelligence system to intentionally or unintentionally cause great harm.
We believe research today will help us better prepare for and prevent such potentially negative consequences in the future, thus enjoying the benefits of AI while avoiding pitfalls."""


print(' '.join(analyzer_summaray.Summarize(paragraph)))