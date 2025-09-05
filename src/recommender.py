class SimpleRecommender:
    def __init__(self):
        self.user_item_matrix = None

    def fit(self, interactions):
        self.user_item_matrix = interactions.pivot(index="user_id", columns="item_id", values="quantity").fillna(0)

    def recommend(self, user_id, top_k=5):
        if self.user_item_matrix is None:
            raise ValueError("Model not fitted yet.")
        user_row = self.user_item_matrix.loc[user_id]
        return user_row.sort_values(ascending=False).head(top_k).index.tolist()
