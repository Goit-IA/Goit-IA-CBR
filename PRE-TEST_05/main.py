from data_loader import load_dataset
from conversation import start_conversation

def main():
    df = load_dataset('dataset.csv')
    start_conversation(df)

if __name__ == "__main__":
    main()
