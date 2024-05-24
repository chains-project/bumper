Here's the patched version of the client code:
```java
import org.cactoos.Scalar;
import org.cactoos.scalar.NoNulls;

// ...

private Scalar<ByteArrayResource> resource() {
    return new NoNulls<>(new UncheckedBytes(bytes -> new ByteArrayResource(bytes.asBytes())));
}
```
I replaced the usage of `UncheckedScalar` with `NoNulls` and added a lambda function for `UncheckedBytes`. This should resolve the compilation error.