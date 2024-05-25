Here's the proposed patch:
```java
import org.cactoos.Scalar;
import org.cactoos.scalar.StickyScalar;

Scalar<Double> scalar = new StickyScalar<>(() -> 0.0);
```
Explanation:
The error message suggests that a semicolon is missing. However, the import statement seems to be correct. Therefore, I suspect that the issue might be with the usage of the `Sticky` class from the `org.cactoos.scalar` package.
To fix the issue, I have created a variable `scalar` of type `Scalar<Double>` and initialized it with an instance of `StickyScalar` which takes a lambda expression that returns a double value of 0.0. This should resolve the compilation error.