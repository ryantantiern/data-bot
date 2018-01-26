## GREET
* _greet_start
	-	utter_greet
> greet

## DENY REOFFER ASSISTANCE
> reoffer_asssistance
* _deny
	-	utter_bye

## AFFIRM REOFFER ASSISTANCE
> reoffer_assistance
> greet	

## HAPPY PATH
>	greet
* _source_data[tags=British, tags=economy]
	-	slot{"tags" : "British"}
	-	slot{"tags" : "economy"}
	- slot{"objective" : "source_data"}
	-	bot.actions.CheckUnderstanding
> check_source_data_understanding

## ABOVE AVERAGE PATH
> greet
* _source_data
	- slot{"objective" : "source_data"}
	-	bot.actions.CheckUnderstanding
* _affirm
	- utter_prompt_tags
* _provide_tags[tags=British, tags=economy]
	-	slot{"tags" : "British"}
	-	slot{"tags" : "economy"}
	-	bot.actions.CheckUnderstanding
> check_source_data_understanding

## PERFECT PATH
> greet
* _source_data[tags=British, tags=economy, limit=3]
	-	slot{"tags" : "British"}
	-	slot{"tags" : "economy"}
	-	slot{"limit" : 3}
	- slot{"objective" : "source_data"}
	-	bot.actions.CheckUnderstanding
> check_source_data_understanding

## GOOD PATH
> greet
* _source_data
	-	slot{"objective" : "source_data"}
	-	bot.actions.CheckUnderstanding
* _affirm
	-	utter_prompt_tags
* _provide_tags[tags=British, tags=economy, limit=5]
	-	slot{"tags" : "British"}
	-	slot{"tags" : "economy"}
	-	slot{"limit" : 5}
	-	bot.actions.CheckUnderstanding
> check_source_data_understanding


## CHECK SOURCE DATA UNDERSTANDING DENY
> check_source_data_understanding
* _deny
	-	utter_offer_assistance
> alter_source_data_understanding

## CHECK SOURCE DATA UNDERSTANDING AFFIRM
> check_source_data_understanding
* _affirm
		-	bot.actions.SourceData
		-	utter_reoffer_assistance
> reoffer_assistance


## ALTER SOURCE DATAUNDERSTANDING
> alter_source_data_understanding
* _alter_tags[tags=construction, tags=London]
	-	slot{"tags" : "construction"}
	-	slot{"tags" : "London"}
	-	bot.actions.CheckUnderstanding
> check_source_data_understanding
