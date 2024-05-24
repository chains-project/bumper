Here's the proposed patch:

```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.input.InputOf;
import org.cactoos.text.TextOf;

//...

public class WalletsIn {
    //...

    private IoCheckedBytes checkedBytes(InputStream input) {
        return new IoCheckedBytes(new BytesOf(input));
    }

    private TextOf textOf(IoCheckedBytes checkedBytes) {
        return new TextOf(new InputOf(checkedBytes.asBytes()));
    }

    //...
}
```

In this patch, I replaced the usage of `IoCheckedScalar` with `IoCheckedBytes` and `TextOf`. The `IoCheckedBytes` class can be used to read from an `InputStream` and handle checked exceptions, while `TextOf` can convert bytes to a string. This should resolve the "cannot find symbol" error related to `IoCheckedScalar`.