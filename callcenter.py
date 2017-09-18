class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print self.id
        print self.name
        print self.number
        print self.time
        print self.reason


class Callcenter(object):
    def __init__(self, call_list, queue_size):
        self.call_list = call_list
        self.queue_size = queue_size
    def add(self, new):
        self.add = call_list.append(new)
    def remove(self):
        self.remove = call_list.remove(call_list[0])
    def info(self):
        print self.call_list
        print self.queue_size

mycall = Call("2", "Stacey", "8888888", "3:30", "who cares" )
othercall = Call("3", "Katie","3333333", "5:00", "saying hi")

call_list = [mycall.name, othercall.name]

callcenter1 = Callcenter(call_list, (len(call_list)) )
callcenter1.info()
