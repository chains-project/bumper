```java
    /**
     * ReLU関数で値を強めて出力系に入れる。
     *
     * @param inputData InputクラスのArrayListデータ。
     */
    public void input(ArrayList<Input> inputData)
    {
        inputData.parallelStream().forEachOrdered(input -> input(input.getWeightingValue()));
        double sum = 0;
        for (Input input : inputData) {
            sum += input.getWeightingValue();
        }
        setValue(sigmoid(sum));
    }
```