Here's the fixed version of the failing client code:

```java
import org.cactoos.scalar.ScalarOf;

// ...

Scalar<Integer> scalar = new ScalarOf<Integer>(() -> 42);
Sticky<Integer> sticky = new Sticky<>(scalar);
```

The `StickyScalar` class has been removed in the new version. Instead, you can use the `Sticky` class, which is a generic version of `StickyScalar`. The `ScalarOf` class can be used to create a `Scalar` instance from a `Supplier`. In this example, a lambda expression is used to create a simple `Supplier`.