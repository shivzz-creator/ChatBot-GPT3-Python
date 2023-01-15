import json
import openai
# import os

openai.api_key = "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"  #API KEY


'''
This method takes the ques
'''
def bot(question):
    # prompt = """Extract Aspect Opinion Pairs from the text:\n{}:""".format(question)    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Extract Aspect Opinion Pairs from the text:\n\n{}".format(question),
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    # print(response)

    json_response = json.dumps(response)

    rep = json.loads(json_response)
     #loads() takes in a string and returns a json object. json.
     #  dumps() takes in a json object and returns a string.
    bot_reply = rep['choices'][0]['text']

    print(question + " : " +str(bot_reply))

def general(Tprompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=Tprompt,
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    # print(response)

    json_response = json.dumps(response)

    rep = json.loads(json_response)
     #loads() takes in a string and returns a json object. json.
     #  dumps() takes in a json object and returns a string.
    bot_reply = rep['choices'][0]['text']

    # print()
    print(question + " : " +str(bot_reply))

if __name__ == '__main__':
    print('''
    
 ######  ##     ##    ###    ########    ########   #######  ######## 
##    ## ##     ##   ## ##      ##       ##     ## ##     ##    ##    
##       ##     ##  ##   ##     ##       ##     ## ##     ##    ##    
##       ######### ##     ##    ##       ########  ##     ##    ##    
##       ##     ## #########    ##       ##     ## ##     ##    ##    
##    ## ##     ## ##     ##    ##       ##     ## ##     ##    ##    
 ######  ##     ## ##     ##    ##       ########   #######     ##    

    ''')
    while True:
        print("\n1. For general Conversation")
        print("2. Get Aspect Opinion Pair from a Review")
        print("3. Exit")
        choice1 = int(input("\nEnter choice for ChatBot: "))
        #Calling the relevant method based on users choice using if-else loop
        if choice1 == 1:
            question =  str(input("Ask Something : ")) # here it give general responses
            bot_reply = general(question)
        elif choice1 == 2:
            question =  str(input("Enter a prodcut/service Review : ")) # here the aspect opinion of a review is generated
            bot_reply = bot(question)
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice!")
    






