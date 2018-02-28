## Greet
* greet
    - action_greet
    - action_offer_help
> greet 

## Reoffer help, affirm 1
> reoffer_help{"tags" : "construction"}
*	affirm 
	-	action_offer_help
>	greet

## Reoffer help, affirm 2
> reoffer_help{"tags" : "congestion"}
*	affirm 
	-	action_offer_help
>	greet

## Reoffer help, affirm 3
> reoffer_help{"tags" : "urban planning"}
*	affirm 
	-	action_offer_help
>	greet
## Reoffer help, affirm 4
> reoffer_help{"tags" : "tunnels"}
*	affirm 
	-	action_offer_help
>	greet
## Reoffer help, affirm 5
> reoffer_help{"tags" : "roads"}
*	affirm 
	-	action_offer_help
>	greet

## Reoffer help, request help 1
> reoffer_help{"tags" : "google"}
*	requestHelp
    -   action_help
>	greet

## Reoffer help, request help 2
> reoffer_help{"tags" : "microsoft"}
*   requestHelp
    -   action_help
>	greet

## Reoffer help, request help 3
> reoffer_help{"tags" : "facebook"}
*   requestHelp
    -   action_help
>	greet

## Reoffer help, request help 4
> reoffer_help{"tags" : "amazon"}
*   requestHelp
    -   action_help
>	greet

## Reoffer help, request help 5
> reoffer_help{"tags" : "roads"}
*   requestHelp
    -   action_help
>	greet


## Reoffer help, source_data 1
> reoffer_help{"tags" : "construction"}
* sourceData{"tags": "london"}
    - slot{"tags": "london"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## Reoffer help, source_data 2
> reoffer_help{"tags" : "congestion"}
* sourceData{"tags": "google", "tags":"microsoft"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## Reoffer help, source_data 3
> reoffer_help{"tags" : "urban planning"}
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## Reoffer help, source_data 4
> reoffer_help{"tags" : "tunnels"}
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility", "tags":"transpotation"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    -	slot{"tags" : "transportation"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## Reoffer help, source_data 5
> reoffer_help{"tags" : "roads"}
* sourceData{"tags": "google", "tags":"microsoft", "limit" : 5}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
		-	slot{"limit" : 5}
    - action_source_data
    - action_reoffer_help
    > reoffer_help

## Reoffer help, source_data 6
> reoffer_help{"tags" : "google"}
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags": "urban planning", "tags" : "London", "tags": "tunnels", "limit" : 5}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	slot{"tags" : "London"}
		-	slot{"tags" : "tunnels"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## Reoffer help, source_data 7
> reoffer_help{"tags" : "microsoft"}
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "google", "tags" : "microsoft", "limit" : 5}
		-	slot{"tags" : "google"}
		-	slot{"tags" : "microsoft"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help


## Reoffer help, source_data 8
> reoffer_help{"tags" : "facebook"}
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "google", "tags":"microsoft"}
		-	slot{"tags" : "google"}
		-	slot{"tags" : "microsoft"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## Reoffer help, source_data 9
> reoffer_help{"tags" : "amazon"}
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags" : "construction"}
		-	slot{"tags" : "construction"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## Reoffer help, source_data 10
> reoffer_help{"tags" : "roads"}
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## Reoffer help, deny 1
> reoffer_help{"tags" : "roads"}
* deny
   	- action_goodbye

## Reoffer help, deny 2
> reoffer_help{"tags" : "amazon"}
* deny
  - action_goodbye

## Reoffer help, deny 3
> reoffer_help{"tags" : "roads",  "limit" : 4}
* deny
	- action_goodbye

## Reoffer help, deny 4
> reoffer_help{"tags" : "amazon" , "limit" : 5}
* deny 
	- action_goodbye

## Reoffer help, deny 5 
> reoffer_help{"tags" : "urban planning", "limit" : 5}
* deny
	- action_goodbye

## Reoffer help, deny 6 
> reoffer_help{"tags" : "construction", "limit" : 5}
* deny
	- action_goodbye

## Reoffer help, deny 7 
> reoffer_help{"tags" : "urban planning", "limit" : 5}
* deny
  - action_goodbye

## Reoffer help, deny 8 
> reoffer_help{"tags" : "construction", "limit" : 5}
* deny
  - action_goodbye


## Reoffer help, source_data
> reoffer_help
> greet
    	
## Generated Story 661491554775496997
> greet
* requestHelp
    - action_help
    - action_offer_help
* sourceData{"tags": "urban planning"}
    - slot{"tags": "urban planning"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## Generated Story -6847416699288690970
> greet
* sourceData{"tags": "construction"}
    - slot{"tags": "construction"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## Generated Story 2859018201048144995
> greet
* requestHelp
    - action_help
    - action_offer_help
* sourceData{"tags": "construction"}
    - slot{"tags": "construction"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help



## Generated Story 2150511379936170861
> greet
* sourceData{"tags": "london"}
    - slot{"tags": "london"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 1
> greet
* sourceData{"tags": "london"}
    - slot{"tags": "london"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 2
> greet
* sourceData{"tags": "london", "tags":"tube"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 3
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 4
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 5
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility", "tags":"transpotation"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    -	slot{"tags" : "transportation"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 6
> greet
* sourceData{"tags": "google"}
    - slot{"tags": "google"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 7
> greet
* sourceData{"tags": "google", "tags":"microsoft"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 8
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - slot{"tags": "apple"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 9
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "tags":"amazon"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - slot{"tags": "apple"}
    - slot{"tags": "amazon"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 10
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "tags":"amazon", "tags":"netflix"}
		- slot{"tags": "google"}
		- slot{"tags": "microsoft"}
		- slot{"tags": "apple"}
		- slot{"tags": "amazon"}
    -	slot{"tags" : "netflix"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 11
> greet
* sourceData{"tags": "urban planning"}
    - slot{"tags": "urban planning"}
    - action_source_data
		-	action_reoffer_help
   > reoffer_help

## story 12
> greet
* sourceData{"tags": "construction"}
    - slot{"tags": "construction"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 13
> greet
* sourceData{"tags": "construction"}
    - slot{"tags": "construction"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 14
> greet
* requestHelp
	- action_help
	- action_offer_help
* sourceData{"tags": "london"}
    - slot{"tags": "london"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 15
> greet
* sourceData{"tags": "london"}
    - slot{"tags": "london"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 16
> greet
* sourceData{"tags": "london", "tags":"tube"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help
	

## story 17
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 18
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 19
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility", "tags":"transpotation"}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    -	slot{"tags" : "transportation"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 20
> greet
* sourceData{"tags": "google"}
    - slot{"tags": "google"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 21
> greet
* sourceData{"tags": "google", "tags":"microsoft"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 22
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - slot{"tags": "apple"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 23
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "tags":"amazon"}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - slot{"tags": "apple"}
    - slot{"tags": "amazon"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 24
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "tags":"amazon", "tags":"netflix"}
		- slot{"tags": "google"}
		- slot{"tags": "microsoft"}
		- slot{"tags": "apple"}
		- slot{"tags": "amazon"}
    -	slot{"tags" : "netflix"}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 25
> greet
* sourceData{"tags": "urban planning", "limit" : 5}
    - slot{"tags": "urban planning"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 26
> greet
* sourceData{"tags": "construction", "limit" : 5}
    - slot{"tags": "construction"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 27
> greet
* sourceData{"tags": "construction", "limit" : 5}
    - slot{"tags": "construction"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help



## story 28
> greet
* sourceData{"tags": "london", "limit" : 5}
    - slot{"tags": "london"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 29
> greet
* sourceData{"tags": "london", "limit" : 5}
    - slot{"tags": "london"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 30
> greet
* sourceData{"tags": "london", "tags":"tube", "limit" : 5}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 31
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "limit" : 5}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 32
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility", "limit" : 5}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 33
> greet
* sourceData{"tags": "london", "tags":"tube", "tags":"congestion", "tags":"mobility", "tags":"transpotation", "limit" : 5}
    - slot{"tags": "london"}
    - slot{"tags": "tube"}
    - slot{"tags": "congestion"}
    - slot{"tags": "mobility"}
    -	slot{"tags" : "transportation"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 34
> greet
* sourceData{"tags": "google", "limit" : 5}
    - slot{"tags": "google"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help

## story 35
> greet
* sourceData{"tags": "google", "tags":"microsoft", "limit" : 5}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
		-	slot{"limit" : 5}
    - action_source_data
    - action_reoffer_help
		-	action_reoffer_help
    > reoffer_help


## story 36
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "limit" : 5}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - slot{"tags": "apple"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 37
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "tags":"amazon", "limit" : 5}
    - slot{"tags": "google"}
    - slot{"tags": "microsoft"}
    - slot{"tags": "apple"}
    - slot{"tags": "amazon"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 38
> greet
* sourceData{"tags": "google", "tags":"microsoft", "tags":"apple", "tags":"amazon", "tags":"netflix", "limit" : 5}
		- slot{"tags": "google"}
		- slot{"tags": "microsoft"}
		- slot{"tags": "apple"}
		- slot{"tags": "amazon"}
    -	slot{"tags" : "netflix"}
		-	slot{"limit" : 5}
    - action_source_data
		-	action_reoffer_help
    > reoffer_help


## story 39
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction"}
		-	slot{"tags" : "construction"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 40
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags" : "congestion"}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 41
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags" : "urban planning"}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 42
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags": "urban planning", "tags" : "London"}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	slot{"tags" : "London"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 43
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags": "urban planning", "tags" : "London", "tags": "tunnels"}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	slot{"tags" : "London"}
		-	slot{"tags" : "tunnels"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 44
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "limit" : 5}
		-	slot{"tags" : "construction"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 45
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags" : "congestion", "limit" : 5}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 46
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags" : "urban planning", "limit" : 5}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 47
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags": "urban planning", "tags" : "London", "limit" : 5}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	slot{"tags" : "London"}
		-	slot{"limit": 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help


## story 48
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "construction", "tags":"congestion","tags": "urban planning", "tags" : "London", "tags": "tunnels", "limit" : 5}
		-	slot{"tags" : "construction"}
		-	slot{"tags" : "congestion"}
		-	slot{"tags" : "urban planning"}
		-	slot{"tags" : "London"}
		-	slot{"tags" : "tunnels"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help


## story 49
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "google"}
		-	slot{"tags" : "google"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 50
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "google", "tags":"microsoft"}
		-	slot{"tags" : "google"}
		-	slot{"tags" : "microsoft"}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

## story 51
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "google", "limit" : 5}
		-	slot{"tags" : "google"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help


## story 52
> greet
* sourceData
    - action_source_data_prompt_tags
		-	action_reset_slots
* sourceDataProvideTags{"tags" : "google", "tags" : "microsoft", "limit" : 5}
		-	slot{"tags" : "google"}
		-	slot{"tags" : "microsoft"}
		-	slot{"limit" : 5}
		-	action_source_data
		-	action_reoffer_help
		> reoffer_help

