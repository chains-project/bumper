Here is the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

//...

public RtTransaction(RtAccount src, RtAccount dst, byte[] data) {
    this.src = src;
    this.dst = dst;
    this.data = data;
    this.len = new LengthOf<>(Arrays.asList(data));
}
```
In the patch, I replaced the `org.cactoos.iterable.LengthOf` with `org.cactoos.scalar.LengthOf` which is a new class added in the updated library version. Additionally, I changed the argument of `LengthOf` from `data` to `Arrays.asList(data)` since `LengthOf` now expects an `Iterable` instead of an array.