# Intent Recognition, as part of the paper "Functional Flexibility in Generative AI Interfaces"

This implementation of a RASA backend works as an intent recognition. 

See the paper on arxiv: https://arxiv.org/abs/2410.10644

## Run the backend:

Execute `docker-compose -f docker-compose.prod.yml up -d` and the backend will be available. 

## How it works: 

Users can delegate 'summarize', 'translate', and 'extend' tasks within the Conversational UI prototype. 

Simplified said, the intent recognition works as follows:

1. The prototype calls this intent recognition if a users leaves an interactive comment on a document. (RASA's parser URL) 

2. The RASA model will then decide for on of the three intents and sends a response back to the Conversational UI prototype. 

3. The prototype will then call the model API according to received response. 


