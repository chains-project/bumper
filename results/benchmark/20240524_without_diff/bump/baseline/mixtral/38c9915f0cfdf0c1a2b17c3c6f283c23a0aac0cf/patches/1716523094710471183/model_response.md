Here is the proposed patch:
```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.FormattedText;
import org.cactoos.text.Joined;
import org.cactoos.text.TextOf;
import org.cactoos.text.UncheckedText;

...

public class Wallet {
    ...
    private static final TextOf<String> TEXT_OF = new TextOf<>("%s: %s\n", "%s: %d\n");
    ...
    @Override
    public String toString() {
        return new FormattedText(
            new Joined(
                "\n",
                new UncheckedText(
                    new TextOf<>("ID: %s\n", this.id())
                ),
                new UncheckedText(
                    new TextOf<>("Balance: %s\n", this.balance())
                ),
                new UncheckedText(
                    new TextOf<>("Created at: %s\n", this.createdAt())
                ),
                new UncheckedText(
                    new TextOf<>("Updated at: %s\n", this.updatedAt())
                ),
                new UncheckedText(
                    new TextOf<>("Public key: %s\n", this.publicKey())
                ),
                new UncheckedText(
                    new TextOf<>("Private key: %s\n", this.privateKey())
                ),
                new UncheckedText(
                    new TextOf<>("Seed: %s\n", this.seed())
                ),
                new UncheckedText(
                    new TextOf<>("Address: %s\n", this.address())
                ),
                new UncheckedText(
                    new TextOf<>("Spent: %s\n", this.spent())
                ),
                new UncheckedText(
                    new TextOf<>("Blocked: %s\n", this.blocked())
                ),
                new UncheckedText(
                    new TextOf<>("Frozen: %s\n", this.frozen())
                ),
                new UncheckedText(
                    new TextOf<>("Paused: %s", this.paused())
                )
            )
        ).asString();
    }
    ...
}
```
In this patch, I replaced the `SplitText` class with the `TextOf` and `UncheckedText` classes from the new library version. I also replaced the `String.format` method with the `FormattedText` and `Joined` classes from the new library version. This should fix the error and allow the code to compile and run successfully.