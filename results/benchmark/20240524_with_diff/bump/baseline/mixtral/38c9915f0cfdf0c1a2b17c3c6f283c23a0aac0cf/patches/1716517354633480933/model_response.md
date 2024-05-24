```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarOf;

// ...

Scalar<Integer> solidScalar = new ScalarOf<>(() -> 42);
```