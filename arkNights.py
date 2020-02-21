import random, time

agent6 = ['能天使', '推进之王', '伊芙利特', '艾雅法拉', '安洁莉娜', '闪灵', '夜莺', '星熊', '塞雷娅', '银灰', '斯卡蒂']
agent5 = ['白面鸮', '凛冬', '德克萨斯', '芙兰卡', '拉普兰德', '幽灵鲨', '蓝毒',
    '白金', '陨星', '天火', '梅尔', '赫默', '华法琳', '临光',
    '红', '雷蛇', '可颂', '普罗旺斯', '守林人', '崖心', '初雪',
    '真理', '空', '狮蝎', '食铁兽', '夜魔']
agent4 = ['夜烟', '远山', '杰西卡', '流星', '白雪', '清道夫', '红豆',
    '杜宾', '缠丸', '霜叶', '慕斯', '砾', '暗锁', '末药',
    '调香师', '角峰', '蛇屠箱', '古米', '深海色', '地灵', '阿消',
    '猎蜂']
agent3 = ['芬', '香草', '翎羽', '玫兰莎', '卡缇', '米格鲁', '克洛丝',
    '炎熔', '芙蓉', '安塞尔', '史都华德', '梓兰', '月见夜', '空爆']

agentDict = {
    3 : agent3,
    4 : agent4,
    5 : agent5,
    6 : agent6
}

class arkRandomizer:
    def __init__(self, times=1):
        self.times = times
        self.count = 0
        self.offset = 0
        self.randomAgent = []
        self.randomClass = []

    def getRandomizedResults(self, offsetSetting):
        random.seed(time.time_ns())
        randomClass = []
        self.count += 1
        offset = int(self.count / 5) + offsetSetting
        for i in range(0, self.times):
            randNum = random.randint(0, 100) + (offset * 2)
            if randNum > 98:
                randomClass.append(6)
                self.count = 0
            elif randNum > 90:
                randomClass.append(5)
            elif randNum > 40:
                randomClass.append(4)
            else:
                randomClass.append(3)

            time.sleep(0.05)

        self.randomClass = randomClass
        self.randomAgent = self.getAgents()

    def getAgents(self):
        randomAgent = []
        random.seed(time.time_ns())
        for elements in self.randomClass:
            agentList = agentDict[elements]
            agentIdx = random.randint(0, len(agentList) - 1)
            randomAgent.append(agentList[agentIdx])

        return randomAgent

    def __str__(self):
        response = ''
        response += '您抽到的东西有~蹡蹡！\n'
        sixStar = 0
        for idx, elements in enumerate(self.randomClass):
            if elements == 6:
                sixStar += 1
            response += str(elements) + '星干员： %s\n' % self.randomAgent[idx]


        if 5 not in self.randomClass and 6 not in self.randomClass:
            congrats = '哈↑哈↓紫气东来'

        else:
            if sixStar > 6:
                congrats = '你丫神仙吧草w'
            elif sixStar > 3:
                congrats = '这个爆率感觉机器人应该是坏了吧'
            elif sixStar >= 1:
                congrats = '有点幸运了啊'
            else:
                congrats = '没事这结果挺正常的，会好起来的，哈哈哈哈嗝~'

        response += '本次寻访获得了%d个六星干员，%s' % (sixStar, congrats)
        self.randomClass.clear()
        self.randomAgent.clear()
        return response
