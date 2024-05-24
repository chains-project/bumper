Here is the proposed patch:
```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.input.InputOf;
import org.cactoos.text.TextOf;

// ...

public RtTransaction(File file, RtDb db, RtApi api) {
  super(file, db, api);
  this.data = IoCheckedBytes.bytesOf(
    new InputOf(
      new TextOfScalar(
        new ScalarOf(
          () -> new String(
            Files.readAllBytes(file.toPath()))
        )
      )
    )
  );
}
```
Explanation:
The `IoCheckedScalar` class has been removed in the new library version. Instead, we can use a combination of `IoCheckedBytes`, `InputOf`, `TextOf`, and `ScalarOf` classes to achieve the same functionality.
The `Files.readAllBytes` method is used to read the contents of the file into a byte array. Then, a `ScalarOf` is used to create a scalar that returns the byte array. This scalar is then passed to a `TextOfScalar` to convert it to a `Text` object, which is then passed to an `InputOf` to convert it to an `Input` object. Finally, an `IoCheckedBytes` is used to create a checked bytes object that reads from the input.
This new implementation should achieve the same functionality as the original implementation using `IoCheckedScalar`.