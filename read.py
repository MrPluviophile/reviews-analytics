data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Finish loading, total', len(data), 'data')
print(data[0])


sum_len = 0
for d in data:
	sum_len += len(d)
print('Average length of review is', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('Total', len(new), 'reviews less than 100 words')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('Total', len(good), 'reviews mentioned good')
print(good[0])

#word count
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
while True:
	word = input('Please input the word that you want to check: ')
	if word == 'q':
		break
	if word in wc:
		print(word, 'displayed', wc[word], 'times')
	else:
		print('Word not found')
print('Thank you')