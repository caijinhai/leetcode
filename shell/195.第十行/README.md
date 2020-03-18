## 第十行

```
sed -n '10p' file.txt
```

```
sed: https://man.linuxde.net/sed
-n 读取下一行用命令处理
p 打印
```

### 评论中其他答案
```
awk 'NR == 10' file.txt
NR在awk中指行号

sed -n 10p file.txt
-n表示只输出匹配行，p表示Print

tail -n+10 file.txt|head -1
tail -n +10表示从第10行开始输出
```

### 扩展
```
awk 打印最后一行
awk 'END{print}' file.txt

awk 打印特定行
awk 'NR==5{print}' file.txt
```