import pymysql

def getIp():
    ipaddr = []
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='5801200zxg',
        db='proxy',
        charset='utf8'
    )
    cursor = conn.cursor()

    cursor.execute("select ip,port from proxys where score = 10 and speed < 0.5")
    a = cursor.fetchall()
    # print(a)
    for i in a:
        dict = {}
        dict["ipaddr"] = str(i[0]) + ":" + str(i[1])
        ipaddr.append(dict)
    print(ipaddr)
    # print(ipaddr)
    # a = (('166.111.80.162', 3128), ('211.159.177.212', 3128), ('123.116.242.190', 8118), ('120.26.14.14', 3128), ('203.174.112.13', 3128), ('101.247.172.40', 80), ('118.97.191.205', 8080), ('42.115.88.12', 65103), ('101.132.148.7', 8080), ('139.59.114.21', 8080), ('96.9.69.210', 53281), ('61.247.187.166', 8080), ('177.134.218.237', 8080), ('39.134.68.9', 80), ('114.251.228.124', 3128), ('148.72.168.178', 1080), ('61.155.164.111', 3128), ('211.159.171.58', 80), ('124.206.133.219', 3128), ('120.77.223.86', 3128), ('163.172.211.176', 3128), ('47.88.20.189', 80), ('202.85.213.220', 3128), ('139.217.24.50', 3128), ('61.6.148.162', 53281), ('120.25.81.117', 80), ('103.252.184.65', 53281), ('37.228.89.215', 80), ('190.2.132.14', 1080), ('176.235.11.8', 8080), ('69.195.129.204', 1080), ('218.241.234.48', 8080), ('200.89.98.38', 42619), ('185.35.137.184', 3128), ('118.185.159.137', 53281), ('123.112.18.228', 53281), ('45.124.145.34', 8080), ('27.123.1.46', 65103), ('61.155.164.112', 3128), ('222.73.68.144', 8090), ('116.228.44.9', 8085), ('174.32.127.27', 87), ('222.255.122.58', 3128), ('110.232.83.115', 8080), ('177.131.51.155', 53281), ('113.207.42.103', 80), ('125.62.26.75', 3128), ('218.67.159.91', 9999), ('218.67.159.88', 9999), ('119.249.48.235', 80), ('101.31.146.3', 80), ('111.62.243.64', 8080), ('111.62.243.64', 80), ('124.165.252.72', 80), ('124.165.252.72', 8080), ('124.165.252.72', 8081), ('124.163.209.110', 80), ('118.81.71.180', 9797), ('118.81.71.131', 9797), ('124.165.252.72', 9999), ('218.106.205.145', 8080), ('119.49.144.83', 80), ('122.136.212.132', 53281), ('222.169.248.3', 80), ('218.203.56.228', 80), ('58.220.95.107', 8080), ('58.220.95.107', 80), ('221.226.20.158', 8080), ('183.207.194.221', 3128), ('221.231.109.40', 3128), ('218.2.80.59', 80), ('112.33.20.244', 3128), ('61.155.164.110', 3128), ('180.115.81.161', 808), ('61.155.164.108', 3128), ('61.155.164.109', 3128), ('218.2.80.59', 8080), ('61.155.164.106', 3128), ('218.2.80.126', 80), ('218.108.93.198', 1080), ('121.43.178.58', 3128), ('115.225.157.179', 808), ('61.155.164.107', 3128), ('125.121.174.168', 808), ('114.97.185.150', 808), ('110.86.102.99', 808), ('220.249.185.178', 9797), ('119.27.189.65', 80), ('119.27.177.169', 80), ('59.56.46.81', 808), ('59.57.33.9', 808), ('218.64.92.183', 808), ('223.84.129.156', 8123), ('119.164.98.121', 8118), ('60.214.154.2', 53281), ('27.221.93.217', 80), ('60.214.155.243', 53281), ('122.114.65.20', 3128), ('219.155.11.141', 8118), ('123.55.152.168', 808), ('61.53.65.54', 3128), ('115.52.196.239', 8118), ('42.51.201.251', 1080), ('125.46.69.18', 3128), ('202.103.14.155', 8118), ('27.19.170.86', 8118), ('220.249.96.135', 8089), ('116.211.123.138', 80), ('223.159.99.100', 8118), ('175.15.172.232', 808), ('222.240.81.3', 8088), ('218.75.217.61', 8998), ('58.20.246.206', 53281), ('119.39.74.213', 80), ('118.254.144.211', 3128), ('58.253.116.125', 80), ('27.46.74.8', 9999), ('27.46.48.108', 9797), ('113.68.188.252', 9999), ('183.49.85.43', 8118), ('101.37.79.125', 3128), ('113.93.224.54', 9797), ('219.135.164.245', 3128), ('183.30.204.174', 9999), ('58.252.6.165', 9000), ('219.223.251.173', 3128), ('163.177.151.23', 80), ('119.145.203.58', 80), ('221.10.159.234', 1337), ('183.223.241.242', 80), ('118.114.77.47', 8080), ('220.166.241.246', 8118), ('223.85.196.75', 9999), ('116.196.104.164', 1080), ('112.114.99.167', 8118), ('112.114.78.89', 8118), ('112.114.96.134', 8118), ('112.114.98.221', 8118), ('112.114.97.15', 8118), ('112.114.97.244', 8118), ('202.100.83.139', 80), ('113.200.101.200', 80), ('61.134.29.13', 8080), ('113.200.214.164', 9999), ('118.171.24.101', 3128), ('125.231.91.31', 3128), ('1.175.139.9', 3128), ('118.171.221.58', 3128), ('218.161.47.231', 3128), ('182.88.26.53', 9797), ('221.7.255.167', 80), ('221.7.255.168', 80), ('221.7.255.167', 8080), ('221.7.255.168', 8080), ('116.11.254.37', 80), ('218.202.219.82', 80), ('218.202.219.82', 81), ('218.202.219.82', 82), ('1.65.218.170', 8118), ('36.55.230.154', 3128), ('117.18.15.12', 3128), ('39.106.97.102', 8080), ('59.188.255.229', 1080), ('103.6.4.3', 3128), ('111.68.7.35', 1080), ('42.98.222.237', 8888), ('168.63.139.99', 3128), ('43.240.6.218', 53281), ('119.28.50.37', 82), ('218.103.42.106', 1080), ('202.175.186.36', 8080), ('124.133.230.254', 80), ('61.234.123.16', 82), ('118.144.149.206', 3128), ('59.41.204.222', 53281), ('113.83.241.17', 8118), ('113.206.129.132', 8118), ('111.13.111.184', 80), ('112.80.255.32', 80), ('120.241.0.52', 80), ('111.2.122.46', 8080), ('47.92.73.2', 8088), ('114.215.174.227', 8080), ('39.137.83.131', 8080), ('114.216.128.51', 8118), ('171.34.197.71', 3128), ('220.181.163.231', 80), ('163.177.151.162', 80), ('14.215.177.58', 80), ('123.125.142.40', 80), ('61.160.190.146', 8090), ('120.24.230.217', 8088), ('39.137.83.133', 80), ('211.159.219.158', 80), ('119.28.128.206', 9000), ('47.95.36.13', 8081), ('139.224.24.26', 8888), ('27.36.116.226', 3128), ('180.97.104.14', 80), ('61.160.190.147', 8090), ('183.146.211.142', 8080), ('39.137.83.130', 8080), ('223.112.84.30', 3128), ('218.26.217.77', 3128), ('111.204.197.194', 3128), ('113.207.44.70', 3128), ('124.65.133.94', 3128), ('58.216.14.65', 8888), ('40.125.164.240', 8088), ('139.224.104.120', 1080), ('117.117.196.9', 80), ('14.215.177.73', 80), ('139.199.49.13', 80), ('171.221.116.110', 9000), ('116.199.115.78', 80), ('202.85.213.219', 3128), ('121.8.98.197', 80), ('36.36.201.253', 8080), ('120.79.133.212', 8088), ('47.95.36.86', 8081), ('116.199.115.79', 80), ('114.215.102.168', 8081), ('140.143.96.141', 80), ('101.201.79.172', 808), ('118.144.187.254', 3128), ('119.129.99.0', 9797), ('123.156.103.46', 8080), ('157.255.144.77', 80), ('140.205.222.3', 80), ('114.115.140.25', 3128), ('60.205.125.201', 8888), ('183.214.79.102', 9797), ('47.96.250.208', 3128), ('112.114.77.245', 8118), ('106.2.6.23', 3128), ('112.114.77.174', 8118), ('121.8.98.198', 80), ('153.3.235.82', 80), ('112.114.96.161', 8118), ('39.137.83.132', 8080), ('183.153.29.88', 808), ('139.196.122.166', 8080), ('112.74.176.242', 3128), ('45.221.221.147', 65205), ('106.14.12.240', 8082), ('58.215.120.223', 3128), ('112.114.77.92', 8118), ('121.69.6.254', 8118), ('120.199.64.163', 8081), ('123.207.25.143', 3128), ('39.73.124.159', 8888), ('120.27.49.85', 8090), ('140.143.96.216', 80), ('61.4.184.180', 3128), ('112.80.255.21', 80), ('120.77.201.46', 8080), ('183.174.228.95', 8080), ('119.23.252.11', 8080), ('103.228.246.24', 8080), ('116.242.232.21', 808), ('180.173.71.70', 9797), ('163.125.74.242', 9797), ('182.121.205.156', 9999), ('183.30.197.220', 9797), ('14.153.53.203', 3128), ('122.234.217.161', 9999), ('219.137.206.25', 53281), ('113.89.55.21', 9999), ('59.78.5.96', 1080), ('58.253.111.11', 80), ('163.125.156.13', 8888), ('113.110.228.48', 9797), ('14.221.165.151', 808), ('112.114.99.9', 8118), ('182.88.14.35', 8123), ('112.114.92.2', 8118))
    # return a

getIp()