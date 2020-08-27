## ask_info
* greet
  - greeting
* ask_score 
  - get_score_tuition
* my_name    
  - utter_ask_name
* num_card
  - utter_ask_card
  - submit


## ask
* ask_score 
  - get_score_tuition
* my_name    
  - utter_ask_name
* num_card
  - utter_ask_card
  - submit
  
## greeting
* greet
  - greeting

## happy path
* greet
  - greeting
* mood_great
  - utter_happy

## sad path 1
* greet
  - greeting
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - greeting
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
