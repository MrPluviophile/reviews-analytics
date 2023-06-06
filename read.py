data = []
count = 0
reviews_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
		reviews_len += len(line)
	avg_len = reviews_len / len(data)
print('Finish loading, total', len(data), 'data')
print('Average length of review is', avg_len)

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
