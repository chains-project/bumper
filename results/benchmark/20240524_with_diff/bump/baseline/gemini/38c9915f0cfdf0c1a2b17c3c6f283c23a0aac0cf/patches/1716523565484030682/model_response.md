```java
import org.cactoos.bytes.CheckedBytes;
import org.cactoos.bytes.IoCheckedBytes;
import org.cactoos.io.Checked;
import org.cactoos.io.IoChecked;
import org.cactoos.scalar.CheckedScalar;
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class WalletsIn {

    public static String getWalletsIn(String url) throws IOException {
        String walletsIn = null;
        try (IoCheckedBytes bytes = new IoCheckedBytes(new CheckedBytes(new CheckedScalar<>(url, String::getBytes), StandardCharsets.UTF_8))) {
            walletsIn = new String(bytes.asBytes(), StandardCharsets.UTF_8);
        }
        return walletsIn;
    }
}
```