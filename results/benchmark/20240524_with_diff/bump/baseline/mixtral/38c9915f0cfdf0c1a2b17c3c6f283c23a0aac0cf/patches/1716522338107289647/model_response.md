Here is the proposed patch:
```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

public class RtNetwork {
  // ...

  private IoCheckedBytes input;

  // ...

  @Override
  protected void initInputs() throws IOException {
    this.input = IoCheckedBytes.valueOf(
      IoChecksum.md5(
        Files.newInputStream(Paths.get("input.txt"))
      )
    );
  }

  // ...
}
```
In this patch, I replaced the usage of `IoCheckedScalar` with `IoCheckedBytes`, which is a new class added in the updated library version. The `IoCheckedBytes` class provides a similar functionality to `IoCheckedScalar`, but it works with bytes instead of scalar values.

In the `initInputs` method, I used the `IoCheckedBytes.valueOf` method to create an `IoCheckedBytes` instance from the MD5 checksum of the input file. This way, we can still ensure the integrity of the input data while using the new library version.