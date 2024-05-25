Here is the proposed patch:
```java
import org.cactoos.Scalar;
import org.cactoos.scalar.StickyScalar;

Scalar<Double> scalar = new StickyScalar<>(() -> 0.0);
```
Explanation:
The error message suggests that a semicolon is missing in the code. However, the code snippet provided does not seem to have any syntax errors. Therefore, I assume that the issue might be caused by a change in the `Sticky` class of the `cactoos` library.

To fix the issue, I have imported the `Scalar` interface from `cactoos` and used the `StickyScalar` class as an implementation of the `Scalar` interface. The `StickyScalar` class returns a sticky value, which remains the same until it is explicitly changed. In this case, I have initialized the `StickyScalar` with a lambda expression that returns a double value of 0.0.

Note: This patch assumes that the rest of the code in the `RtScore` class is using the `scalar` variable correctly. If there are any further issues, please provide more context or code snippets for a more accurate solution.