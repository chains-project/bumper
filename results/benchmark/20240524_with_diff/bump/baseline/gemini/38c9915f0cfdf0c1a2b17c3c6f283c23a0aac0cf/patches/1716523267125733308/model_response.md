```java
import org.cactoos.scalar.Solid;

public class WalletsIn {

    // ...

    public WalletsIn(Scalar<Boolean> isTestnet) {
        this.isTestnet = isTestnet;
    }

    // ...

    @Override
    public Scalar<String> wallets() {
        return new Solid<>(
            new Mapped<>(
                text -> text.asString(),
                new Sub(
                    new TextOfScalar(isTestnet),
                    new Solid<>(1)
                )
            )
        );
    }

    // ...
}
```