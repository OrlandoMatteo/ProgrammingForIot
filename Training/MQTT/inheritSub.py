from simpleSubscriber import MySubscriber
import time

class InhSub(MySubscriber):
    def __init__(self, clientID,topic,broker):
        MySubscriber.__init__(self,clientID,topic,broker)

if __name__ == "__main__":
	test = InhSub("MySubscriber 1","orlando/iot/#",'mqtt.eclipse.org')
	test.start()

	a = 0
	while (a < 30):
		a += 1
		time.sleep(1)

	test.stop()

