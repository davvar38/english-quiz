import pandas as pd


def main():
    table = pd.read_csv('vocabulary_table_rename.csv')

    while table.shape[0] != 0:
        question_row = table.sample(n=1)
        table = table.drop(question_row.index)
        question, exact_response = question_row['french'].iloc[0], question_row['english'].iloc[0]

        print(question)
        response = input()

        if response == exact_response:
            print("Correct")
        else:
            print("Wrong")


if __name__ == '__main__':
    main()
