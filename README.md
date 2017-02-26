# Facebook_Markov

Ever wanted to simulate your friends?
Well now you can!

For any given chat, this program creates a Markov Model on words used in the mesages. Simply give it a seed word and it'll print Markov generated poetry, inspired by your friends own sentances.

## Setup
First, head over to this [repo](https://github.com/ownaginatious/fbchat-archive-parser) and use it to create a **json** file of your messages titled chat_dat.txt.

Next, replace the *user_id* dictionary in the code to contain the id's and names of the friends in the chat you want to simulate from. (The ID's are the second number in the url in the user's about section of their profile.)

Lastly, run *markov_sim.py*. It will creates the corpus, keyed by first word with values of lists of next words. You will be prompted for a seed word. $end$ denotes the end of a message. Type $exit$ to quit the program.

