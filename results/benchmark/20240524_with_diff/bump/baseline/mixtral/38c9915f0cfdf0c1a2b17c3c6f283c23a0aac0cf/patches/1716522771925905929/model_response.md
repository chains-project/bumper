Here's the proposed patch:
```java
import org.cactoos.iterable.Filtered;

// ...

public class Wallet {
    // ...

    @Override
    public Wallet with(final Iterable<Coin> coins) {
        this.coins = new Filtered<>(coins, new CactoosCoin::isZol);
        return this;
    }

    // ...
}
```
In this patch, I replaced the usage of `org.cactoos.collection.Filtered` with `org.cactoos.iterable.Filtered`. The constructor signature has changed slightly, so the parameters are passed in a different order now.