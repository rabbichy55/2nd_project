

# checking pandas version
import pandas as pd

print(pd.__version__)


# pandas series
import pandas as pd

a = [1, 4, 23, 45, "BMW"]

se = pd.Series(a)

print(se)

print(se[4]) # access

# own labels
import pandas as pd
a1 = ["Bangladesh", "India", "Nepal", "Pakistan"]

bb = pd.Series(a1, index=["x", "y", "z", "q"])
print(bb)

print(bb["y"])  # access by label


# key/value objects as series
import pandas as pd

a2 = {"D1": 100, "D2": 200, "D3": 300}

bb1 = pd.Series(a2)
print(bb1)
  

# create a DataFrame from two series
import pandas as pd

data = {
    'Home': ["Raj", "Taj"],
    'Floor': [2, 12]
}

my_house = pd.DataFrame(data)

print(my_house)
