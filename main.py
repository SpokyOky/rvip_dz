class LogicWatch:
  def __init__(self, name):
    self.name = name
    self.time = 0

  def tick(self):
    self.time += 1

  def send(self, clock):
    self.tick()
    clock.receive(self)

  def receive(self, clock):
    self.time = max(self.time, clock.time)
    print("[" + str(self.time) + "]" + "Clock " + self.name + " received message from clock " + clock.name)

clock1 = LogicWatch("message 1")
clock2 = LogicWatch("message 2")
clock3 = LogicWatch("message 3")
clock1.send(clock3)
clock2.send(clock2)
clock3.send(clock1)
clock1.send(clock3)
