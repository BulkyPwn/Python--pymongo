# -*- coding: UTF-8 -*-

def analysis(text):

    import time
    import jieba

    emotion_dic = {}
    filename = 'D:\BosonNLP_sentiment_score.txt'  # txt�ļ��͵�ǰ�ű���ͬһĿ¼�£����Բ���д����·��
    with open(filename, 'rb') as file:
        while True:
            try:
                senList = file.readline().decode('utf-8')
                # print(senList)
                senList = senList[:-1]
                senList = senList.split(' ')
                emotion_dic[senList[0]] = senList[1]
            except IndexError:
                break

    def get_emotion(score):
        emotion_archive = ['绝望，十分愤怒，对生活不在抱有希望', '难过，失望，抑郁', '有点小难过或者小愤怒', '轻微的难受或者不屑，想得太多啦，洗洗睡觉吧', '生活也就这样吧', '有点小开心或者小激动',
                       '蛮开心的，生活多美好', '喜笑颜开，每天的太阳都是新的，生活充满了希望']
        if score <= -3.9:
            return emotion_archive[0]
        elif -3.9 < score <= -2.5:
            return emotion_archive[1]
        elif -2.5 < score <= -1:
            return emotion_archive[2]
        elif -1 < score <= 0:
            return emotion_archive[3]
        elif 0 <score <= 1:
            return emotion_archive[4]
        elif 1 < score <= 2.5:
            return emotion_archive[5]
        elif 2.5 < score < 3.9:
            return emotion_archive[6]
        else:
            return emotion_archive[7]

    test = text

    seg_list = jieba.cut(test, cut_all=True)
    string = "/ ".join(seg_list)
    string_list = string.split('/')
    emotion_index = 0
    time.sleep(1)
    print("-5分为极端消极，5分为非常高兴")

    for _ in range(len(string_list)):
        if string_list[_] in emotion_dic:
            emotion_index += float(emotion_dic[string_list[_]])
    print(emotion_index)
    print(get_emotion(emotion_index))

def main():

    import pymongo

    conn = pymongo.MongoClient()
    db = conn.test
    handler = db.b
    result=handler.find_one(skip=1)

    #print(result)

    text = result["text"]

    print(text)

    analysis(text)

    import sys
    sys.path.append("D:\Python Projects/venv/")
    import sha256
    c = sha256.s(text)

    # import hashlib
    #
    # string = text
    # # ######## sha256 ########
    #
    # sha256 = hashlib.sha256()
    # sha256.update(string.encode('utf-8'))
    # c = sha256.hexdigest()
    # # print("sha256加密结果:",s256)

    handler = db.c
    handler.insert_one({"hash":c})



main()