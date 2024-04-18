```java
    public void input(ArrayList<Input> inputData)
    {
        double[] values = inputData.parallelStream().mapToDouble(input -> input.getWeightingValue()).toArray();
        setValue(sigmoid(sum));
    }
```