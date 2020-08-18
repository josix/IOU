COMMAND_PATTERN = r"^(?P<prefix>@meow)(?P<command>\s+\w+)?"

SUBCOMMANDS = frozenset(
    {"join", "add", "status", "peep", "modify", "remove", "quit", "balance"}
)

USAGE = (
    "【使用說明】：\n"
    '輸入 "@meow+動作 (例如 @meow join)"\n\n'
    "☑️ 註冊帳號請輸入：\n@meow join\n"
    "☑️ 記錄債務借款或還款請輸入：\n@meow add\n"
    "☑️ 快速查看你的上一筆紀錄請輸入：\n@meow peep\n"
    "☑️ 修改一筆紀錄請輸入：\n@meow modify\n"
    "☑️ 償還後刪除一筆紀錄請輸入：\n@meow remove\n"
    "☑️ 查看自身目前借前或欠錢狀況請輸入：\n@meow status:\n"
    "☑️ 查看指定雙方的債務狀況請輸入：\n@meow balance\n"
    "☑️ 離開並不使用這個 Bot請輸入：\n@meow quit"
)

WRONG_USAGE_RESPONSE = f"========輸入錯誤喔🙀========\n\n{USAGE}"
WELCOME_MESSAGE = (
    "哈囉喵😽！\n我是債貓機器人\n專門處理大家覺得麻煩的欠錢還錢問題💰" f"如果想知道如何呼喚我，請大家看一下使用說明😼\n\n{USAGE}"
)
