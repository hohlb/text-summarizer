# -*- coding: utf-8 -*-

# request a summary for a long text
#
# at http://127.0.0.1:8000/docs we see the cURL command needed:
# curl -X POST "http://127.0.0.1:8000/summaries/" -H  "accept: application/json" -H  "Content-Type: application/x-www-form-urlencoded" -d "text=This+is+a+long+text"
#
# the cURL-to-Python translator at https://curl.trillworks.com/#python then got us the basis for this script:
import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {    
  # using the Wikipedia article about tree squirrels as an example for a long text
  #
  # This text was taken from https://en.wikipedia.org/wiki/Tree_squirrel
  # some parts (e.g. the image captions) were left out.
  # This slightly shortened Wikipedia text is thus publicly available the Creative Commons Attribution-ShareAlike License, https://creativecommons.org/licenses/by-sa/3.0/
  # as explained by https://en.wikipedia.org/wiki/Wikipedia:Reusing_Wikipedia_content#Re-use_of_text_under_Creative_Commons_Attribution-ShareAlike
  'text': '''Tree squirrel

Tree squirrels are the members of the squirrel family (Sciuridae) commonly just referred to as "squirrels". They include over a hundred arboreal species native to all continents except Antarctica and Oceania. They do not form a single natural, or monophyletic group; they are related to others in the squirrel family, including ground squirrels, flying squirrels, marmots, and chipmunks. The defining characteristic used to determine which species of Sciuridae are tree squirrels is dependent on their habitat rather than their physiology. Tree squirrels live mostly among trees, as opposed to those that live in burrows in the ground or among rocks. An exception is the flying squirrel that also makes its home in trees, but has a physiological distinction separating it from its tree squirrel cousins: special flaps of skin called patagia, acting as glider wings, which allows gliding flight.

The best known genus of tree squirrels is Sciurus, which includes the eastern gray squirrel of North America (introduced to Great Britain in the 1870s), the red squirrel of Eurasia, and the North American fox squirrel, among many others. Many tree squirrel species have adapted to human-altered environments such as rural farms, suburban backyards and urban parks; and because they are diurnal (active during the daytime) they have become perhaps the most familiar wildlife to most humans.

Relationship with humans
Squirrels are generally inquisitive and persistent animals. In residential neighborhoods, they are notorious for tenaciously trying to circumvent obstacles in order to eat from bird feeders. Although they are expert climbers, and primarily arboreal, some species of squirrels also thrive in urban environments, where they have adapted to humans.

As pests

Squirrels are sometimes considered pests because of their propensity to chew on various edible and inedible objects, and their stubborn persistence in trying to get what they want. Their characteristic gnawing trait also aids in maintaining sharp teeth, and because their teeth grow continuously, prevents their over-growth. On occasion, squirrels will chew through plastic and even metal to get to food.

Tree squirrels may bury food in the ground for later retrieval. Squirrels use their keen sense of smell to search for buried food, but can dig numerous holes in the process. This may become an annoyance to gardeners with strict landscape requirements, especially when the garden contains edibles.

Homeowners in areas with a heavy squirrel population must be vigilant in keeping attics, basements, and sheds carefully sealed to prevent property damage caused by nesting squirrels. A squirrel nest is called a "drey".

Squirrels are a serious fire hazard when they break into buildings. They often treat exposed power cables as tree branches, and gnaw on the electrical insulation. The resulting exposed conductors can short out, causing a fire. For this reason alone, squirrel nests inside buildings cannot be safely ignored. A squirrel nest will also cause problems with noise, excreta, unpleasant odors, and eventual structural damage.

Some homeowners resort to more interesting ways of dealing with this problem, such as collecting and placing fur from pets such as domestic cats and dogs in attics. It is hoped that this fur would indicate to nesting squirrels that a potential predator roams, and will encourage evacuation. Odoriferous repellents, including mothballs and ammonia, are generally ineffective in expelling squirrels from buildings.
This squirrel looking for a treat has become desensitized to humans. The distance between the squirrel and the camera was less than 18 in (46 cm).

Once established in a nest, squirrels stubbornly ignore fake owls and scarecrows, along with bright flashing lights, loud noises, and ultrasonic or electromagnetic devices. However, squirrels must leave the nest to obtain food and water (usually daily, except in bad weather), affording an opportunity to trap them or exclude them from re-entering.

To discourage chewing on an object, it can be coated or covered with something to make it distasteful: for instance a soft cloth doused with chili pepper paste or powder. Capsaicin and Ro-pel are other forms of repellent. To remain effective, the coating must be renewed regularly, especially if it is exposed to the weather. Poisoning squirrels can be problematic because of the risks to other animals or children in the building, and because the odor of a dead squirrel in an attic or wall cavity is very unpleasant and persistent.

Trapping is often necessary to remove squirrels from residential structures. Effective baits include fruit, peanut butter, nuts, seeds and vanilla extract.

An alternative method is to wait until squirrels have left in search of food, and then close up all their access openings, or to install one-way trap doors or a carefully angled pipe. Attempting to get rid of all squirrels in a neighborhood is generally a futile goal; the focus instead should be on physically excluding them from places where they can do damage. There are other humane techniques to remove squirrels from buildings, but removal is ineffective unless steps are taken to prevent them from immediately breaking in again.

Squirrels are often the cause of power outages. They can readily climb a power pole and crawl or run along a power cable. The animals will climb onto power transformers or capacitors looking for food, or a place to cache acorns. If they touch a high voltage conductor and a grounded portion of the enclosure at the same time, they are electrocuted, and often cause a short circuit that shuts down equipment. Squirrels have brought down the high-tech NASDAQ stock market twice and were responsible for a spate of power outages at the University of Alabama. To sharpen their teeth, squirrels will often chew on tree branches or even the occasional live power line. Rubber or plastic plates, or freely rotating sleeves ("squirrel guards") are sometimes used to discourage access to these facilities.

Squirrels otherwise appear to be safe and pose almost zero risk of transmitting rabies.

Squirrels cause economic losses to homeowners, nut growers, and forest managers in addition to damage to electric transmission lines. These losses include direct damage to property, repairs, lost revenue and public relations. While dollar costs of these losses are sometimes calculated for isolated incidents, there is no tracking system to determine the total extent of the losses.
As roadkill and traffic hazards

In regions where squirrels are plentiful, tire-flattened roadkill is a common sight on roadways, especially in the spring and fall, when there is a fresh crop of young rodents. Motorists have caused serious accidents by attempting to swerve or stop to avoid a squirrel in the road. Evasive maneuvers are difficult since squirrels are much more agile and have much quicker reaction times than motorists in heavy vehicles; the majority of vehicular encounters end with no harm to either party.

An effort to mitigate these hazards to both squirrels and humans is the Nutty Narrows Bridge in Longview, Washington, listed on the National Register of Historic Places. It provides a way for squirrels to cross a busy street safely.
Tree squirrels are a common attraction of many urban parks.

As urban wildlife

Tree squirrels are a common type of urban wildlife. They can be trained to be hand-fed and will take as much food as is available because they cache the surplus. Squirrels living in parks and campuses in cities have learned that humans are typically a ready source of food. Urban squirrels have learned to get a lot of food from generous or unknowingly 'careless' humans. Humans commonly offer various nuts and seeds; however, wildlife rehabilitators in the field have noted that neither raw nor roasted peanuts nor sunflower seeds are healthy for squirrels, because they are deficient in several essential nutrients. This type of deficiency has been found to cause metabolic bone disease, a somewhat common ailment found in malnourished squirrels.[dubious – discuss]
As food

In the US

Squirrel meat is considered a favored meat in certain regions of the United States where it can be listed as wild game. This is evidenced by a number of recipes for its preparation (e.g. Brunswick stew) found in cookbooks, including James Beard's American Cookery and pre-1997 copies of The Joy of Cooking. Squirrel meat can be substituted for rabbit or chicken in many recipes, though it may have a gamey taste if handled improperly.

Although squirrel meat is low in fat content, unlike most game meat it has been found by the American Heart Association to be high in cholesterol.

In many areas of the US squirrels are still hunted for food, as they were in earlier years. Squirrel meat was an ingredient in the original recipe for Brunswick stew, a popular dish in various parts of the Southern U.S. Other similar stews were also based on squirrel meat, including burgoo and Southern Illinois chowder.

In the UK

For most of the history of the United Kingdom, squirrel has been a meat not commonly eaten, and even scorned by many. In the early 21st century however, wild squirrel has become a more popular meat to cook with, showing up in restaurants and shops more often in Britain as a fashionable alternative meat. Specifically, UK citizens are cooking with the invasive gray squirrel, which is praised for its low fat content and the fact that it comes from free range sources. Additionally, the novelty of a meat considered unusual or special has contributed to the spread of squirrel consumption. Due to the difficulty of a clean kill and other factors, the majority of squirrel eaten in the UK is acquired from professional hunters, trappers and gamekeepers.

Some Britons are eating the gray squirrel as a direct attempt to help the native red squirrel, which has been dwindling since the 19th-century introduction of the gray squirrel, resulting in dramatic habitat loss for the indigenous red squirrels. This factor was marketed by a national "Save Our Squirrels" campaign that used the slogan, "Save a red, eat a grey!"
Risks of eating

As with other wild game and fish species, the consumption of squirrels that have been exposed to high levels of pollution or toxic waste poses a health risk to humans. In 2007 in the northern New Jersey community of Ringwood, the New Jersey Department of Health and Senior Services issued a warning to anyone who eats squirrel (especially for children and pregnant women) to limit their consumption after a lead-contaminated squirrel was found near the Ringwood Mines Landfill. Toxic waste had been illegally dumped at this location for many years, before authorities cracked down on this practice in the 1980s. The warning especially affects the local Ramapough Mountain Indians, who have hunted and consumed squirrels from before European contact. The hunting and eating of squirrels is considered to be one of this people's time-honored traditions, linking them through a process of cultural identity to their ancestors, and to each other. On learning of the ban on squirrel meat consumption, one member of the Ramapough Tribe told a reporter, "I feel my ancestry is disappearing, my heritage".

In 1997, doctors in Kentucky warned of possible hazards from eating squirrel brains, which are considered a folk delicacy in the region. In western parts of the state, the doctors found a greatly elevated human incidence of Creutzfeldt–Jakob disease, a rarely seen but serious prion-based disorder that causes dementia and eventual death. So-called "mad squirrel disease" can be difficult to distinguish from the usual behavior of squirrels, but could be more prevalent among roadkilled animals. Some squirrel eaters have special rituals for preparing and eating the brain, while others avoid eating it altogether.
In culture
Seventeenth-century Icelandic manuscript illustration depiction Ratatoskr, a squirrel in Norse mythology said to live in the world-tree Yggdrasil and to convey insults and gossip

In the Ramayana, an ancient Sanskrit epic poem, a squirrel assists in constructing a bridge from India to Sri Lanka to help Rama rescue his wife Sita. Rama rewards the squirrel by stroking his back with his three middle fingers, thus giving the Indian palm squirrel the three white stripes that appear on its back. In Norse mythology, the squirrel Ratatoskr is a messenger who scurries up and down the trunk of the world-tree Yggdrasil, carrying malicious gossip and insults back and forth between the dragon Níðhöggr, who sits at the bottom of the tree gnawing on its roots, and the hawk Veðrfölnir, who sits at the top of the tree keeping watch. According to Richard W. Thorington, Jr. and Katie E. Ferrell, this legend may have originated from the red squirrel's habit of giving a "scolding alarm call in response to danger", which some Norsemen may have imagined as insults.

In Irish mythology, the goddess Medb is said to always have a bird perched on one shoulder and a squirrel on the other, serving as her messengers to the sky and the earth respectively. In Europe during the Middle Ages, squirrels were sometimes used in bestiaries as symbols of greed and avarice on account of their storing of nuts, but, in the nineteenth century, British natural history books often praised them as thrifty for this same reason. A myth told by the Ainu people of Japan holds that squirrels are the discarded sandals of the ancestral deity Aioina, possibly because squirrels move in spurts like footsteps. The Kalevala, a Finnish epic poem collected in the nineteenth century but rooted in much older oral tradition, contains references to squirrels, including mention of a white squirrel being born of a virgin.

Literary references to squirrels include the works of Beatrix Potter, Brian Jacques' Redwall series (including Jess Squirrel and numerous other squirrels), Pattertwig in C. S. Lewis' Prince Caspian, Michael Tod's Woodstock Saga of novels featuring squirrel communities in the style of Watership Down, and the Starwife and her subjects from Robin Jarvis's Deptford novels. The title character in Miriam Young's 1964 children's book Miss Suzy is a squirrel.

Anthropomorphic red squirrels were used in UK road safety campaigns between the 1950s and 1980s.

An episode of the radio program This American Life called "Squirrel Cop" describes the unintentionally humorous misadventure of a newly-hired policeman in trying to remove a frantic squirrel from a homeowner's living room, which results in personal injury and a small fire. First aired in 1998, this episode turned out to be one of the most popular ones of the series, prompting rebroadcasts and a lead position on the two-CD compilation Crimebusters + Crossed Wires: Stories from This American Life.

Albino and white squirrels

One of the ways that squirrels affect human society is inspired by the fascination that people seem to have over local populations of white squirrels (often misidentified as being albino). This manifests itself by the creation of social group communities that form from a commonly shared interest in these rare animals. Other impacts on human society inspired by white squirrels include the creation of organizations that seek to protect them from human predation, and the use of the white squirrel image as a cultural icon.

Although these squirrels are commonly referred to as "albinos", most of them are likely non-albino squirrels that exhibit a rare white fur coloration known as leucism that is as a result of a recessive gene found within certain eastern gray squirrel (Sciurus carolinensis) populations, and so technically they ought to be referred to as white squirrels, instead of albino.

Olney, Illinois, known as the "White Squirrel Capital of the World", is home of the world's largest known white squirrel colony. These squirrels have the right of way on all streets in the town, with a $500 fine for hitting one. The Olney Police Department features the image of a white squirrel on its officers' uniform patches.

Along with Olney, there are four other towns in North America that avidly compete with each other to be the official "Home of the White Squirrel", namely: Marionville, Missouri; Brevard, North Carolina; Exeter, Ontario; and Kenton, Tennessee, each of which holds an annual white squirrel festival, among other things designed to promote their claim of "White Squirrel Capital".

A list of white squirrel sightings around the world is maintained by the White Squirrel Research Institute, a group based in Brevard, North Carolina.

Other towns that have reported white squirrel populations in North America (although not necessarily competing to be the "official" white squirrel capital) include Bowling Green, Kentucky; Columbia, Mississippi; Dayton, Ohio; DeForest, Wisconsin; Queenstown, Maryland; Stratford, Connecticut; and some of the snowbelt cities in the Western, Central and Finger Lakes regions of New York State (Buffalo, Rochester, Ithaca and Syracuse). White squirrels have also been spotted in Broad Ripple Village, Indianapolis. The Trinity Bellwoods neighborhood of Toronto, Ontario is locally known for white squirrel sightings.
Campus populations

In addition to the various towns that boast of their white squirrel populations, a number of university campuses in North America have white squirrels. The University of Texas at Austin is home to a white squirrel population which has spurred the myth of the albino squirrel as a good luck charm. There are many versions of the tale; one of the more popular versions is if one spots the albino squirrel before an exam, they will ace it. The University of North Texas founded the Albino Squirrel Preservation Society in 2001, which has since acquired several "worldwide" chapters. In 2006, the University of North Texas held a student referendum to name their white squirrel as the university's secondary mascot, but the vote was narrowly defeated by the student body. University of Wisconsin - Eau Claire has a significant white squirrel population both on the campus and in other areas of the city of Eau Claire. Michigan Technological University in Houghton, Michigan is home to frequently sighted white squirrels that live on and around the campus. A Facebook group dedicated to these squirrels, called I've Seen the Albino Squirrel of Michigan Tech, was created for people to post photographs and anecdotes of their encounters with the white squirrels, and includes some stories from Michigan Tech alumni that recall seeing white squirrels in Houghton dating back to the 1930s.

In Kentucky, the University of Louisville has established its own chapter of the Albino Squirrel Preservation Society, which maintains contact with its members and interested parties through a Facebook group by that name. The university has an open policy to give away a free t-shirt to anyone who takes a photograph of a white squirrel on campus grounds and brings it to the administration offices.

Other university campuses that have albino squirrel populations include Oberlin College in Ohio, Ohio State University in Columbus, Ohio, Western Kentucky University in Bowling Green, Kentucky (which has had a population of albino squirrels since the 1960s), and Youngstown State University in Youngstown, Ohio.

Dr. Michael Stokes, a biology professor at Western Kentucky University, commented that the probable cause for the abundance of white squirrels on university campuses was because they were originally introduced by someone: "We're not sure how they got here, but I'll tell you how it usually happens...When you see them, especially around a college campus or parks, somebody brought them in because they thought it would be neat to have white squirrels around."

Dr. Albert Meier, another biology professor at Western Kentucky University, added that: "... white squirrels rarely survive in the wild because they can't easily hide. But on a college campus, they are less likely to be consumed by other animals."
In folklore

A story in which a Nāga shapeshifts into a white or albino squirrel, is killed by a hunter, and is magically transformed into meat equal to 8,000 cartloads figures prominently in the folklore of rocket festival traditions and the origin of Nong Han Kumphawapi Lake in Northeast Thailand.
Red and gray squirrels in the UK
See also: Eastern grey squirrels in Europe
Red squirrel at a feeding tray in the Lake District, England.

A decline of the red squirrel and the rise of the eastern gray squirrel, an introduced species from North America, has been widely remarked upon in British popular culture. It is mostly regarded as the invading grays driving out the native red species. Evidence also shows that gray squirrels are vectors of the squirrel parapoxvirus for which no vaccine is currently available, and which is deadly to red squirrels but does not seem to affect the non-native host. Currently, the red squirrel's range has been reduced to the coniferous forests in Scotland, and in England's Formby, the Lake District, Brownsea Island, and the Isle of Wight. The majority of England's red squirrels are found in the county of Northumberland. Special measures are in place to contain and remove any infiltration of gray squirrels into these areas. Though the population has dramatically decreased, they remain listed on the IUCN Red List as Least Concern.

As the eastern gray squirrel is regarded as vermin it is illegal to release any into the wild; any caught have to be humanely killed.'''
}

response = requests.post('http://127.0.0.1:8000/summaries/', headers=headers, data=data)
print(response.json())
