Here's a modified version of the client code that removes the dependency on the problematic library method:

```java
import static java.lang.Math.exp;

// ...

public static double sigmoid(double x) {
    return 1.0 / (1.0 + exp(-x));
}
```

This version of the `sigmoid` function uses the `exp` method from the `java.lang.Math` class instead of the problematic `sigmoid` method from the `develop.p2p.lib.LearnMath` class.