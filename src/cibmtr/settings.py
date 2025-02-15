from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

data_path = Path(__file__).parents[2] / "data"

train_data_path = data_path / "train.csv"
test_data_path = data_path / "test.csv"
