```java
import org.cactoos.scalar.Checked;
import org.cactoos.text.TextOfScalar;

public class WalletsIn {

    public WalletsIn(final String url, final String token) {
        final String wallets = new Checked<>(
            new TextOfScalar(token),
            token -> String.format("%s/wallets", url)
        ).value();
    }
}
```