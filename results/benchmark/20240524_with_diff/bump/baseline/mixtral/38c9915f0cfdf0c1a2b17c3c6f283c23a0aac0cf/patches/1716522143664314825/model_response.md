Here's a possible patch for the client code:
```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

public RtTransaction(String id, Bytes data, Bytes signature, Scalar<Long> timestamp) {
  this.id = id;
  this.data = data;
  this.signature = signature;
  this.timestamp = timestamp;
  this.value = IoCheckedScalar.value(() -> new IoCheckedBytes(data).asBytes());
}
```
In this patch, we replaced the usage of `IoCheckedScalar` with `IoCheckedBytes` and used its `asBytes()` method to get the byte array representation of the data. We then passed this byte array to the constructor of `IoCheckedScalar` to get a scalar value that can be assigned to `this.value`.

Note that this patch assumes that the `Bytes` class and the `Scalar` class are still available in the updated library, and that they have not changed significantly. If this is not the case, additional changes may be necessary.