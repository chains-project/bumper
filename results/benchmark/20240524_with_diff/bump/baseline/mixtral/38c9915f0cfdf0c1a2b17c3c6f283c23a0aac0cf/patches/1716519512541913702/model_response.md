```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarOf;

// ...

Scalar<Double> solidScalar = new ScalarOf<>(() -> 42.0);
```