## 最小栈

1. 要输出栈里面最小数，并且保证常数级，则必须要在push过程中记录最小值，并且和已上一步最小值比较取最小值
2. 同时要保证在pop过程中，上一步的最小值不丢失
push中（x, min_val）结构
min_val: min(x, data[-1][1])