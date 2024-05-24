Here's a possible patch for the client code:
```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

IoCheckedScalar<String> scalar = new IoCheckedScalar<>(() -> "Hello, world!");
IoCheckedBytes<String> bytes = new IoCheckedBytes(scalar);
String value = bytes.asBytes();
```
Here, we're using the new `IoCheckedBytes` class to wrap a `Scalar` that produces a `String` value. We then convert the `IoCheckedBytes` to a byte array using the `asBytes()` method.

Note that this patch assumes that the `IoCheckedScalar` class has been removed from the library, as indicated by the `--` symbol in the library changes. If `IoCheckedScalar` is still available, you can use it directly instead of wrapping it with `IoCheckedBytes`.