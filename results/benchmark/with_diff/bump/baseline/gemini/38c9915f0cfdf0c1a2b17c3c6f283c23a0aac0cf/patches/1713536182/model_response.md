```java
import org.cactoos.scalar.IoChecked;

import java.io.IOException;

public interface WalletsIn {

    IoChecked<String> walletsIn(String hash) throws IOException;
}
```