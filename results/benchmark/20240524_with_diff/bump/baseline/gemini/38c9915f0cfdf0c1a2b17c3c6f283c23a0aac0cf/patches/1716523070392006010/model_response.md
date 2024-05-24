```java
import org.cactoos.text.Joined;

public class WalletsIn {

    public WalletsIn(String url) {
        // ...
        Joined wallets = new Joined(url, "/wallets");
        // ...
    }

}
```