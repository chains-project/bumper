```java
    public void input(ArrayList<Input> inputData)
    {
        List<Double> weights = new ArrayList<>();
        inputData.parallelStream().forEachOrdered(input -> weights.add(input.getWeightingValue()));
        setValue(sigmoid(sum));
    }
```