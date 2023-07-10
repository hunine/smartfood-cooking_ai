import os
import pandas as pd


class Recipe:
    def __init__(self, conn):
        self.db_conn = conn

    def __get_dataframe_recipes(self):
        query = f"SELECT recipes.id, recipes.name as name, ingredients.name as ingredients, levels.name as level, cuisine.name as cuisine, categories.name as category FROM recipes LEFT JOIN quantification ON recipes.id = quantification.recipe_id LEFT JOIN ingredients ON quantification.ingredient_id = ingredients.id LEFT JOIN levels ON recipes.level_id = levels.id LEFT JOIN cuisine ON recipes.cuisine_id = cuisine.id LEFT JOIN categories ON recipes.category_id = categories.id"

        df = pd.read_sql_query(query, self.db_conn)
        df_clean = df.dropna()
        df_grouped = (
            df_clean.groupby("id")
            .agg(
                {
                    "name": "first",
                    "ingredients": ", ".join,
                    "level": "first",
                    "cuisine": "first",
                    "category": "first",
                }
            )
            .reset_index()
        )

        return df_grouped

    def save_recipes_csv(self):
        try:
            df_grouped = self.__get_dataframe_recipes()

            cwd = os.getcwd()
            ref_path = "src/files/"
            file_path = os.path.join(cwd, ref_path)
            df_grouped.to_csv(file_path + "recipes.csv", index=False)
            os.remove(file_path + "recipe_features.csv")
            return True
        except:
            return False
