```java
import java.util.List;
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

public class WalletsIn {

    public static String getWalletsIn(List<String> wallets) {
        return new UncheckedText(
                new JoinedText(
                        ",\n",
                        wallets
                )
        ).asString();
    }
}
```