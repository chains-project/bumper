```java
import org.cactoos.bytes.IoCheckedBytes;

public class WalletsIn {

    public IoCheckedBytes read(String path) {
        return new IoCheckedBytes(new IoCheckedBytes(path));
    }
}
```