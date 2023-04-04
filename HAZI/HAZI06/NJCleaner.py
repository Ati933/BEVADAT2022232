import pandas as pd

class NJCleaner():
    def __init__(self, path):
        self.data = pd.read_csv(path)

    def order_by_scheduled_time(self) -> pd.core.frame.DataFrame:
        pass

    def drop_columns_and_nan(self) -> pd.core.frame.DataFrame:
        pass

    def convert_date_to_day(self) -> pd.core.frame.DataFrame:
        pass

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.core.frame.DataFrame:
        pass

    def convert_delay(self) -> pd.core.frame.DataFrame:
        pass

    def drop_unnecessary_columns(self) -> pd.core.frame.DataFrame:
        pass

    def save_first_60k(self, path: str):
        pass

    def prep_df(self, path = 'data/NJ.csv'):
        pass