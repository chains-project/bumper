Here's a fixed version of the `input` method that should resolve the error:

```java
import ml.peya.plugins.Learn.develop.p2p.lib.LearnMath;

public void input(java.util.ArrayList<ml.peya.plugins.Learn.Input> inputData) {
    inputData.parallelStream().forEachOrdered(( input) -> input(input.getWeightingValue()));
    setValue(LearnMath.sigmoid(sum));
}
```

The error is caused by the missing import statement for `ml.peya.plugins.Learn.develop.p2p.lib.LearnMath`. By adding this import statement, the `sigmoid` method can be found.