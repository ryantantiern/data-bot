from pprint import pprint
from json import dump
import argparse
def start_end(text, word):
	ltext = len(text)
	lword = len(word)
	i = 0
	while i < ltext:
		j = 0
		
		while  j < lword and i < ltext and text[i] == word[j]:
			i += 1
			j += 1

		if j == lword:
			return (i-j, i)

		i += 1

	return (0,0)


def convert(filename, output):
	rasa = {
		'rasa_nlu_data' : {
			'common_examples' : [],
			'regex_features' : [],
			'entity_synonyms' : []
		}
	}
	data = []
	with open(filename, 'r') as f:
		ndata = int(f.readline().rstrip())
		for _ in range(ndata):
			entry = {}
			line = f.readline().rstrip().split(sep='-')
			entry['text'] = line[0]
			entry['intent'] = line[1]
			entry['entities'] = []
			for _ in range(int(line[2])):
				line = f.readline().rstrip().split(sep='-')
				tup = start_end(entry['text'].lower(), line[1].lower())
				entity = {
					'start' : tup[0],
					'end': tup[1],
					'entity' : line[0],
					'value' : line[1]
				}
				entry['entities'].append(entity)
			data.append(entry)
	rasa['rasa_nlu_data']['common_examples'] = data
	with open(output, 'w') as f:
		dump(rasa, f)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", help="Data file to parse from")
	parser.add_argument("-o", "--output", help="Output file to write to. hint: this will be your data.json")
	args = parser.parse_args()
	filename = args.input if args.input is not None else "raw_data"
	output = args.output if args.output is not None else "data/data-1.json"
	convert(filename, output)
