```java
  /**
     * ReLU関数で値を強めて出力系に入れる。
     *
     * @param inputData InputクラスのArrayListデータ。
     */
    public void input(ArrayList<Input> inputData)
    {
        double[] weights = inputData.parallelStream().mapToDouble(input -> input.getWeightingValue()).toArray();
        setValue(sigmoid(sum));
    }
```