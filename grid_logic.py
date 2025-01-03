from datetime import datetime, timezone
import numpy as np

WEEK_START = 6 # 6 = sunday
DRAW_START = datetime(2024,12,29,tzinfo=timezone.utc)
PIXEL_MAX = 100 

assert WEEK_START == DRAW_START.weekday()

def get_location():
    today = datetime.now(timezone.utc)
    location = (DRAW_START - today).days
    return location

def normalize(img: np.ndarray):
    img = img+img.min()
    img = (img/img.max()*PIXEL_MAX).astype(int)
    assert img.min() == 0
    assert img.max() == PIXEL_MAX
    return img

def img_2_arr(img: np.ndarray):
    return img.T.flatten()

def arr_2_img(arr: np.ndarray):
    return arr.reshape((-1,7)).T

def imshow(img: np.ndarray):
    print(img.T)

if __name__ == "__main__":
    a = np.arange(0,371)
    i = arr_2_img(a)
    print(normalize(i))