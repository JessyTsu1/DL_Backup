class process:
    #结构体
    def __init__(self, name, priority, reachtime, needtime, usedtime, state):
        self.name = name
        self.priority = priority #优先数
        self.reachtime = reachtime #到达时间
        self.needtime = needtime #需要的运行时
        self.usedtime = usedtime #用了的时间
        self.state = state #当前状态，就绪、运行或完成
