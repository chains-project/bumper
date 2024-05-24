Here's the fixed version of the client code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoCheckedScalar;

public class RtTransaction {
    // ...
    private Scalar<Bytes> content;

    @Override
    public Bytes content() throws IOException {
        return new IoCheckedScalar<>(this.content, Bytes::new).value();
    }
    // ...
}
```

The change I made is to replace the direct use of `IoCheckedScalar` with a new instance created using the `IoCheckedScalar` constructor that takes a `Scalar` and a function to convert the scalar's value to a `Bytes` object. This way, the new version of the library is used without directly referencing any of the removed classes or methods.