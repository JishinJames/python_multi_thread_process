import time 
import tqdm
import threading

def load_data():
    time.sleep(2)

def train_data():
    time.sleep(3)


epochs  = 5

if __name__=="__main__":
    epochs  = 5 
    with tqdm.tqdm(range(epochs)) as epochLoop:
        for i in epochLoop:
            # loadData
            load_data()
            #print("Loading_Data_F")
    
            # trainModel
            train_data()
            #print("Training_Data_F")