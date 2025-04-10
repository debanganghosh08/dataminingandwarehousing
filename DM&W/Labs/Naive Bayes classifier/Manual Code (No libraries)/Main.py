# Training dataset
data = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rainy', 'Mild', 'Yes'],
    ['Rainy', 'Cool', 'Yes'],
    ['Rainy', 'Cool', 'No'],
    ['Overcast', 'Cool', 'Yes'],
    ['Sunny', 'Mild', 'No'],
    ['Sunny', 'Cool', 'Yes']
]

# Count function
def count_freq(attribute_index, value, target, data):
    count = 0
    target_count = 0
    for row in data:
        if row[2] == target:
            target_count += 1
            if row[attribute_index] == value:
                count += 1
    return count, target_count

# Predict for: ['Sunny', 'Cool']
def predict(test):
    classes = ['Yes', 'No']
    probs = {}

    for cls in classes:
        prob = 1
        for i in range(len(test)):
            attr_count, total = count_freq(i, test[i], cls, data)
            prob *= (attr_count / total) if total != 0 else 0
        class_count = sum(1 for row in data if row[2] == cls)
        prob *= class_count / len(data)
        probs[cls] = prob

    return max(probs, key=probs.get)

# Run prediction
test_sample = ['Sunny', 'Cool']
print("Prediction for", test_sample, "=>", predict(test_sample))
test_sample = ['Overcast', 'Mild']
print("Prediction for", test_sample, "=>", predict(test_sample))
test_sample = ['Rainy', 'Hot']
print("Prediction for", test_sample, "=>", predict(test_sample))
test_sample = ['Sunny', 'Mild']
print("Prediction for", test_sample, "=>", predict(test_sample))
test_sample = ['Rainy', 'Cool']
print("Prediction for", test_sample, "=>", predict(test_sample))
