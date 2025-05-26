import random
from math import sqrt

class recommender:

    def __init__(self, data, k=1, metric='pearson', n=5):
        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}
        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson
        if type(data).__name__ == 'dict':
            self.data = data

    def pearson(self, rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        if n == 0:
            return 0
        denominator = (sqrt(sum_x2 - pow(sum_x, 2) / n)
                       * sqrt(sum_y2 - pow(sum_y, 2) / n))
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator

    def computeNearestNeighbor(self, username):
        distances = []
        for instance in self.data:
            if instance != username:
                distance = self.fn(self.data[username], self.data[instance])
                distances.append((instance, distance))
        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return distances

    def recommend(self, user):
        recommendations = {}
        nearest = self.computeNearestNeighbor(user)
        userRatings = self.data[user]
        totalDistance = 0.0
        for i in range(min(self.k, len(nearest))):
            totalDistance += nearest[i][1]
        if totalDistance == 0:
            totalDistance = 1e-10
        for i in range(min(self.k, len(nearest))):
            weight = nearest[i][1] / totalDistance
            name = nearest[i][0]
            neighborRatings = self.data[name]
            for book in neighborRatings:
                if book not in userRatings:
                    if book not in recommendations:
                        recommendations[book] = neighborRatings[book] * weight
                    else:
                        recommendations[book] += neighborRatings[book] * weight
        recommendations = list(recommendations.items())
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return recommendations[:self.n]


pizza = [
    "chiken pesto",
    "peperoni",
    "sir estake",
    "makhloot",
    "gosht",
    "chahar fasl",
    "morgh",
    "nacho",
    "alferedo",
    "kalbas"
]

users = {}
for i in range(1, 101):
    user = 'User' + str(i)
    ratings = {}
    rated_pizza = random.sample(books, 7)  
    for pizza in rated_pizza:
        ratings[pizza] = random.randint(1, 5)
    users[user] = ratings


recommender_system = recommender(users, k=5, metric='pearson', n=5)

recommendations = recommender_system.recommend('User1')

print("Top 5 pizza Recommendations for User1:")
for item, score in recommendations:
    print(f"{item}: {score:.2f}")
