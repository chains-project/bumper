```java
/**
 * ReLU関数で値を強めて出力系に入れる。
 *
 * @param inputData InputクラスのArrayListデータ。
 */
public void input(ArrayList<Input> inputData)
{
    inputData.parallelStream().forEachOrdered(input -> {
        double weightingValue = input.getWeightingValue();
        input(weightingValue);
    });
    setValue(sigmoid(sum));
}
```