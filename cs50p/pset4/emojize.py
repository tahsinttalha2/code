import emoji

prompt = input("Input: ")

if len(emoji.emoji_list(prompt)) > 0:
    print(f"output: {emoji.demojize(prompt)}")
else:
    print(f"output: {emoji.emojize(prompt, language="alias")}")