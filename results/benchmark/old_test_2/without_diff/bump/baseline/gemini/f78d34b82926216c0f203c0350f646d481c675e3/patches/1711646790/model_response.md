```java
    public void input(ArrayList<Input> inputData)
    {
        inputData.parallelStream().forEachOrdered(input -> input(input.getWeightingValue()));
        double[] values = inputData.stream().mapToDouble(Input::getWeightingValue).toArray();
        setValue(sigmoid(values));
    }
```