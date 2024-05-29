Here's a fixed version of the `input` method that uses the `sigmoid` method from `develop.p2p.lib.LearnMath` instead of `develop.p2p.lib.LearnMath.sigmoid`:
```java
import static develop.p2p.lib.LearnMath.sigmoid;

// ...

public void input(java.util.ArrayList<ml.peya.plugins.Learn.Input> inputData) {
    inputData.parallelStream().forEachOrdered(( input) -> input(input.getWeightingValue()));
    setValue(sigmoid(sum));
}
```
This assumes that the `sigmoid` method is static, as it is in the original code that uses `develop.p2p.lib.LearnMath.sigmoid`. If it's not, you can create an instance of `develop.p2p.lib.LearnMath` and call the method on that instance instead.