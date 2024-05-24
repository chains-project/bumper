Here's a patch that you can apply to your code to fix the error:
```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.io.InputOf;

// ...

public RtTransaction(String hash) {
  super(
    new IoCheckedScalar<>(
      new InputOf(
        new ByteSourceOf(
          new IoCheckedBytes(
            new BytesOf(hash),
            string -> string.getBytes()
          )
        )
      )
    )
  );
}
```
In this patch, we replaced the `IoCheckedScalar` import with the new `IoCheckedBytes` import. We then wrapped the `BytesOf(hash)` call with `IoCheckedBytes` to handle any checked exceptions that might be thrown during the conversion of the string to bytes. The `string -> string.getBytes()` function is used as a fallback to convert the string to bytes.