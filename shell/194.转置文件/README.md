## 转置文件

```
cat file.txt| awk '{if(length !=0) {print}}' | awk '{for(i=1;i<=NF;i++){if(arr[i]){arr[i]=arr[i]" "$i}else{arr[i]=$i}}}END{for(j=1;j<=length(arr);j++){print arr[j]}}'
```

```
awk: https://man.linuxde.net/awk
awk命令重要的点：
awk -F '分隔符' 'BEGIN{输入流执行前}{每行输入流均执行}END{输入流执行后}'

特殊变量
NF: 列数
NR: 行数
$1: 第一列
$NF: 最后一列
$NR: 最后一行
$0: 整行输入流

注意变量，数组在awk命令的使用方式
for(a in arr)在awk中无序的方式执行，并不一定是下标递增
```

### 评论中其他方式
```
transpose=`head -n1 file.txt | wc -w`

for i in `seq 1 $transpose`
do
    echo `cut -d' ' -f$i file.txt`
done
```

```
head -n1 取第一行
wc -w 按单词维度统计
cut -d' ' -f1 按空格分隔读取第一列
```