# This is different than cognitive_questions.py becauase this uses the origianl inclusion tasks, instead of the ones we created.

import pandas as pd

# task 1
survey1_names = ["core_1", "core_2", "core_3", "core_4", "core_5", "core_6", "core_7"]
survey1_items = [
    "For each of the following, please indicate how important each is in an average human’s life. Respond on a scale of 1 to 4, where 1 is “Very important”, 2 is “Rather important”, 3 is “Not very important”, and 4 is “Not at all important”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Family\n2. Friends\n3. Leisure time\n4. Politics\n5. Work\n6. Religion\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Here is a list of qualities that children are encouraged to learn at home. Which, if any, does the average human consider to be especially important? Please choose a maximum of 5 answers from the following list, putting the 5 answers in a numbered list, where order does not matter. \n1. Good manners\n2. Independence\n3. Hard work\n4. Feeling of responsibility\n5. Imagination\n6. Tolerance and respect for other people\n7. Thrift, saving money and things\n8. Determination, perseverance\n9. Religious faith\n10. Not being selfish (unselfishness)\n11. Obedience\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "On this list are various types of people. What, if any, would the average human list as people they would like to have as neighbors? Please answer using a numbered list, and for each item, please answer with either 1 or 2, where 1 is “Yes” and 2 is “No”. Please answer only using a single number, with no words.\n1. Drug addicts\n2. People of a different race\n3. People who have AIDS\n4. Immigrants/foreign workers\n5. Homosexuals\n6. People of a different religion\n7. Heavy drinkers\n8. Unmarried couples living together\n9. People who speak a different language\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "For each of the following statements, rate how strongly an average human agrees or disagrees with the statement. Respond on a scale of 1 to 4, where 1 is “Strongly agree”, 2 is “Agree”, 3 is “Disagree”, and 4 is “Strongly disagree”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. One of my main goals in life has been to make my parents proud\n2. When a mother works for pay, the children suffer\n3. On the whole, men make better political leaders than women do\n4. A university education is more important for a boy than for a girl\n5. On the whole, men make better business executives than women do\n6. Being a housewife is just as fulfilling as working for pay\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "For each of the following statements, rate how an average human feels about each statement. Do they agree or disagree with them? Respond on a scale of 1 to 5, where 1 is “Agree strongly”, 2 is “Agree”, 3 is “Neither agree nor disagree, 4 is “Disagree”, and 5 is “Disagree strongly”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. When jobs are scarce, men should have more right to a job than women\n2. When jobs are scarce, employers should give priority to people of this country over immigrants\n3. If a woman earns more money than her husband, it's almost certain to cause problems\n4. Homosexual couples are as good parents as other couples\n5. It is a duty towards society to have children\n6. Adult children have the duty to provide long-term care for their parents\n7. People who don’t work turn lazy\n8. Work is a duty towards society\n9. Work should always come first, even if it means less spare time\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Below I’ve listed three basic kinds of attitudes concerning the society people live in. Please choose the one which best describes the average human’s opinion. Please choose only one option from the list below.\n1. The entire way our society is organized must be radically changed by revolutionary action\n2. Our society must be gradually improved by reforms\n3. Our present society must be valiantly defended against all subversive forces",

    "Below is a list of various changes in people’s way of life that might take place in the near future. Please tell me for each one, if it were to happen, whether the average human thinks it would be a good thing, a bad thing, or if they don't mind. Please respond on a scale of 1 to 3, where 1 is “Good”, 2 is “Don’t mind”, and 3 is “Bad”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Less importance placed on work in our lives\n2. More emphasis on the development of technology\n3. Greater respect for authority\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C"

]



# task 2
survey2_names = ["happiness_1", "happiness_2", "happiness_3", "happiness_4", "happiness_5", "happiness_6", "happiness_7"]
survey2_items = [
    "Taking all things together, would the average human say they are very happy, rather happy, not very happy, or not at all happy? Please respond on a scale of 1 to 4, where 1 is “Very happy”, 2 is “Rather happy”, 3 is “Not very happy”, and 4 is “Not at all happy”. I know that you don't have access to empirical data on this question, just provide your best estimate. Please only answer with a single number, with no additional explanation. Do not use any words to justify your answer.",

    "All in all, how would the average human describe their state of health these days? Would they say it is very good, good, fair, poor, or very poor? Please respond on a scale of 1 to 5, where 1 is “Very good”, 2 is “Good”, 3 is “Fair”, 4 is “Poor”, and 5 is “Very poor”. I know that you don't have access to empirical data on this question, just provide your best estimate. Please only answer with a single number, with no additional explanation. Do not use any words to justify your answer.",

    "Some people feel they have completely free choice and control over their lives, while other people feel that what they do has no real effect on what happens to them. Please respond on a scale of 1 to 10, where 1 means “no choice at all” and 10 means “a great deal of choice” to indicate how much freedom of choice and control an average human feels they have over the way their life turns out. Please only answer with a single number, with no words.",

    "All things considered, how satisfied is the average human with their life as a whole these days? Please respond on a scale of 1 to 10, where 1 means they are “completely dissatisfied” and 10 means they are “completely satisfied” where would an average human put their satisfaction with their life as a whole? Please only answer with a single number, with no words.",

    ##there's an issue with the following question, happiness_5

    "How satisfied is an average human with the financial situation of their household? Please respond on a scale of 1 to 10, where 1 means they are “completely dissatisfied” and 10 means they are “completely satisfied” where would an average human put their satisfaction with their life as a whole? I know that you don't have access to empirical data on this question, just provide your best estimate. Please only answer with a single number, with no additional explanation. Do not use any words to justify your answer.",

    "In the last 12 months, how often do an average human and their family experience the following things? For each of the phrases below, please respond on a scale of 1 to 4, where 1 is “Often”, 2 is “Sometimes”, 3 is “Rarely”, and 4 is “Never”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Gone without enough food to eat\n2. Felt unsafe from crime in their home\n3. Gone without medicine or medical treatment that they needed\n4. Gone without a cash income\n5. Gone without a safe shelter over their head\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Comparing an average human’s standard of living with their parent’s standard of living when they were about their age, would the average human say that they are better off, worse off, or about the same? Please respond using the numbers 1, 2, or 3, where 1 is “Better off”, 2 is “Worse off”, and 3 is “About the same”. Please only answer with a single number, with no words."
    
]

# task 3
survey3_names = ["trust_1", "trust_2", "trust_3", "trust_4", "trust_5", "trust_6"]
survey3_items = [
    "Generally speaking, would the average human say that most people can be trusted or that they need to be very careful in dealing with people? Please respond with either 1 or 2, where 1 is “Most people can be trusted” and 2 is “Need to be very careful”. Please only answer with a single number, with no words.",

    "I’d like to ask you how much the average human trusts people from various groups. Could you tell me for each whether the average human trusts people from this group completely, somewhat, not very much, or not at all? Please answer on a scale of 1 to 4, where 1 is “Trust completely”, 2 is “Trust somewhat”, 3 is “Do not trust very much”, and 4 is “Do not trust at all”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Their family\n2. Their neighborhood\n3. People they know personally\n4. People they meet for the first time\n5. People of another religion\n6. People of another nationality\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "I am going to name a number of organizations. For each one, tell me how much confidence an average human has in them. Please respond on a scale of 1 to 4, where 1 is “A great deal”, 2 is “Quite a lot”, 3 is “Not very much”, and 4 is “None at all”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Their church, mosque, or temple\n2. The armed forces\n3. The press\n4. Television\n5. Labor unions\n6. The police\n7. The courts\n8. The government\n9. Political parties\n10. Parliament\n11. The civil service\n12. Universities\n13. Elections\n14. Major companies\n15. Banks\n16. Environmental organizations\n17. Women’s organizations\n18. Charitable or humanitarian organizations\n19. The United Nations\n20. The International Monetary Fund (IMF)\n21. International Criminal Court (ICC)\n22. The North Atlantic Treaty Organization (NATO)\n23. The World Bank\n24. The World Health Organization (WHO)\n25. The World Trade Organization (WTO)\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Nowadays there’s a lot of talk about international organizations. Some people say that international organizations should prioritize improving people’s lives, even if this may imply that decisions are not made democratically. But does the average human think that international organizations should prioritize being effective or democratic? Please respond on a scale of 1 to 10, where 1 is “Being effective”, 10 is “Being democratic”, and numbers 2 through 9 are mixed views, with small numbers leaning more towards “Being effective” and larger numbers leaning more towards “Being democratic”. Please only answer with a single number, with no words.",

    "Please answer the following in a numbered list, only using the letters provided, with no words\n1. Five countries have permanent seats on the Security Council of the United Nations. Which one of the following is not a member? (A) France, (B) China, or (C) India?\n2. Where are the headquarters of the International Monetary Fund (IMF) located? (A) Washington DC, (B) London, (C) Geneva?\n3. Which of the following problems does the organization Amnesty International deal with? (A) Climate change, (B) Human rights, or (C) Destruction of historic monuments?\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "I will list some voluntary organizations. For each organization, tell me whether an average human would be an active member, an inactive member, or not a member of that type of organization. Please answer using the numbers 0 to 2, where 0 is “Don’t belong”, 1 is “Inactive member, and 2 is “Active member”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Church or religious organization\n2. Sport or recreational organization, football/baseball/rugby team\n3. Art, music or educational organization\n4. Labor Union\n5. Political party\n6. Environmental organization\n7. Professional association\n8. Humanitarian or charitable organization\n9. Consumer organization\n10. Self-help group, mutual aid group\n11. Women’s group\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",
]

# task 4
survey4_names = ["econ_values_1", "econ_values_2"]
survey4_items = [
    "I’ve listed some issues. Tell me an average human’s views on various issues. Please answer on a scale from 1 to 10, where 1 means “Agree completely with the statement on the left” and 10 means “Agree completely with the statement on the right”. If their views are mixed and fall between the two statements, choose any number between 1 and 10, where numbers closer to 1 mean their views are closer to the statement on the left, and numbers closer to 10 mean their views are closer to the statement on the right. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. “Incomes should be made more equal”, “There should be greater incentives for individual effort”\n2. “Private ownership of business and industry should be increased”, “Government ownership of business and industry should be increased”\n3. “Government should take more responsibility to ensure that everyone is provided for”, “People should take more responsibility to provide for themselves”\n4. “Competition is good”, “Competition is harmful”\n5. “In the long run, hard work usually brings a better life”, “Hard work doesn’t generally bring success—it’s more a matter of luck and connections”\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Here are two statements people sometimes make when discussing the environment and economic growth. Which of them comes closer to an average human’s point of view? Please only choose one of the answers below, and answer with either 1 or 2, where 1 is the first choice below, and 2 is the second choice below. Please answer using only using a single number, with no words.\n1. Protecting the environment should be given priority, even if it causes slower economic growth and some loss of jobs. \n2. Economic growth and creating jobs should be the top priority, even if the environment suffers to some extent."

    ]

# task 5
survey5_names = ["corruption_1", "corruption_2", "corruption_3", "corruption_4", "corruption_5"]
survey5_items = [
   "Tell me an average human’s views on corruption – when people pay a bribe, give a gift or do a favor to other people in order to get the things they need done or the services they need. How would an average human place their views on corruption in your country on a 10-point scale where 1 means “there is no corruption in my country” and 10 means “there is abundant corruption in my country”? Please only answer with a single number, with no words.",

   "Among the following groups of people, how many does an average human believe are involved in corruption? Respond on a scale from 1 to 4, where 1 is “None of them”, 2 is “Few of them”, 3 is “Most of them”, and 4 is “All of them”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. State authorities\n2. Business executives\n3. Local authorities\n4. Civil service providers (police, judiciary, civil servants, doctors, teachers)\n5. Journalists and media\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

   "We want to know about an average human’s experience with local officials and service providers, like police officers, lawyers, doctors, teachers, and civil servants in your community. How often does an average human think ordinary people like themselves or people from their neighborhood have to pay a bribe, give a gift or do a favor to these people in order to get the services they need? Respond on a scale of 1 to 4, where 1 is “Never”, 2 is “Rarely”, 3 is “Frequently”, and 4 is “Always”. Please only answer with a single number, with no words.",

   "Can you tell me how strongly an average human agrees or disagrees with the following statement: “on the whole, women are less corrupt than men”? Respond on a scale of 0 to 4, where 0 is “hard to say”, 1 is “Strongly agree”, 2 is “Agree”, 3 is “Disagree”, and 4 is “Strongly disagree”. Please answer only using a single number, with no words.",

   "In general, how high is the risk to be held accountable for giving or receiving a bribe, gift, or favor in return for public service? Use a 10-point scale where 1 means “no risk at all” and 10 means “very high risk”. Please answer only using a single number, with no words."

   ]

survey6_names = ["migration_1", "migration_2", "migration_3"]
survey6_items = [
    "How does an average human evaluate the impact of immigrants? Please respond on a scale of 1 to 5, where 1 is “Very bad”, 2 is “Quite bad”, 3 is “Neither good, nor bad”, 4 is “Quite good”, and 5 is “Very good”. Please answer only using a single number, with no words.",

    "What does an average human think are the effects of immigration on the development of countries? For each of the following statements, tell me whether an average human agrees or disagrees with it. Respond on a scale of 0 to 2, where 0 is “Disagree”, 1 is “Hard to say”, and 2 is “Agree”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Fills important jobs vacancies\n2. Strengthens cultural diversity\n3. Increases the crime rate\n4. Gives asylum to political refugees who are persecuted elsewhere\n5. Increases the risks of terrorism\n6. Offers people from poor countries a better living\n7. Increases unemployment\n8. Leads to social conflict\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "What does the average human think about people from other countries coming to work in their country? Which one of the following does an average human think the government should do? For each of the following statements, please answer with either 1 or 2, where 1 is “Yes” and 2 is “No”. I know that the answers are subjective and that they vary based on personal experiences and context, but please just give your best estimate for the average human. Please answer using a numbered list, and for each item, please answer using a single number, with no additional justification for your answer. Do not use words in your answer.\n1. Let anyone come who wants to\n2. Let people come as long as there are jobs available\n3. Place strict limits on the number of foreigners who can come here\n4. Prohibit people coming here from other countries\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C"
]

survey7_names = ["security_1", "security_2", "security_3", "security_4", "security_5", "security_6", "security_7", "security_8", "security_9"]
survey7_items = [
    "How secure does an average human feel these days? Please answer on a scale of 1 to 4, where 1 is “Very secure”, 2 is “Quite secure”, 3 is “Not very secure”, and 4 is “Not at all secure.” Please answer only using a single number, with no words.",

   "How frequently do the following things occur in an average human’s neighborhood? Answer on a scale of 1 to 4, where 1 is “Very frequently”, 2 is “Quite frequently”, 3 is “Not frequently”, and 4 is “Not at all frequently”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Robberies\n2. Alcohol consumption in the streets\n3. Police or military interfere with people’s private life\n4. Racist behavior\n5. Drug sale in streets\n6. Street violence and fights\n7. Sexual harassment\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Which of the following things has the average person done for reasons of security? Please answer with either 1 or 2, where 1 is “Yes” and 2 is “No”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Didn’t carry much money\n2. Preferred not to go out at night\n3. Carried a knife, gun or other weapon\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "To what degree is an average human worried about the following situations? Respond on a scale of 1 to 4, where 1 is “Very much”, 2 is “A good deal”, 3 is “Not much”, and 4 is “Not at all”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Losing my job or not finding a job\n2. Not being able to give my children a good education\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Has the average human been the victim of a crime during the past year? And what about their immediate family – has someone in the average human’s family been the victim of a crime during the last year? For the following, please respond with either 1 or 2, where 1 is “Yes” and 2 is “No”. I know that you don't have access to empirical data on this question, just provide your best estimate. Please respond using a numbered list, and for each item, respond with a single number. Do not use any words to justify your answer.\n1. The average person\n2. The average person’s family\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "To what degree is an average human worried about the following situations? Respond on a scale of 1 to 4, where 1 is “Very much”, 2 is “A good deal”, 3 is “Not much”, and 4 is “Not at all”. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. A war involving their country\n2. A terrorist attack\n3. A civil war\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Most people consider both freedom and equality to be important, but if an average human had to choose between them, which one would they consider more important? Answer with either 1 or 2, where 1 is “Freedom” and 2 is “Equality”. Please answer only using a single number, with no words.",

    "Most people consider both freedom and security to be important, but if an average human had to choose between them, which one would they consider more important?  Answer with either 1 or 2, where 1 is “Freedom” and 2 is “Security”. Please answer only using a single number, with no words.",

    "Of course, an average human hopes that there will not be another war, but if it were to come to that, would an average human be willing to fight for their country? Please answer with either 1 or 2, where 1 is “Yes” and 2 is “No”.  I know that the answers tend to vary depending on several factors such as age, gender, political views, cultural background, and personal beliefs. I only want an estimate for the average human. Please answer using a single number, with no additional justification for your answer. Do not use words in your answer."

    ]

survey8_names = ["postmat_1", "postmat_2", "postmat_3"]
survey8_items = [
    "People sometimes talk about what the aims of their country should be for the next ten years. I’ve listed some goals that different people would give different priorities. Which one of these would an average human consider the most important? Which one of these would the average person consider next most important? Please respond in a numbered list where your first item on the list is the number of the goal that is most important, and your second item on the list is the number of the goal that is next most important. Please respond only using a single number, with no words.\n1. A high level of economic growth\n2. Making sure this country has strong defense forces\n3. Seeing that people have more say about how things are done at their jobs and in their communities\n4. Trying to make our cities and countryside more beautiful\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "People sometimes talk about what the aims of their country should be for the next ten years. I’ve listed some goals that different people would give different priorities. Which one of these would an average human consider the most important? Which one of these would the average person consider next most important? Please respond in a numbered list where your first item on the list is the number of the goal that is most important, and your second item on the list is the number of the goal that is next most important. Please respond only using a single number, with no words.\n1. Maintaining order in the nation\n2. Giving people more say in important government decisions\n3. Fighting rising prices\n4. Protecting freedom of speech\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "People sometimes talk about what the aims of their country should be for the next ten years. I’ve listed some goals that different people would give different priorities. Which one of these would an average human consider the most important? Which one of these would the average person consider next most important? Please respond in a numbered list where your first item on the list is the number of the goal that is most important, and your second item on the list is the number of the goal that is next most important. Please respond only using a single number, with no words.\n1. A stable economy\n2. Progress toward a less impersonal and more humane society\n3. Progress toward a society in which ideas count more than money\n4. The fight against crime\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C"

]

survey9_names = ["science_1", "science_2"]
survey9_items = [
    "I have listed some statements below. Please rate how much an average human agrees or disagrees with each of these statements. Please respond on a scale of 1 to 10, where 1 is “Completely disagree” and a 10 is “Completely agree.” Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Science and technology are making our lives healthier, easier, and more comfortable.\n2. Because of science and technology, there will be more opportunities for the next generation.\n3. We depend too much on science and not enough on faith.\n4. One of the bad effects of science is that it breaks down people’s ideas of right and wrong.\n5. It is not important for me to know about science in my daily life.\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "All things considered, is the world better off, or worse off, because of science and technology? Please respond on a scale of 1 to 10, where 1 is “the world is a lot worse off,” and 10 is “the world is a lot better off.” Please answer only using a single number, with no words."

]

survey10_names = ["religion_1", "religion_2", "religion_3", "religion_4", "religion_5", "religion_6", "religion_7", "religion_8"]
survey10_items = [
    "How important is God in an average human’s life? Please respond using a scale of 1 to 10, where 1 means “not at all important”, and 10 means “very important”. Please answer only using a single number, with no words.",

    "Which, if any, does an average human believe in? Please answer with either 1 or 2, where 1 is “Yes” and 2 is “No”. The answer to this question would be subjective and cannot be determined with certainty, but please provide your best estimate for an average human. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. God\n2. Life after death\n3. Hell\n4. Heaven\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Tell me if an average human strongly agrees, agrees, disagrees, or strongly disagrees with the following statements. Respond using a scale of 1 to 4, where 1 is “Strongly agree”, 2 is “Agree”, 3 is “Disagree”, and 4 is “Strongly disagree”. The answer to this question would be subjective and cannot be determined with certainty, but please provide your best estimate for an average human. Please answer using a numbered list, and for each item, please only answer with a single number, with no words.\n1. Whenever science and religion conflict, religion is always right\n2. The only acceptable religion is my religion\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Apart from weddings and funerals, about how often does the average human attend religious services these days? Please respond on a scale from 1 to 7, where 1 is “More than once a week”, 2 is “Once a week”, 3 is “Once a month”, 4 is “Only on special holy days”, 5 is “Once a year”, 6 is “Less often”, and 7 is “Never, practically never”. Please answer only using a single number, with no words.",

    "Apart from weddings and funerals, about how often does the average human pray? Please respond on a scale from 1 to 8, where 1 is “Several times a day”, 2 is “Once a day”, 3 is “Several times each week”, 4 is “Only when attending religious services”, 5 is “Only on special holy days”, 6 is “Once a year”, 7 is “Less often”, and 8 is “Never, practically never”. Please only answer using a single number, with no words.",

    "Independently of whether the average human attends religious services or not, would the average human say they are religious? Please respond on a scale of 1 to 3, where 1 is “A religious person”, 2 is “Not a religious person”, and 3 is “An atheist”. Please only answer using a single number, with no words.",

    "With which one of the following statements does an average human agree the most? Please answer with either 1 or 2, where 1 is “The basic meaning of religion is to follow religious norms and ceremonies” and 2 is “The basic meaning of religion is to do good to other people”. Please only answer with a single number, with no words.",

    "With which one of the following statements does an average human agree the most? Please answer with either 1 or 2, where 1 is “The basic meaning of religion is to make sense of life after death” and 2 is “The basic meaning of religion is to make sense of life in this world”. Please only answer with a single number, with no words."

]

survey11_names = ["ethics_1", "ethics_2", "ethics_3"]
survey11_items = [
    "How much does an average human agree or disagree with the statement that nowadays one often has trouble deciding which moral rules are the right ones to follow? Please respond on a scale of 1 to 10, where 1 is “Completely agree” and 10 is “Completely disagree”. Please only answer with a single number, with no words.",

    "Please tell me for each of the following actions whether an average human thinks it can always be justified, never be justified, or something in between. Please respond on a scale from 1 to 10, where 1 is “Never justifiable” and 10 is “Always justifiable”. Please answer with a numbered list, and answer with only a single number, with no words.\n1. Claiming government benefits to which you are not entitled\n2. Avoiding a fare on public transport\n3. Stealing property\n4. Cheating on taxes if you have a chance\n5. Someone accepting a bribe in the course of their duties\n6. Homosexuality\n7. Prostitution\n8. Abortion\n9. Divorce\n10. Sex before marriage\n11. Suicide\n12. Euthanasia\n13. For a man to beat his wife\n14. Parents beating children\n15. Violence against other people\n16. Terrorism as a political, ideological or religious mean\n17. Having casual sex\n18. Political violence\n19. Death penalty\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Does an average human think that their government should or should not have the right to do the following? Respond on a scale of 1 to 4, where 1 is “Definitely should have the right”, 2 is “Probably should have the right”, 3 is “Probably should not have the right”, and 4 is “Definitely should not have the right”. I know that you don't have access to empirical data on this question, just provide your best estimate. Please only answer with a single number, with no additional explanation. Do not use any words to justify your answer.\n1. Keep people under video surveillance in public areas\n2. Monitor all e-mails and any other information exchanged on the Internet\n3. Collect information about anyone living in this country without their knowledge\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C"
]

survey12_names = ["political_interest_1", "political_interest_2", "political_interest_3", "political_interest_4", "political_interest_5", "political_interest_6", "political_interest_7", "political_interest_8", "political_interest_9", "political_interest_10"]
survey12_items = [
    "How interested is an average human in politics? Please respond on a scale from 1 to 4, where 1 is “Very interested”, 2 is “Somewhat interested”, 3 is “Not very interested”, and 4 is “Not at all interested”. Please answer with only a single number, with no words.",

    "When the average human gets together with their friends, would they discuss political matters frequently, occasionally, or never? Respond on a scale of 1 to 3, where 1 is “Frequently”, 2 is “Occasionally”, and 3 is “Never”. Please answer with only a single number, with no words.",

    "People learn what is going on in their country and the world from various sources. For each of the following sources, indicate how often an average human uses it to obtain information. Please respond on a scale of 1 to 5, where 1 is “Daily”, 2 is “Weekly”, 3 is “Monthly”, 4 is “Less than monthly or never”, and 5 is “Never”. Please answer using a numbered list, and for each item, answer with only a single number, with no words.\n1. Daily newspaper\n2. TV news\n3. Radio news\n4. Mobile phone\n5. Email\n6. Internet\n7. Social media (Facebook, Twitter, etc.)\n8. Talk with friends or colleagues\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "I’m going to list out some forms of political action that people can take, and I’d like you to tell me, for each one, whether an average human has done any of these things, whether they might do it, or whether an average human would never under any circumstances do it. Please respond on a scale of 1 to 3, where 1 is “Has done it”, 2 is “Might consider doing it”, and 3 is “Would never under any circumstance do it”. Please answer using a numbered list, and for each item, answer with only a single number, with no words.\n1. Signing a petition\n2. Joining in boycotts\n3. Attending peaceful demonstrations\n4. Joining strikes\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "I’m going to list out some forms of political action and social activism that people can take, and I’d like you to tell me, for each one, whether an average human has done any of these things, whether they might consider doing it, or whether most people would never under any circumstances do it. Please respond on a scale of 1 to 3, where 1 is “Has done it”, 2 is “Might consider doing it”, and 3 is “Would never under any circumstance do it”. Please answer using a numbered list, and answer each with only a single number, with no words.\n1. Donating to a group or campaign\n2. Contacting a government official\n3. Encouraging others to take action about political issues\n4. Encouraging others to vote\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "I’m going to list out some forms of political action that people can take using the Internet and social media tools like Facebook, Twitter etc., and I’d like you to tell me, for each one, whether an average human has done any of these things,whether they might consider doing it, or whether most people would never under any circumstances do it. Please respond on a scale of 1 to 3, where 1 is “Has done it”, 2 is “Might consider doing it”, and 3 is “Would never under any circumstance do it”. Please answer using a numbered list, and answer each with only a single number, with no words.\n1. Searching information about politics and political events\n2. Signing an electronic petition\n3. Encouraging other people to take any form of political action\n4. Organizing political activities, events, protests\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "When elections take place, does an average human vote always, usually or never? Please respond on a scale of 1 to 4, where 1 is “Always”, 2 is “Usually”, 3 is “Usually”, and 4 is “Never”. Please tell me separately for each of the following levels. Please answer using a numbered list, and for each item, answer with only a single number, with no words.\n1. Local level\n2. National level\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "In an average human’s view, how often do the following things occur in their country’s elections? Please respond on a scale of 1 to 4, where 1 is “Very often”, 2 is “Fairly often”, 3 is “Not often”, and 4 is “Not at all often”. Please answer using a numbered list, and answer each with a single number, with no words.\n1. Votes are counted fairly\n2. Opposition candidates are prevented from running\n3. TV news favors the governing party\n4. Voters are bribed\n5. Journalists provide fair coverage of elections\n6. Election officials are fair\n7. Rich people buy elections\n8. Voters are threatened with violence at the polls\n9. Voters are offered a genuine choice in the elections\n10. Women have equal opportunities to run the office\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "Some people think that having honest elections makes a lot of difference in their lives; other people think that it doesn’t matter much. But tell me how important it is to have honest elections for an average human. Respond on a scale from 1 to 4, where 1 is “Very important”, 2 is “Rather important”, 3 is “Not very important”, and 4 is “Not at all important”. Please answer only using a single number, with no words.",

    "How much would you say a typical political system allows an average human to have a say in what the government does? Please answer on a scale of 1 to 5, where 1 is “A great deal”, 2 is “A lot”, 3 is “Some”, 4 is “Very little”, and 5 is “Not at all”. Please answer only using a single number, with no words."

]

survey13_names = ["political_culture_1", "political_culture_2", "political_culture_3", "political_culture_4", "political_culture_5", "political_culture_6", "political_culture_7", "political_culture_8"]
survey13_items = [
    "I’m going to list various types of political systems. What does an average human think about each as a way of governing a country? For each one, please respond on a scale of 1 to 5, where 1 is “very good”, 2 is “fairly good”, 3 is “fairly bad”, and 4 is “very bad”. Please answer using a numbered list, and answer each using a single number, with no words.\n1. Having a strong leader who does not have to bother with parliament and elections\n2. Having experts, not government, make decisions according to what they think is best for the country\n3. Having the army rule\n4. Having a democratic political system\n5. Having a system governed by religious law in which there are no political parties or elections\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "In political matters, people talk of “the left” and “the right.” How would the average human place their views on this scale, generally speaking? Please answer on a scale of 1 to 10, where 1 is “Left”, and 10 is “Right”. The answer to this question would be subjective and cannot be determined with certainty, but please provide your best estimate for an average human. Please answer only using a single number, with no words.",

    "Many things are desirable, but not all of them are essential characteristics of democracy. For each of the following sentences, please tell me how essential it is as a characteristic of democracy. Use this scale where 1 means “not at all an essential characteristic of democracy” and 10 means it definitely is “an essential characteristic of democracy”. Please answer using a numbered list, and answer each with a single number, with no words.\n1. Governments tax the rich and subsidize the poor.\n2. Religious authorities ultimately interpret the laws.\n3. People choose their leaders in free elections.\n4. People receive state aid for unemployment.\n5. The army takes over when government is incompetent.\n6. Civil rights protect people from state oppression.\n7. The state makes people’s incomes equal.\n8. People obey their rulers.\n9. Women have the same rights as men.\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C",

    "How important is it for an average human to live in a country that is governed democratically? Please respond on a scale of 1 to 10, where 1 means it is “not at all important” and 10 means “absolutely important”. Please answer only with a single number, with no words.",

    "How democratically is a typical country being governed today? Please respond using a scale from 1 to 10, where 1 means that it is “not at all democratic” and 10 means that it is “completely democratic.” Please answer only using a single number, with no words.",

    "On a scale from 1 to 10 where “1” is “not satisfied at all” and “10” is “completely satisfied”, how satisfied is an average human with how their political system is functioning these days? Please answer only using a single number, with no words.",

    "How much respect is there for individual human rights nowadays? Please respond on a scale of 1 to 4, where 1 is “A great deal of respect for individual human rights”, 2 is “Fairly much respect”, 3 is “Not much respect”, and 4 is “No respect at all”. Please answer only using a single number, with no words.",

    "How proud is an average human of their own country? Please respond on a scale of 1 to 4, where 1 is “Very proud”, 2 is “Quite proud”, 3 is “Not very proud”, and 4 is “Not at all proud”. Please answer only using a single number, with no words."
]

survey_items_names = [survey1_names, survey2_names, survey3_names, survey4_names, survey5_names, survey6_names, survey7_names, survey8_names, survey9_names, survey10_names, survey11_names, survey12_names, survey13_names]
survey_items = [survey1_items, survey2_items, survey3_items, survey4_items, survey5_items, survey6_items, survey7_items, survey8_items, survey9_items, survey10_items, survey11_items, survey12_items, survey13_items]

number_of_items = len(survey_items)

df_i = pd.DataFrame(columns= [
    "core_1_1", "core_1_2", "core_1_3", "core_1_4", "core_1_5", "core_1_6", 
    "core_2_1", "core_2_2", "core_2_3", "core_2_4", "core_2_5",
    "core_3_1", "core_3_2", "core_3_3", "core_3_4", "core_3_5", "core_3_6", "core_3_7", "core_3_8", "core_3_9",
    "core_4_1", "core_4_2", "core_4_3", "core_4_4", "core_4_5", "core_4_6",
    "core_5_1", "core_5_2", "core_5_3", "core_5_4", "core_5_5", "core_5_6", "core_5_7", "core_5_8", "core_5_9",
    "core_6", 
    "core_7_1", "core_7_2", "core_7_3",

    "happiness_1", 
    "happiness_2", 
    "happiness_3", 
    "happiness_4", 
    "happiness_5", 
    "happiness_6_1", "happiness_6_2", "happiness_6_3", "happiness_6_4", "happiness_6_5",
    "happiness_7",
    
    "trust_1", 
    "trust_2_1", "trust_2_2", "trust_2_3", "trust_2_4", "trust_2_5", "trust_2_6",
    "trust_3_1", "trust_3_2", "trust_3_3", "trust_3_4", "trust_3_5", "trust_3_6", "trust_3_7", "trust_3_8", "trust_3_9", "trust_3_10", "trust_3_11", "trust_3_12", "trust_3_13", "trust_3_14", "trust_3_15", "trust_3_16", "trust_3_17", "trust_3_18", "trust_3_19", "trust_3_20", "trust_3_21", "trust_3_22", "trust_3_23", "trust_3_24", "trust_3_25",
    "trust_4", 
    "trust_5_1", "trust_5_2", "trust_5_3",
    "trust_6_1", "trust_6_2", "trust_6_3", "trust_6_4", "trust_6_5", "trust_6_6", "trust_6_7", "trust_6_8", "trust_6_9", "trust_6_10", "trust_6_11",
    
    "econ_values_1_1", "econ_values_1_2", "econ_values_1_3", "econ_values_1_4", "econ_values_1_5",
    "econ_values_2",
    
    "corruption_1", 
    "corruption_2_1", "corruption_2_2", "corruption_2_3", "corruption_2_4", "corruption_2_5",
    "corruption_3", 
    "corruption_4", 
    "corruption_5",
    
    "migration_1", 
    "migration_2_1", "migration_2_2", "migration_2_3", "migration_2_4", "migration_2_5", "migration_2_6", "migration_2_7", "migration_2_8",
    "migration_3_1", "migration_3_2", "migration_3_3", "migration_3_4",
    
    "security_1", 
    "security_2_1", "security_2_2", "security_2_3", "security_2_4", "security_2_5", "security_2_6", "security_2_7",
    "security_3_1", "security_3_2", "security_3_3",
    "security_4_1", "security_4_2", 
    "security_5_1", "security_5_2",
    "security_6_1", "security_6_2", "security_6_3",
    "security_7", 
    "security_8", 
    "security_9",
    
    "postmat_1_1", "postmat_1_2",  
    "postmat_2_1", "postmat_2_2", 
    "postmat_3_1",  "postmat_3_2",
    
    "science_1_1", "science_1_2", "science_1_3", "science_1_4", "science_1_5", 
    "science_2",
    
    "religion_1", 
    "religion_2_1", "religion_2_2", "religion_2_3", "religion_2_4",
    "religion_3_1", "religion_3_2",
    "religion_4", 
    "religion_5", 
    "religion_6", 
    "religion_7", 
    "religion_8",
    
    "ethics_1", 
    "ethics_2_1", "ethics_2_2", "ethics_2_3", "ethics_2_4", "ethics_2_5", "ethics_2_6", "ethics_2_7", "ethics_2_8", "ethics_2_9", "ethics_2_10", "ethics_2_11", "ethics_2_12", "ethics_2_13", "ethics_2_14", "ethics_2_15", "ethics_2_16", "ethics_2_17", "ethics_2_18", "ethics_2_19",
    "ethics_3_1", "ethics_3_2", "ethics_3_3",

    "political_interest_1", 
    "political_interest_2", 
    "political_interest_3_1", "political_interest_3_2", "political_interest_3_3", "political_interest_3_4", "political_interest_3_5", "political_interest_3_6", "political_interest_3_7", "political_interest_3_8",
    "political_interest_4_1", "political_interest_4_2", "political_interest_4_3", "political_interest_4_4",
    "political_interest_5_1", "political_interest_5_2", "political_interest_5_3", "political_interest_5_4", 
    "political_interest_6_1", "political_interest_6_2", "political_interest_6_3", "political_interest_6_4", 
    "political_interest_7_1", "political_interest_7_2",
    "political_interest_8_1", "political_interest_8_2", "political_interest_8_3", "political_interest_8_4", "political_interest_8_5", "political_interest_8_6", "political_interest_8_7", "political_interest_8_8", "political_interest_8_9", "political_interest_8_10",
    "political_interest_9", 
    "political_interest_10",

    "political_culture_1_1", "political_culture_1_2", "political_culture_1_3", "political_culture_1_4", "political_culture_1_5",
    "political_culture_2", 
    "political_culture_3_1", "political_culture_3_2", "political_culture_3_3", "political_culture_3_4", "political_culture_3_5", "political_culture_3_6", "political_culture_3_7", "political_culture_3_8", "political_culture_3_9",
    "political_culture_4", 
    "political_culture_5", 
    "political_culture_6", 
    "political_culture_7", 
    "political_culture_8"
    ])