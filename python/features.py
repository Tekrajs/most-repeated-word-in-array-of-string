class Features:

    def __init__(self, topFeaturesNumber, possibleFeatures, featuresRequests) -> None:
        self.top_features_number = topFeaturesNumber
        self.possible_features = possibleFeatures
        self.features_requests = featuresRequests

    # Function to calculate the most frequently requested feature.
    def get_top_features(self):

        # keywords count are counts of word appearing in each sentence and that exist in given possible features
        keywords_count = {}
        for features_request in self.features_requests:
            # making possible features unique in each feature requests
            unique_request_set = set(features_request.lower().split())
            for keyword in unique_request_set:
                if keyword in self.possible_features:
                    if keyword not in keywords_count:
                        keywords_count[keyword] = 1
                    else:
                        keywords_count[keyword] += 1

        # sort dictionary by its values in descending order (note -1 for reverse order)
        keywords_count = dict(
            sorted(
                keywords_count.items(),
                key=lambda x: -x[1]
            )
        )

        # take top n features
        top_n_features = list(
            keywords_count.keys()
        )[:self.top_features_number]

        # example including these features
        # loop throught top features, find each by iterating over the examples, if found add to a top_examples
        top_examples = []
        for feature in top_n_features:
            for feature_request in self.features_requests:
                if feature in feature_request.lower() and feature_request not in top_examples:
                    top_examples.append(feature_request)

        # print result
        print('Top features\n', top_n_features)
        print('Top feature requests\n', top_examples)


features = Features(

    topFeaturesNumber=3,
    possibleFeatures=[
        "storage", "battery",
        "hover", "alexa", "waterproof", "solar"
    ],
    featuresRequests=[
        "I wish my kindle had even more storage",
        "I wish the battery battery battery life on my kindle lasted 2 years.",
        "Waterproof and increased battery are my top two",
        "I wanted to take my kindle into the shower. Waterproof please waterproof",
        "I wanna make my kindle hover on my desk",
        "How about a solar kindle!"
    ]
)

features.get_top_features()
