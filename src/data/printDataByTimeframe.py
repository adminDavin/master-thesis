import sys, os
ROOT_PATH = os.path.abspath(".").split("src")[0]
module_path = os.path.abspath(os.path.join(ROOT_PATH+"/src/utils/"))
if module_path not in sys.path:
    sys.path.append(module_path)

import time
import utilities
import prints
from configs import getConfig

def main(filename, start, end):
    df = utilities.readDataFile(filename)
    df = utilities.getDataWithTimeIndex(df)
    df = df.dropna()
    df = utilities.getDataByTimeframe(df, start, end)

    subdir = filename.split('/')[-2]
    columns, relevantColumns, labelNames, columnUnits, timestamps = getConfig(subdir)

    if relevantColumns is not None:
        df = utilities.dropIrrelevantColumns(df, [relevantColumns, labelNames])

    prints.printDataframe(df)

pyName = "printDataByTimeframe.py"
arguments = [
    "- file name (string)",
    "- start (string)",
    "- end (string)",
]

# usage: python ml/printDataByTimeframe.py datasets/filename.csv relevantColumns(bool) start end
if __name__ == "__main__":
    start_time = time.time()
    prints.printEmptyLine()
    
    print("Running", pyName)
    print("Prints dataframe by provided timeframe")
    prints.printEmptyLine()
    
    try:
        filename = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]
    except IndexError:
        print(pyName, "was called with inappropriate arguments")
        print("Please provide the following arguments:")
        for argument in arguments:
            print(argument)
        sys.exit()
    
    main(filename, start, end)

    prints.printEmptyLine()
    print("Running of", pyName, "finished in", time.time() - start_time, "seconds")
    prints.printEmptyLine()