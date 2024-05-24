Here's the fixed version of the code:

```java
import org.cactoos.Scalar;
import org.cactoos.io.IoCheckedBytes;
import org.cactoos.io.InputOf;
import org.cactoos.text.TextOf;

// ...

public RtTransaction(String hash, Scalar<ByteSequence> data) {
  this.hash = hash;
  this.data = data;
  this.bytes = new IoCheckedBytes(
    new InputOf(
      new TextOfScalar(
        new BytesOf(data)
      )
      .asString()
    ),
    new FallbackOf(
      () -> new BytesOf("")
    )
  );
}
```

The changes include:

* Importing the new `IoCheckedBytes` class.
* Creating a `TextOfScalar` from the `data` `Scalar` to convert it to a `String`.
* Creating an `InputOf` from the `TextOfScalar` to convert it to an `InputStream`.
* Creating an `IoCheckedBytes` from the `InputOf` using a `FallbackOf` to handle any exceptions.
* Using the `bytes` `IoCheckedBytes` instead of the `IoCheckedScalar` in the rest of the method.