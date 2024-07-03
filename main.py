meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешное",
            "ROFL":"its a joke"
            }
while True:
    command=int(input("Выберите свою комманду: 1 - значение слова, 2 - добавление нового слова"))
    if command==1:
        word = input("Введите непонятное слово (большими буквами!): ")
        if word in meme_dict.keys():
            print(word,meme_dict[word])
            # Что делать, если слово нашлось?
        else:
            # Что делать, если слово не нашлось?
            print("слово не нашлось")
    elif command==2:
        key1=input()
        value1=input()
        meme_dict[key1]=value1
