import time 
import tqdm
import threading

class TrainData(threading.Thread):
    def __init__(self,data):
        threading.Thread.__init__(self)
        self.data = data
    def run(self):
        self._return = train_data()
    def join(self):
        threading.Thread.join(self)
        return self._return

class LoadData(threading.Thread):
    def __init__(self, filenames):
        threading.Thread.__init__(self)
        self.filenames = filenames
    def run(self):        
        # return data
        self._return = load_data()
    def join(self):
        threading.Thread.join(self)
        return self._return

def load_data():
    time.sleep(2)

def train_data():
    time.sleep(3)


epochs  = 5

'''if __name__=="__main__":
    epochs  = 5 
    with tqdm.tqdm(range(epochs)) as epochLoop:
        for i in epochLoop:
            # loadData
            load_data()
            #print("Loading_Data_F")
    
            # trainModel
            train_data()
            #print("Training_Data_F")
'''

with tqdm.tqdm(range(epochs)) as epochLoop:
  for _ in epochLoop:
    # loadData
    loadThread = LoadData(None)
    loadThread.start()
    
    # trainModel
    trainThread = TrainData(None)
    trainThread.start()
    
    # only continue if both threads are done
    modelLoss = trainThread.join()
    data = loadThread.join()
