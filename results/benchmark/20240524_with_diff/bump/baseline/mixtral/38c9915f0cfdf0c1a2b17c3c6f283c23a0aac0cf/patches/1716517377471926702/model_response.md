Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarOf;

// ...

Scalar<Double> balance = new ScalarOf<>(() -> 100.0);
```

In this patch, I replaced the usage of `SolidScalar` with `ScalarOf`, which is a new class added in the updated library version. The `ScalarOf` class accepts a `java.util.concurrent.Callable` as a constructor argument. In this case, I provided a lambda expression that returns a `Double` value of 100.0 as the balance. You can replace the value with the appropriate balance calculation or retrieval logic for your specific use case.