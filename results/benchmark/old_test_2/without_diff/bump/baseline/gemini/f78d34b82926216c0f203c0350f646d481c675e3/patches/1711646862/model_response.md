```java
public void input(ArrayList<Input> inputData)
{
    for (Input input : inputData) {
        input(input.getWeightingValue());
    }
    setValue(sigmoid(sum));
}
```