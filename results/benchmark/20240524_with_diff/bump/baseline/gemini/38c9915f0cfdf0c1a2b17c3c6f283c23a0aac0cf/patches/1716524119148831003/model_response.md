```java
import io.vavr.collection.List;
import io.vavr.control.Try;
import io.zold.api.WalletsIn;
import org.cactoos.text.TextOf;

public class WalletsInWithPatch {

    @SuppressWarnings("unchecked")
    public Try<List<String>> walletsIn(String apiKey) {
        return Try.of(() -> {
            String walletsInUrl = new TextOf(new WalletsIn.WalletsInUrl(apiKey)).asString();
            return WalletsIn.fetchWallets(walletsInUrl);
        });
    }
}
```