Here's the fixed version of the code, using the `UncheckedBytes` method added in the new library version:

```java
import org.cactoos.bytes.UncheckedBytes;

// ...

public RtTransaction(String id, Bytes data, Bytes hash, Bytes sign, Scalar<Long> nonce) {
    this.id = id;
    this.data = new UncheckedBytes(data);
    this.hash = new UncheckedBytes(hash);
    this.sign = new UncheckedBytes(sign);
    this.nonce = new UncheckedScalar<>(nonce);
}
```