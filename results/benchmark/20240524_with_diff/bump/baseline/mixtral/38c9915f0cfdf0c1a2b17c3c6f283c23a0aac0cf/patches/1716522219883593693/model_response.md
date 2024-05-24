Here's the patch for the failing client code:

```java
import org.cactoos.bytes.IoCheckedBytes;

//...

IoCheckedScalar<String> ioCheckedScalar = new IoCheckedScalar<>(
  new IoCheckedBytes(new BytesOf("some string"))
);
```

This code creates a new `IoCheckedScalar` using `IoCheckedBytes` to wrap a `BytesOf` object instead of the removed `Scalar$NoNulls` and `Scalar$NoNulls.value()`. The `BytesOf` class is used as a replacement for the removed `Scalar` class. The `IoCheckedBytes` class is used to handle any checked exceptions when reading bytes from the `BytesOf` object.