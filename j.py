# 自販機のクラスを作成
class VendingMachine:
    def __init__(self):
        # 商品とその値段を定義
        self.items = {
            "aaa": 150,
            "bbb": 160,
            "ccc": 100,
            "ddd": 130
        }

    # 商品を表示する関数
    def show_items(self):
        print("商品一覧:")
        for item, price in self.items.items(): # self.itemsは辞書。items()は辞書内のすべてのキーと値のペア取得。itemにキー、priceに値を代入。
            print(f"{item}: {price}円")

    # おつりを計算する関数
    def calculate_change(self, money, price): # selfを入れることでself.itemsにアクセス。moneyは投入金額。priceは商品価格。
        change = money - price  # おつりを計算
        coins = [500, 100, 50, 10]  # 使用する硬貨の種類
        coin_count = {}  # 硬貨の枚数を保存する辞書

        if change < 0:
            print("お金が足りません。")
            return None

        print(f"おつり: {change}円")

        # 高額な硬貨から順におつりを計算
        for coin in coins: # coinsに含まれる要素を順番にcoinに代入
            if change >= coin: #　おつりが硬貨より大きいか
                count = change // coin  # 何枚必要か計算(商)
                change = change % coin  # 残りのおつり(余り)
                coin_count[coin] = count  # 硬貨(coin)と枚数(count)を辞書(coin_count)に保存

        return coin_count

# メインの処理
def main():
    # 自販機を作成
    vending_machine = VendingMachine()

    # 商品を表示
    vending_machine.show_items()

    # ユーザーからお金と商品を入力してもらう
    money_inserted = int(input("お金を入れてください（円）: "))
    item_name = input("購入する商品を入力してください: ")

    # 商品の価格を取得
    if item_name in vending_machine.items: # item_name(キー)が辞書(vending_machine.items)にあるか確認
        item_price = vending_machine.items[item_name] # 存在するなら対応する商品の価格(値)を代入
    else:
        print("その商品はありません。")
        return

    # おつりを計算
    change = vending_machine.calculate_change(money_inserted, item_price) # def calculate_change(self, money, price)のmoneyとpriceに値を送って計算

    # おつりを表示
    if change:
        print("おつりを硬貨でお返しします:")
        for coin, count in change.items():
            print(f"{coin}円硬貨: {count}枚")

# プログラムを実行
if __name__ == "__main__":
    main()