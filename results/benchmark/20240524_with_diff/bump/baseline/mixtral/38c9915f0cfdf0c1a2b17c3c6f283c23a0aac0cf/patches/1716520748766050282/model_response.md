```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarOf;

// ...

Scalar<Double> amount = new ScalarOf<>(() -> 5.0);
```