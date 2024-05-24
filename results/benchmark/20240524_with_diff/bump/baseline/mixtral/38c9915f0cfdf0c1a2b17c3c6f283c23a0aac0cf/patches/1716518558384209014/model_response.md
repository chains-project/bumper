Here's a possible patch for the client code:
```java
import org.cactoos.text.UncheckedText;

// ...

import static org.cactoos.Text.asString;

// ...

public RtTransaction(String id, String hash, Timestamp timestamp,
    TransactionType type, Money value, Money fee, Money total,
    User from, User to, String comment, String[] tags) throws IOException {
  this.id = new UncheckedText(id);
  this.hash = new UncheckedText(hash);
  this.timestamp = timestamp;
  this.type = type;
  this.value = value;
  this.fee = fee;
  this.total = total;
  this.from = from;
  this.to = to;
  this.comment = new UncheckedText(comment != null ? comment : "");
  this.tags = tags != null ? asString(tags) : "";
  // ...
}
```
In this patch, I replaced the usage of `SplitText` with `UncheckedText` and `asString` method, which are new classes/methods in the updated library version. Also, I added a null check for the `comment` parameter and initialized it with an empty string if it's null, to avoid a possible `NullPointerException`.