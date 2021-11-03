#!/usr/bin/env python
import socket
import pandas as pd
import numpy as np
from datetime import datetime


def getIpodata(recvdata):
    datas = []
    lines = recvdata.split('\n')
    for line in lines:
        fields = line.split(',')
        if len(fields) > 7 and len(fields[6]) > 16:
            fields[7] = fields[6][0:6]
            fields[6] = fields[6][6:]
            fields[5] = fields[5][6:]
            datas.append(fields)

    return np.array(datas)


if __name__ == '__main__':
    myFile = open('/home/asterisk/ipodata/append.txt', 'a')
    myFile.write('\nAccessed on ' + str(datetime.now()))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # socket config
        host = "192.168.252.253"
        port = 9001

        s.connect((host, port))

        while True:
            data = s.recv(1024)
            print(str("receive data : " + data.decode()))

            if not data:
                print("data is null")
                break

            numArr = getIpodata(data.decode())
            print(numArr)
            df = pd.DataFrame(numArr)
            df.to_csv("/home/asterisk/ipodata/data.csv", mode='a', header=False, index=False)

