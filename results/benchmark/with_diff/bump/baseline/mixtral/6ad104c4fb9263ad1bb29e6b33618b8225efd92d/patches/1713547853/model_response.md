Sure, here's a patch for the failing code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public AlertDescription getAlertDescription(short alert) {
    return new TlsFatalAlert(alert).getAlertDescription();
}
```
In the new version of the library, the `getAlertDescription()` method is no longer a public method of the `TlsFatalAlert` class, but instead, it's a method of the `TlsFatalAlert` constructor. Therefore, we need to create a new `TlsFatalAlert` object and call the `getAlertDescription()` method on it.

Note that I had to make a couple of assumptions here, since I don't have the full context of your codebase. Specifically, I assumed that the `getAlertDescription()` method is supposed to take a `short` parameter and return an `AlertDescription` object, based on the error message you provided. If this assumption is incorrect, you may need to adjust the code accordingly.