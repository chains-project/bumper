Here is the proposed patch:
```java
import org.cactoos.bytes.BytesOf;
import org.cactoos.text.Abbreviated;
import org.cactoos.text.Base64Decoded;
import org.cactoos.text.Base64Encoded;
import org.cactoos.text.Capitalized;
import org.cactoos.text.Concatenated;
import org.cactoos.text.Contains;
import org.cactoos.text.EndsWith;
import org.cactoos.text.FormattedText;
import org.cactoos.text.IoCheckedText;
import org.cactoos.text.IsEmpty;
import org.cactoos.text.Joined;
import org.cactoos.text.Lowered;
import org.cactoos.text.Mapped;
import org.cactoos.text.NoNulls;
import org.cactoos.text.Normalized;
import org.cactoos.text.PaddedStart;
import org.cactoos.text.Replaced;
import org.cactoos.text.Reversed;
import org.cactoos.text.Rotated;
import org.cactoos.text.Split;
import org.cactoos.text.StartsWith;
import org.cactoos.text.Sticky;
import org.cactoos.text.Strict;
import org.cactoos.text.Sub;
import org.cactoos.text.SwappedCase;
import org.cactoos.text.Synced;
import org.cactoos.text.TextOfScalar;
import org.cactoos.text.TextOfString;
import org.cactoos.text.Trimmed;
import org.cactoos.text.TrimmedLeft;
import org.cactoos.text.TrimmedRight;
import org.cactoos.text.UncheckedText;
import org.cactoos.text.Upper;

// ...

import static org.cactoos.text.TextOf.string;

// ...

public class Wallet {
    // ...

    private String[] split(String text) {
        return new Split(
            text, "\n"
        ).asString().split("\n");
    }

    // ...
}
```
The changes include:

* Importing the new classes that replace the removed ones.
* Updating the `split` method to use the new `Split` class instead of `SplitText`.
* Creating a `TextOf.string()` method call to convert the input `String` to a `Text` instance, which is accepted by the new `Split` constructor.
* Using `asString()` method to convert the `Split` instance back to a `String` instance.
* Splitting the resulting `String` using `split()` method to get the original array of `String` instances.