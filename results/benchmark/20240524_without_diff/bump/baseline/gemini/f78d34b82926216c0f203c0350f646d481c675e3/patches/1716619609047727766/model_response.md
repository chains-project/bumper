```java
  /**
     * ReLU関数で値を強めて出力系に入れる。
     *
     * @param inputData InputクラスのArrayListデータ。
     */
    public void input(ArrayList<Input> inputData)
    {
        for (Input input : inputData) {
            input(input.getWeightingValue());
        }
        setValue(sigmoid(sum));
    }
```