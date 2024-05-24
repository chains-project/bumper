Here is a possible patch for the failing code:
```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

IoCheckedScalar<String> scalar = new IoCheckedScalar<>(() -> "Hello, world!");
IoCheckedBytes<String> bytes = new IoCheckedBytes(scalar);
String value = bytes.asBytes();
```
This code creates a new `IoCheckedScalar` that returns a string, then converts it to an `IoCheckedBytes` using the new `IoCheckedBytes` constructor, and finally extracts the bytes as a string using the `asBytes()` method.

Note that the `IoCheckedScalar` class has been removed in the new version, but it has been replaced by the `IoCheckedBytes` class, which can be used to achieve a similar result.

I hope this helps! Let me know if you have any questions.