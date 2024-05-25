```java
    public void input(ArrayList<Input> inputData)
    {
        inputData.parallelStream().forEachOrdered(input -> {
            double weightingValue = input.getWeightingValue();
            setValue(sigmoid(weightingValue));
        });
    }
```