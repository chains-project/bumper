Here is the proposed patch:
```java
import org.cactoos.text.Joined;
import org.cactoos.text.TextOf;

...

public RtTransaction(String raw, Repo repo) {
    super(raw, repo);
    this.parts = new Joined(",", new TextOf(
        new Split(
            ",",
            new TextOf(raw)
        )
    ).asString().split("\\s"));
}
```
This patch uses the new `Joined` and `TextOf` classes to split the `raw` string into parts using a `,` delimiter and then split each part into words using a space delimiter. The resulting array of words is assigned to the `parts` field.