# DataBot
Conversational AI system for interacting with data using natural language (English).

# Training data format

Rasa NLU requires data to be in a a well structured format defined at [Rasa](http://rasa-nlu.readthedocs.io/en/latest/dataformat.html#training-data-format). However, it can be very tedious to type when creating the data. Included is **converter.py** that converts an easier-to-type data format into rasa training format. It that takes 2 optional arguments:  
* -i input file 
* -o output file  

If `input` or `output` files aren't specified, the default files are `'raw_data'` and `'data/data-1.json'` respectively. The format is as follows:  
1. Each line must end with a newline character i.e. <Enter>
2. The first line in the file denotes the number of intent
3. The next section describes each intent block:  
	* **T**-**I**-**E** represents *text*, *intent* and *no. of entities* seperated by a hypen. 
	 e.g. `I want chinese food-search_restaurant-1` 
	* The next **E** lines are represented as *entity*-*value* to capture (entity, value) pairs.
	 e.g. `food-chinese`
