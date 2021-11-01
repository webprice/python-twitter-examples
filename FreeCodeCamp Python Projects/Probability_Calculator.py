import copy
import random
class Hat:

    def __init__(self,**color):
        keys=[]
        values=[]
        items = color.items()
        self.contents=[]
        for item in items:
            keys.append(item[0]), values.append(item[1])
        k = 0
        for each in values:
            i=0
            #print(each)
            while i<each:
                self.contents.append(keys[k])
                i+=1
            k+=1
        self.contents_original=self.contents[:]
    def __str__(self):
        return str(self.contents_original)

    def draw(self,numberofballs):
        self.nballs=numberofballs
        self.drawballs=copy.copy(self.contents_original)
        self.contents=copy.copy(self.contents_original)
        self.ballsthatdrawn=[]
        i=0
        if numberofballs >= len(self.contents_original):
            return  self.drawballs
        while i<self.nballs:
            numba=random.randint(0,(len(self.contents)-1))
            self.ballsthatdrawn.append(self.contents[numba])
            self.contents.pop(numba)
            i+=1
        return  self.ballsthatdrawn
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    items = expected_balls.items()
    keys = []
    values = []
    expected_balls_result = []
    for item in items:
        keys.append(item[0]), values.append(item[1])
        k = 0
    for each in values:
        i = 0
        while i < each:
            expected_balls_result.append(keys[k])
            i += 1
        k += 1
    #print("expected_balls_result",expected_balls_result)

    run=num_experiments
    same_balls=0
    exceptcounter=0
    while run>0:
        drawn_list=hat.draw(num_balls_drawn)
        #print(drawn_list)
        #if all(a in expected_balls_result for a in drawn_list):
        #N = [i for i in range(len(expected_balls_result)) if expected_balls_result[i] in drawn_list]
        #print(N)
            #same_balls += 1
        for every in expected_balls_result:
            try:
                drawn_list.remove(every)
            except:
                exceptcounter+=1
                continue
        if exceptcounter==0:
            same_balls+=1
        run-=1

    #print(same_balls)
    probability=same_balls/num_experiments
    return probability
