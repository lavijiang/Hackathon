# A Simple QQ ChatBot With ChatGPT

## 1 安装步骤
### 1.1 qq bot
https://docs.go-cqhttp.org/

### 1.2 配置bot config.yml
```
account: # 账号相关  
  uin: 2493233979 # QQ账号
  password: '' # 密码为空时使用扫码登录
```
```
- url: http://127.0.0.1:5701/ # 地址
    secret: ''                # 密钥
```

## 2 启动命令
nohup python3 main.py script.py >/dev/null 2>&1 &  
nohup ./go-cqhttp >/dev/null 2>&1 &