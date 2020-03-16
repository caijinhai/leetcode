# shell词频统计

<font color="#4285f4">更</font>
<font color="#ea4335">丰</font>
<font color="#fbbc05">富</font>
<font color="#4285f4">的</font>
<font color="#34a853">颜</font>
<font color="#ea4335">色</font>

<font color=#fbbc05>cat words.txt| tr ' ' '\n'| tr -s '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'</font>

```shell
cat words.txt| tr ' ' '\n'| tr -s '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
```


[linux命令大全](https://man.linuxde.net/)

```
tr: https://man.linuxde.net/tr
删除，替换(-d)，压缩(-s)

sort: https://man.linuxde.net/sort
文件排序
-n(数字从小到大), -r(倒序) -k 第几列, -t 分隔

uniq: https://man.linuxde.net/uniq
-c或——count：在每列旁边显示该行重复出现的次数；
-d或--repeated：仅显示重复出现的行列

awk: https://man.linuxde.net/awk
awk 'BEGIN{ commands } pattern{ commands } END{ commands }'
```

### 除去空行的四种方式
```shell
cat words.txt | tr -s '\n'

cat words.txt | sed '/^$/d'

cat words.txt | awk '{if($0 != "")print}'
cat words.txt | awk '{if(length != 0)print $0}'

cat words.txt | grep -v "^$"
```

```
grep: https://man.linuxde.net/grep
-v 反转查找
```