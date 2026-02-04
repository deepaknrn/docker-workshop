import sys
import pandas as pd

print ("Arguments passed to the script:" + str(sys.argv))
month = int(sys.argv[1])
print ("Month argument value: " + str(month))

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4], "month": month})
print(df.head())

df.to_parquet(f"output_data_{month}.parquet")