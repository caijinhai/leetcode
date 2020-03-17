## 193.有效电话号码

```bash
cat file.txt| awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/{print}'
```

`此题主要是涉及正则表达式, 注意括号后面有一个空格`
[0-9]: 匹配数字
{n}: 匹配多次

评论中提供了三种解法：
```
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-([0-9]{4})$/' file.txt
```

[linux命令大全](https://man.linuxde.net/
```
sed: https://man.linuxde.net/sed
awk: https://man.linuxde.net/awk
```