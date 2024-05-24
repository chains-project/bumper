Here is the proposed patch:
```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.Scalar;

public class RtTransaction {
  ...
  private Scalar<Bytes> content() {
    return new IoCheckedBytes(
      new BytesOf(() -> new String(data, StandardCharsets.UTF_8))
    );
  }
  ...
}
```
Explanation:
The error message indicates that the class `IoCheckedScalar` cannot be found in the package `org.cactoos.scalar`. Upon checking the library changes, we can see that the class has been removed. Instead, we can use the `IoCheckedBytes` class, which can convert a `Bytes` object to a `Scalar` object. We can create a `Bytes` object using the `BytesOf` class, which takes a `Callable` object that returns a byte array. In this case, we can use a lambda expression to convert the `data` byte array to a string using `StandardCharsets.UTF_8`, and then convert the string to a byte array.