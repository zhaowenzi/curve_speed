from queue import Queue
from threading import Thread
import cv2
import argparse


def mock_function(x1, y1, x2, y2, x):
    if y2 == y1:
        return y1
    return (y2 - y1) / (x2 - x1) * x + (y1 - (x1 * (y2 - y1) / (x2 - x1)))


def shanchu(cur_time, sum_time):
    x1 = 0.0
    y1 = 0.0
    x2 = 15.0
    y2 = 0.0
    x3 = 20.0
    y3 = 4.2
    x4 = 38.0
    y4 = 4.2

    time_in_image = cur_time / sum_time * 38
    ret = 0
    if x1 <= time_in_image <= x2:
        ret = mock_function(x1, y1, x2, y2, time_in_image)
    elif x2 < time_in_image <= x3:
        ret = mock_function(x2, y2, x3, y3, time_in_image)
    elif x3 < time_in_image <= x4:
        ret = mock_function(x3, y3, x4, y4, time_in_image)

    if ret < 0:
        ret = 0.1 * ret + 1
    else:
        ret = ret + 1
    return ret


def mengtaiqi(cur_time, sum_time):
    x1 = 0.0
    y1 = -1.0
    x2 = 1.0
    y2 = -1.0
    x3 = 22.0
    y3 = 7.0
    x4 = 25.0
    y4 = -4.0
    x5 = 32.0
    y5 = 0.0
    x6 = 38.0
    y6 = 0.0
    time_in_image = cur_time / sum_time * 38.0
    ret = 0.0
    if x1 <= time_in_image <= x2:
        ret = mock_function(x1, y1, x2, y2, time_in_image)
    elif x2 < time_in_image <= x3:
        ret = mock_function(x2, y2, x3, y3, time_in_image)
    elif x3 < time_in_image <= x4:
        ret = mock_function(x3, y3, x4, y4, time_in_image)
    elif x4 < time_in_image <= x5:
        ret = mock_function(x4, y4, x5, y5, time_in_image)
    elif x5 < time_in_image <= x6:
        ret = mock_function(x5, y5, x6, y6, time_in_image)
    if ret < 0:
        ret = 0.1 * ret + 1
    else:
        ret = ret + 1
    return ret


def yingxiongshike(cur_time, sum_time):
    x1 = 0.0
    y1 = 0.0
    x2 = 1.0
    y2 = 0.0
    x3 = 14.0
    y3 = 6.0
    x4 = 18.0
    y4 = -5.0
    x5 = 20.0
    y5 = -5.0
    x6 = 24.0
    y6 = 6.0
    x7 = 37.0
    y7 = 0.0
    x8 = 38.0
    y8 = 0.0
    time_in_image = cur_time / sum_time * 38.0
    ret = 0.0
    if x1 <= time_in_image <= x2:
        ret = mock_function(x1, y1, x2, y2, time_in_image)
    elif x2 < time_in_image <= x3:
        ret = mock_function(x2, y2, x3, y3, time_in_image)
    elif x3 < time_in_image <= x4:
        ret = mock_function(x3, y3, x4, y4, time_in_image)
    elif x4 < time_in_image <= x5:
        ret = mock_function(x4, y4, x5, y5, time_in_image)
    elif x5 < time_in_image <= x6:
        ret = mock_function(x5, y5, x6, y6, time_in_image)
    elif x6 < time_in_image <= x7:
        ret = mock_function(x6, y6, x7, y7, time_in_image)
    elif x7 < time_in_image <= x8:
        ret = mock_function(x7, y7, x8, y8, time_in_image)
    if ret < 0:
        ret = 0.1 * ret + 1
    else:
        ret = ret + 1
    return ret


def shanjin(cur_time, sum_time):
    x1 = 0.0
    y1 = 4.2
    x2 = 16.0
    y2 = 4.2
    x3 = 23.0
    y3 = 0.0
    x4 = 38.0
    y4 = 0.0

    time_in_image = cur_time / sum_time * 38
    ret = 0
    if x1 <= time_in_image <= x2:
        ret = mock_function(x1, y1, x2, y2, time_in_image)
    elif x2 < time_in_image <= x3:
        ret = mock_function(x2, y2, x3, y3, time_in_image)
    elif x3 < time_in_image <= x4:
        ret = mock_function(x3, y3, x4, y4, time_in_image)

    if ret < 0:
        ret = 0.1 * ret + 1
    else:
        ret = ret + 1
    return ret


def tiaojie(cur_time, sum_time):
    x1 = 0.0
    y1 = -4.0
    x2 = 15.0
    y2 = -4.0
    x3 = 19.0
    y3 = 6.0
    x4 = 23.0
    y4 = -4.0
    x5 = 38.0
    y5 = -4.0

    time_in_image = cur_time / sum_time * 38
    ret = 0
    if x1 <= time_in_image <= x2:
        ret = mock_function(x1, y1, x2, y2, time_in_image)
    elif x2 < time_in_image <= x3:
        ret = mock_function(x2, y2, x3, y3, time_in_image)
    elif x3 < time_in_image <= x4:
        ret = mock_function(x3, y3, x4, y4, time_in_image)
    elif x4 < time_in_image <= x5:
        ret = mock_function(x4, y4, x5, y5, time_in_image)

    if ret < 0:
        ret = 0.1 * ret + 1
    else:
        ret = ret + 1
    return ret


def zidanshijian(cur_time, sum_time):
    x1 = 0.0
    y1 = 4.2
    x2 = 16.0
    y2 = 4.2
    x3 = 18.0
    y3 = -5.0
    x4 = 20
    y4 = -5.0
    x5 = 22.0
    y5 = 4.2
    x6 = 38.0
    y6 = 4.2

    time_in_image = cur_time / sum_time * 38
    ret = 0
    if x1 <= time_in_image <= x2:
        ret = mock_function(x1, y1, x2, y2, time_in_image)
    elif x2 < time_in_image <= x3:
        ret = mock_function(x2, y2, x3, y3, time_in_image)
    elif x3 < time_in_image <= x4:
        ret = mock_function(x3, y3, x4, y4, time_in_image)
    elif x4 < time_in_image <= x5:
        ret = mock_function(x4, y4, x5, y5, time_in_image)
    elif x5 < time_in_image <= x6:
        ret = mock_function(x5, y5, x6, y6, time_in_image)

    if ret < 0:
        ret = 0.1 * ret + 1
    else:
        ret = ret + 1
    return ret


# 用来表示终止的特殊对象
_sentinel = object()


def mock_curve(inpput_file, func):
    videoCapture = cv2.VideoCapture(input_file)
    sum_frame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)

    def producer(out_q):
        speed = 1
        leiji = 0.0
        for x in range(int(sum_frame)):
            if x % 10 == 0:
                speed = func(x, sum_frame)
                speed = 1 / speed
            leiji = leiji + speed
            while leiji >= 1.0:
                leiji = leiji - 1.0
                out_q.put("1")
        out_q.put(_sentinel)

    def consumer(in_q):
        count = 0
        while True:
            data = in_q.get()
            if data is _sentinel:
                in_q.put(_sentinel)
                break
            else:
                count = count + 1
        print("%.2f" % (count / fps))

    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


def curve_speed(input_file, output_file, func):
    # 获得视频的格式
    videoCapture = cv2.VideoCapture(input_file)
    sum_frame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    videoWriter = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), fps, size)

    def producer(out_q):
        speed = 1
        leiji = 0.0
        for x in range(int(sum_frame)):
            _, frame = videoCapture.read()
            if x % 10 == 0:
                speed = func(x, sum_frame)
                speed = 1 / speed
            leiji = leiji + speed
            while leiji >= 1.0:
                leiji = leiji - 1.0
                out_q.put(frame)
        out_q.put(_sentinel)

    def consumer(in_q):
        while True:
            data = in_q.get()
            if data is _sentinel:
                in_q.put(_sentinel)
                break
            else:
                videoWriter.write(data)

    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


def get_parser():
    parser = argparse.ArgumentParser(description="curve_speed")
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', default="./")
    parser.add_argument('-b', '--build', required=True, type=int)
    parser.add_argument('-t', '--onlytime', default=False, type=bool)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_parser()
    input_file = args.input
    output_file = args.output
    build = args.build
    onlytime = args.onlytime
    if onlytime:
        if build == 1:
            mock_curve(input_file, mengtaiqi)
        elif build == 2:
            mock_curve(input_file, yingxiongshike)
        elif build == 3:
            mock_curve(input_file, zidanshijian)
        elif build == 4:
            mock_curve(input_file, tiaojie)
        elif build == 5:
            mock_curve(input_file, shanjin)
        elif build == 6:
            mock_curve(input_file, shanchu)
    else:
        if build == 1:
            curve_speed(input_file, output_file, mengtaiqi)
        elif build == 2:
            curve_speed(input_file, output_file, yingxiongshike)
        elif build == 3:
            curve_speed(input_file, output_file, zidanshijian)
        elif build == 4:
            curve_speed(input_file, output_file, tiaojie)
        elif build == 5:
            curve_speed(input_file, output_file, shanjin)
        elif build == 6:
            curve_speed(input_file, output_file, shanchu)
