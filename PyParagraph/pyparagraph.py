def count( file ):

	print("Paragraph Analysis")
	print("-------------------")
	num_words = 0
	num_sentences = 0
	with open(file, 'r') as f:
	    for line in f:
	        words = line.split()
	        num_words += len(words)
	        sentences = line.split(".")
	        num_sentences += len(sentences)
    
	average = sum(map(len, words))/len(words)
	sent_len = sum(len(x.split()) for x in sentences) / len(sentences)
	print("Number of words: " + str(num_words))
	print("Number of sentences: " + str(num_sentences))
	print("Average Letter Count: " + str(average))
	print("Average Sentence Length: " + str(sent_len))
	print()


count('paragraph_1.txt')
count('paragraph_2.txt')