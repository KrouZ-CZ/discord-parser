import requests
import json
headers = {
    "authorization": "YOUR TOKEN HERE"
}
all_messages = []
def main():
    lists = 0
    chid = int('CHAT ID')
    try:
        url = f"https://discord.com/api/v9/channels/{chid}/messages"
        while True:
            r = requests.get(url=url, headers=headers)
            text = json.loads(r.text)
            if len(text) == 0:
                print("All messages has parsed"); break
            for item in text:
                if item['content'] != "":
                    all_messages.insert(0, {item['author']['username']: item['content']})
                id = item['id']
            print(f"Lists {lists + 1} has parsed")
            lists += 1
            url = f"https://discord.com/api/v9/channels/{chid}/messages?before={id}&limit=100"
    except:
        print('Operation except')
    with open('ServerForBrother.json', "w", encoding='utf-8') as file:
        json.dump(all_messages, file, indent=4, ensure_ascii=False)
    print('All data saved!')
if __name__ == "__main__":
    main()
