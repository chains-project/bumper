Here's the patched version of the client code that uses the added `IoCheckedBytes` class from the new library version:

```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

public class RtNetwork {
  // ...

  private static byte[] getBytes(Scalar<URL> url) throws IOException {
    try (InputStream is = url.value().openStream()) {
      return new IoCheckedBytes(new BytesOf(is)).asBytes();
    }
  }

  // ...
}
```

The `getBytes` method uses `IoCheckedBytes` to read the contents of a URL into a byte array. The `BytesOf` class is used to convert the `InputStream` from the URL to a `Bytes` object, which is then passed to `IoCheckedBytes` to read the data. The `asBytes` method is then called on `IoCheckedBytes` to get the data as a byte array.

Note that `IoCheckedBytes` is used instead of `IoCheckedScalar` because the latter has been removed in the new library version. `IoCheckedBytes` provides similar functionality to `IoCheckedScalar`, but it is used for reading bytes instead of scalar values.