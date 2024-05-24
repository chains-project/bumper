Here's a possible patch for the client code:
```java
import org.cactoos.text.UncheckedText;

// ...

import static org.cactoos.Text.isEmpty;

// ...

@Override
public Transaction fromJson(final JsonElement json) throws IOException {
  requireNonNull(json, "JSON element can't be null");
  requireTrue(json.isJsonObject(), "JSON element must be an object");
  requireTrue(json.getAsJsonObject().has("id"), "JSON element must have 'id' field");
  requireTrue(json.getAsJsonObject().has("type"), "JSON element must have 'type' field");
  requireTrue(json.getAsJsonObject().has("amount"), "JSON element must have 'amount' field");
  requireTrue(json.getAsJsonObject().has("time"), "JSON element must have 'time' field");
  requireTrue(json.getAsJsonObject().has("owner"), "JSON element must have 'owner' field");
  requireTrue(json.getAsJsonObject().has("spender"), "JSON element must have 'spender' field");
  requireTrue(json.getAsJsonObject().has("status"), "JSON element must have 'status' field");
  final String id = getString(json, "id");
  final String type = getString(json, "type");
  final BigDecimal amount = getDecimal(json, "amount");
  final Instant time = getInstant(json, "time");
  final String owner = getString(json, "owner");
  final String spender = getString(json, "spender");
  final TransactionStatus status = TransactionStatus.valueOf(getString(json, "status"));
  return new Transaction(
      id,
      type,
      amount,
      time,
      owner,
      spender,
      status,
      new UncheckedText(getString(json, "data"))
  );
}
```
The patch replaces the usage of `TrimmedText` with `UncheckedText`, which is a new class in the updated library version. It also adds a static import for `isEmpty` to make the code more concise.

Note that the `Transaction` constructor has also changed in the updated library version, so the patch also reflects those changes. Specifically, the `data` field is now expected to be a `CharSequence` instead of a `String`, so the `UncheckedText` constructor is used instead of the `TrimmedText` constructor.