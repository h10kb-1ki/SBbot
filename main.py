import requests
import os
import random

ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")  # GitHub Secrets から取得
USER_ID = os.getenv("U4c1ebc83ae32482ea9bf5c81759c7d0b")  # 送信先ユーザーID

def select_message():
    sb = [
        '本気の失敗には…価値がある', 
        '迷ったときはね どっちが正しいかなんて考えちゃダメ。『どっちが楽しいか』で決めなさい', 
        'It’s a piece of cake!', 
        '俺の敵は\nだいたい俺です', 
        'グーみたいな奴がいて、チョキみたいな奴もいて、パーみたいな奴もいる\n誰が一番強いか答えを知ってる奴はいるか？', 
        '人という字は支えあっているのではない\n「支える者がいてその上に立つ者がいる」', 
        '死ぬ覚悟なんていらねえぞ\n必要なのは”生きる覚悟”だ', 
        '危機感のない者には成長もない', 
        'ネクタイを締める理由なんて1コしかねえ\n仕事が無事に終わった後に”緩める”ためだ', 
        '「空」は誰のもんでもない\n「人生」は自分のもんだ\n人生はコントロールが利く', 
        '事故った時、整備士に責任を押し付けるのはパイロットの恥っちゅうもんだ\n”心のノート”にメモっとけ', 
        '避けようのないもんはそりゃある\nだがそれを言ってどうなる\nワシらは死ぬまで生きるだけだ', 
        'やれるとこまでやって何かを見つけろよ\nどーせやるなら\nその道の一流を目指そうぜ', 
        '自分で気付いて動き出さない者にかけてやるやさしい言葉などない', 
        '大事なのは”できる”という経験を得ること', 
        '逃げ道ってのは甘えの道だ\n誰でも楽に歩けるかわりどこにも辿り着けない', 
        '”諦め”ってある意味では”決意”に似てるよな', 
        '一生消えないなら受け入れるしかない\n内ポケットの不発弾も月まで連れていく', 
        '人の悪口というのは仲間内で言う人は”凡人”\n口に出さない人は”賢人”\n不特定多数に向けて発信する人は”暇人”ですから', 
        'キノコと名乗ったからにはカゴに入れ', 
        '死人や神様に答えを求める前に周りをよく見るこった\n生きてる兄貴と話せ', 
        '本当ははじめから”バカでかいドア”なんでものはない\n小さなドアがいっぱいあるだけだ', 
        'We are lonely, but not alone.', 
        '最下位でも何でもいいから絶対…ゴールまで歩いてやる\n1位と最下位との差なんて大したことねーんだよ\nゴールすることとしないことの差に比べりゃ', 
        '新しいモノ作ろうって話なんだ\n最初は何だって”仮説”だろ', 
        '先のこと考えるのやめたんだ。わかってたけど、大事なのは結局、今だ。今、この訓練が、どうやったら最高のもんになるかだけど考えることにした。やったことは、きっと俺らの力に変わるはず。だからケンジちょっとだけ、無理なことに挑戦してこうぜ。', 
        'モノ作りには失敗することにかける金と労力が必要なんだよ。いい素材使ってるモノがいいモノとは限らねえんだ\nだけど…失敗を知って乗り越えたモノなら、それはいいモノだ', 
        'もしこれが運だとしてもねー、それも俺の実力なわけだよ。', 
        '大事なのは……動くこと\n何もせずに止まっているのは道端の石コロです\n動いて動いて輝く石は流れ星……\n「生きた石コロ」です', 
        'バカげてると思うか？茶番だと\nだがこれをやるのが今のお前の現実だ、受け入れろ\n大事なのは“できる”という経験を得ること', 
        '”止まる”も”進む”もコントロールするのはお前だ', 
        ''
        ]
    i = random.randint(0, len(sb)-1)
    return sb[i]

def send_line_message():
    message = select_message()
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code, response.text)
    

if __name__ == "__main__":
    send_line_message()