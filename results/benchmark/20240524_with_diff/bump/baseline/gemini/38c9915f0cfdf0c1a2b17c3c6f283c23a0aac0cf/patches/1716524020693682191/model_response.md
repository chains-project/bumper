```java
import org.cactoos.scalar.Solid;

public class WalletsIn {

    // ...

    public static Solid<String> getWalletId(String walletName) {
        return new Solid<>(walletName);
    }

    // ...

}
```