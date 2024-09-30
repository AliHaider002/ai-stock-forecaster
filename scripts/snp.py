import sys
import pandas as pd

def main():
    sp500 = pd.read_html(sys.argv[1])[0]["Symbol"]
    list = [ticker for ticker in sp500]
    # Print the list so the Node.js script can capture the output
    print(list)

if __name__ == "__main__":
    main()
