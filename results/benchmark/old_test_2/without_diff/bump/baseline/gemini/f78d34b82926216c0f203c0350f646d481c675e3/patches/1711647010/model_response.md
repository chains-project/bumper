```java
  /**
     * ReLU関数で値を強めて出力系に入れる。
     *
     * @param inputData InputクラスのArrayListデータ。
     */
    public void input(ArrayList<Input> inputData)
    {
        double[] weightings = inputData.parallelStream().mapToDouble(input -> input.getWeightingValue()).toArray();
        input(weightings);
        setValue(sigmoid(sum));
    }
```