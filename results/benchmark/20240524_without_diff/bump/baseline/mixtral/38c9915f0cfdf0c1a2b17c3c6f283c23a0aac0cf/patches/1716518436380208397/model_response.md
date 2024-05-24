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
import org.cactoos.text.Mapped;
import org.cactoos.text.NoNulls;
import org.cactoos.text.Normalized;
import org.cactoos.text.PaddedStart;
import org.cactoos.text.PrefixOf;
import org.cactoos.text.Replaced;
import org.cactoos.text.Reversed;
import org.cactoos.text.Rotated;
import org.cactoos.text.SuffixOf;
import org.cactoos.text.SwappedCase;
import org.cactoos.text.Synced;
import org.cactoos.text.Trimmed;
import org.cactoos.text.TrimmedLeft;
import org.cactoos.text.TrimmedRight;
import org.cactoos.text.UncheckedText;
import org.cactoos.text.Upper;

// ...

import static org.cactoos.text.TextOf.string;

// ...

  import org.cactoos.text.Split;
 
  private String[] split(String text, String separator) {
    return new Split(text, separator).asArray();
  }
```
The main change is replacing the import statement for `SplitText` with the import statement for `Split` and creating a new method `split` that uses the new `Split` class to split a string into an array of strings. The `Split` class takes a text and a separator as arguments and returns an iterable of strings, which is then converted to an array using the `asArray` method.