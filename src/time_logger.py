from datetime import datetime
import pandas as pd

class TimeLogger:

    def __init__(self, log_file):
        self._log_file = log_file
        self._df = pd.read_csv(self._log_file, skip_blank_lines=True)

    def get_categories(self):
        return self._df['category'].unique()

    def start_session(self, category):
        self._df = self._df.append({'category': category, 'start': datetime.now().replace(microsecond=0)}, ignore_index = True)
        self.save()

    def stop_session(self):
        self._df.at[self._df.last_valid_index(), 'end'] = datetime.now().replace(microsecond=0)
        self.save()

    def save(self):
        self._df.to_csv(self._log_file, index = False)