Here's the fixed version of the failing method using the added `IoCheckedBytes` class:

```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

public RtTransaction(final Bytes source, final Bytes destination) {
  this.source = new IoCheckedBytes(source);
  this.destination = new IoCheckedBytes(destination);
}
```