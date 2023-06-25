import os
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class RecipeRecommender:
    def __init__(self):
        cwd = os.getcwd()
        ref_path = "src/files/recipes.csv"
        file_path = os.path.join(cwd, ref_path)
        self.recipes = pd.read_csv(file_path).dropna()
        self.recipe_features = self.__get_recipe_features()

    def __get_recipe_features(self):
        self.recipes.columns[self.recipes.isna().any()].tolist()
        self.recipes[self.recipes.isna().any(axis=1)]

        ingredients = set()

        for row in self.recipes["ingredients"]:
            for ingredient in row.split(", "):
                ingredients.add(ingredient)

        ingredients = sorted(list(ingredients))

        # One-Hot Encoding for features
        recipes_features = pd.DataFrame(
            0, index=self.recipes.index, columns=ingredients
        )
        for i, row in self.recipes.iterrows():
            for ingredient in row["ingredients"].split(", "):
                recipes_features.loc[i, ingredient] = 1

        cuisine_dummies = pd.get_dummies(self.recipes["cuisine"], prefix="cuisine")
        category_dummies = pd.get_dummies(self.recipes["category"], prefix="category")
        level_dummies = pd.get_dummies(self.recipes["level"], prefix="level")
        recipes_features = pd.concat(
            [recipes_features, cuisine_dummies, category_dummies, level_dummies], axis=1
        )

        return recipes_features

    def __get_recommendations(self, user_recipe_ids, user_feature_vector, top_k=10):
        # Calculate cosine similarity between user profile and all recipes
        similarities = cosine_similarity(
            user_feature_vector.values.reshape(1, -1), self.recipe_features
        )

        # Get indices of top 10 similar recipes
        similar_recipes = similarities.argsort()[0][::-1][:top_k + len(user_recipe_ids)]

        # Remove user's own recipes from recommendations
        recommendations = set(similar_recipes) - set(user_recipe_ids)
        list_tuple_recipe = []

        for recipe in recommendations:
            list_tuple_recipe.append(tuple([recipe, similarities[0][recipe]]))

        recommendations_recipe_sorted = [
            item[0] for item in sorted(list_tuple_recipe, key=lambda x: x[1])[::-1]
        ]

        # Get recommended recipes
        recommended_recipes = self.recipes.iloc[np.array(recommendations_recipe_sorted)]
        return recommended_recipes

    def __get_user_feature_vector(self, user_recipes):
        user_recipe_ids = []

        for recipe in user_recipes:
            match = self.recipes.index[self.recipes["name"] == recipe]

            if match.empty:
                continue
            user_recipe_ids.append(match[0])

        return [user_recipe_ids, self.recipe_features.iloc[user_recipe_ids].mean(axis=0)]

    def get_recommendations(self, user_recipes):
        [user_recipe_ids, user_feature_vector] = self.__get_user_feature_vector(user_recipes)
        recommended_recipes = self.__get_recommendations(
            user_recipe_ids, user_feature_vector
        )
        return list(recommended_recipes.name)
