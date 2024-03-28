```java
  /**
     * ReLU関数で値を強めて出力系に入れる。
     *
     * @param inputData InputクラスのArrayListデータ。
     */
    public void input(ArrayList<Input> inputData)
    {
        ArrayList<Double> weightingValues = new ArrayList<>();
        inputData.forEach(input -> weightingValues.add(input.getWeightingValue()));
        weightingValues.parallelStream().forEachOrdered(weightingValue -> input(weightingValue));
        setValue(sigmoid(sum));
    }
```