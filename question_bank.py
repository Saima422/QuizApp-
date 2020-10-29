# contains all the questions and their correct answers in form of lists

from Question import Question

def Ques_bank():
    question_prompts = [
        "\nWorld Wildlife Day is celebrated at?\n (a) 25th January\n (b) 2nd February\n (c) 27th February\n (d) 3rd March\n\n", #d
        "\nThe main source of water pollution is?\n (a) Sewage Water\n (b) Rain Water\n (c) Atmospheric Pollutants\n (d) Well-Water\n\n", #a
        "\nWhich crop is sown on the largest area in India?\n (a) Rice\n (b) Wheat\n (c) Sugarcane\n (d) Maize\n\n", #a
        "\nWhat is the second largest country (in size) in the world?\n (a) Canada\n (b) USA\n (c) China\n (d) Russia\n\n", #a
        "\nWhich language is spoken in Karnataka?\n (a) Marathi\n (b) Hindi\n (c) Malayalam\n (d) Kannada\n\n", #d
        "\nThe currency notes are printed in?\n (a) New Delhi\n (b) Nasik\n (c) Nagpur\n (d) Bombay\n\n", #b
        "\nWhat is the world's most common religion?\n (a) Hinduism\n (b) Christianity\n (c) Buddhism\n (d) Muslim\n\n", #b
        "\nThe country that has the highest in Barley Production?\n (a) China\n (b) India\n (c) Russia\n (d) France\n\n", #c
        "\nTsunamis are not caused by?\n (a) Hurricanes\n (b) Earthquakes\n (c) Undersea landslides\n (d) Volcanic eruptions\n\n", #a
        "\nThe hottest planet in the solar system?\n (a) Mercury\n (b) Venus\n (c) Mars\n (d) Jupiter\n\n", #b
        "\nWhich is the country which has the Great Barrier Reef?\n (a) London\n (b) Australia\n (c) Ireland\n (d) New Zealand\n\n", #b
        "\nAnthophobia is fear of which of the following?\n (a) Boss\n (b) Fire\n (c) Flowers\n (d) Dogs\n\n", #c
        "\nIn binary code, the number 7 is written by?\n (a) 110\n (b) 111\n (c) 101\n (d) 100\n\n", #b
        "\nClove is obtained from?\n (a) Root\n (b) Stem\n (c) Fruit\n (d) Flower bud\n\n", #d
        "\nSamba dance is famous in?\n (a) Brazil\n (b) Peru\n (c) Argentina\n (d) Mexico\n\n", #a
        "\nWhich is the famous International dance?\n (a) Romantic Dance\n (b) Bibhu\n (c) Odissi\n (d) Chau\n\n", #d
        "\nFathometer is used to measure?\n (a) Rainfall\n (b) Ocean depth\n (c) Sound intensity\n (d) Earthquakes\n\n", #b
        "\nWhich is the national vegetable of India?\n (a) lady’s-finger\n (b) Brinjal\n (c) Meetha Kaddu\n (d) None of these\n\n", #c
        "\nWhich is the national food of India?\n (a) Khichdi\n (b) Roti\n (c) Dal\n (d) None of these\n\n", #a
        "\nStrawberry is good source of which vitamin?\n (a) Vitamin C\n (b) Vitamin A\n (c) Vitamin K\n (d) None of these\n\n", #a
    ]

    questions_bank = [
        Question(question_prompts[0], "d"),
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "a"),
        Question(question_prompts[3], "a"),
        Question(question_prompts[4], "d"),
        Question(question_prompts[5], "b"),
        Question(question_prompts[6], "b"),
        Question(question_prompts[7], "c"),
        Question(question_prompts[8], "a"),
        Question(question_prompts[9], "b"),
        Question(question_prompts[10], "b"),
        Question(question_prompts[11], "c"),
        Question(question_prompts[12], "b"),
        Question(question_prompts[13], "d"),
        Question(question_prompts[14], "a"),
        Question(question_prompts[15], "d"),
        Question(question_prompts[16], "b"),
        Question(question_prompts[17], "c"),
        Question(question_prompts[18], "a"),
        Question(question_prompts[19], "a"),     
    ]

    return questions_bank