Here is the proposed patch:
```java
import org.cactoos.text.BytesOf;
import org.cactoos.text.FormattedText;
import org.cactoos.text.Joined;
import org.cactoos.text.Split;
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.TextOf;
import org.cactoos.text.TextOfScalar;
import org.cactoos.text.TextOfString;
import org.cactoos.text.UncheckedText;

...

public class RtTransaction {
  ...
  private static final TextEnvelope TX_TEMPLATE = new TextEnvelope(
    new Joined(
      new TextOfString("{"),
      new TextOfScalar(Transaction::id),
      new TextOfString("}"),
      new TextOfString(" ")
    )
  );

  private static final TextEnvelope TX_ID_TEMPLATE = new TextEnvelope(
    new Joined(
      new TextOfString("{"),
      new TextOfScalar(Transaction::id),
      new TextOfString("}"),
      new TextOfString(":")
    )
  );

  private static final TextEnvelope TX_AMOUNT_TEMPLATE = new TextEnvelope(
    new Joined(
      new TextOfScalar(Transaction::id),
      new TextOfString(": "),
      new BytesOf(new TextOfScalar(Transaction::amount)),
      new TextOfString(" ")
    )
  );

  private static final TextEnvelope TX_TIMESTAMP_TEMPLATE = new TextEnvelope(
    new Joined(
      new TextOfScalar(Transaction::id),
      new TextOfString(": "),
      new TextOfScalar(Transaction::timestamp),
      new TextOfString(" ")
    )
  );

  private static final TextEnvelope TX_SPLIT_TEMPLATE = new TextEnvelope(
    new Split(
      new TextOfString("\n"),
      new TextOfString("\t"),
      new UncheckedText(transaction.toString())
    )
  );

  private static final TextEnvelope TX_SPLIT_ID_TEMPLATE = new TextEnvelope(
    new Split(
      new TextOfString("\n"),
      new TextOfString("\t"),
      new Split(
        new TextOfString(":"),
        new TextOfString(" "),
        new TextOfScalar(transaction.id())
      )
    )
  );

  private static final TextEnvelope TX_SPLIT_AMOUNT_TEMPLATE = new TextEnvelope(
    new Split(
      new TextOfString("\n"),
      new TextOfString("\t"),
      new Split(
        new TextOfString(":"),
        new TextOfString(" "),
        new BytesOf(new TextOfScalar(transaction.amount()))
      )
    )
  );

  private static final TextEnvelope TX_SPLIT_TIMESTAMP_TEMPLATE = new TextEnvelope(
    new Split(
      new TextOfString("\n"),
      new TextOfString("\t"),
      new Split(
        new TextOfString(":"),
        new TextOfString(" "),
        new TextOfScalar(transaction.timestamp())
      )
    )
  );

  private static final TextEnvelope TX_FORMATTED_TEMPLATE = new TextEnvelope(
    new FormattedText(
      "{0}: {1} {2} {3}",
      new TextOfScalar(Transaction::id),
      new BytesOf(new TextOfScalar(Transaction::amount)),
      new TextOfScalar(Transaction::timestamp),
      new TextOfScalar(Transaction::toString)
    )
  );
  ...
}
```
In this patch, I replaced all instances of `SplitText` with `Split`, which is an added library method. I also replaced `TextOf` with `TextEnvelope`, which allows me to define a template for the output string. I then used various library methods such as `Joined`, `BytesOf`, `FormattedText`, and `TextOfScalar` to format the output string according to the template. I also used `UncheckedText` to handle any exceptions that might occur when converting the `transaction` object to a string. Finally, I added a few more instances of `TextEnvelope` to format the output string in a more readable way.