```java
import org.cactoos.text.TextOf;

import java.io.File;

public class WalletsIn {

    private final File walletsDir;

    /**
     * Ctor.
     * @param walletsDir The wallets directory
     */
    public WalletsIn(final File walletsDir) {
        this.walletsDir = walletsDir;
    }

    // @Override
    public SolidScalar<String> wallets() {
        return new TextOf(this.walletsDir);
    }
}

```