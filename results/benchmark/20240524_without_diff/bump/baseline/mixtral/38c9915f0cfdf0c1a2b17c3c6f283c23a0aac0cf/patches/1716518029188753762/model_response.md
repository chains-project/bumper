Here's a possible patch for the client code:
```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String hash, String data, UserApi userApi) {
  super(
    new TextEnvelope(
      new UncheckedText(data),
      new Trimmed(new TextOfScalar(userApi::currentUserId))
    ),
    hash
  );
}
```
The patch creates a `TextEnvelope` that wraps the `data` parameter and trims the current user ID from the user API. This way, the `TrimmedText` class is no longer used, so the failure should be resolved.