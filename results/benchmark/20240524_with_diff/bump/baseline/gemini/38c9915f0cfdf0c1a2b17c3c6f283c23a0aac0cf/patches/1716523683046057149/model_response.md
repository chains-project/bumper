```java
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.scalar.IoChecked;

import java.io.IOException;

public class WalletsIn {

    public String getWallets(String url) throws IOException {
        return new IoCheckedBytes(
                new IoChecked<>(
                        () -> url
                )
        ).asBytes().toString();
    }

}
```