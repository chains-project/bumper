```java
public void input(java.util.ArrayList<ml.peya.plugins.Learn.Input> inputData) {
    double sum = 0;
    for (ml.peya.plugins.Learn.Input input : inputData) {
        sum += input.getWeightingValue();
    }
    setValue(1 / (1 + java.lang.Math.exp(-sum)));
}
```