Here's a patch that you can apply to fix the error:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.Unchecked;

// ...

Scalar<Bytes> bytes = new Unchecked<>(() -> ...);
```

In the above code, replace the `...` with the code that was previously used to create an instance of `UncheckedScalar`. This should fix the error.