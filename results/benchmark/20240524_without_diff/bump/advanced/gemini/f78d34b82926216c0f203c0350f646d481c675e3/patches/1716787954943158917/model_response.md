```java
/**
 * ReLU関数で値を強めて出力系に入れる。
 *
 * @param inputData
 * 		InputクラスのArrayListデータ。
 */
public void input(java.util.ArrayList<ml.peya.plugins.Learn.Input> inputData) {
    inputData.parallelStream().forEachOrdered(( input) -> input(input.getWeightingValue()));
    double sigmoid = develop.p2p.lib.LearnMath.sigmoid(sum);
    setValue(sigmoid);
}
```