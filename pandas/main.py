import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count=len(data[data["Primary Fur Color"] =="Gray"])
black_count=len(data[data["Primary Fur Color"]=="Black"])
cinnamon_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(gray_count,black_count,cinnamon_count)

data_dict={
    "Fur Color":["Gray","Black","Cinnamon"],
    "Count":[gray_count,black_count,cinnamon_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("wonderwomen.csv")

