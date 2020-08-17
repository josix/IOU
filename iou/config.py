COMMAND_PATTERN = r"^(?P<prefix>/dc)(?P<command>\s+\w+)?"

SUBCOMMANDS = frozenset(
    {"join", "add", "status", "peep", "modify", "remove", "quit", "balance"}
)

USAGE = (
    "使用說明（Usage）：\n"
    "/dc join:   註冊自己帳號至這個 Bot\n"
    "/dc add:   記錄一筆債務(?)含借出一筆錢或欠一筆錢\n"
    "/dc peep:   快速查看你的上一筆紀錄\n"
    "/dc modify:   修改一筆紀錄\n"
    "/dc remove:   償還後刪除一筆紀錄\n"
    "/dc status:   查看自身目前借前或欠錢狀況\n"
    "/dc balance:   查看指定雙方的債務狀況\n"
    "/dc quit:   離開並不使用這個 Bot"
)

WRONG_USAGE_RESPONSE = f"==WRONG USAGE==\n\n{USAGE}"
