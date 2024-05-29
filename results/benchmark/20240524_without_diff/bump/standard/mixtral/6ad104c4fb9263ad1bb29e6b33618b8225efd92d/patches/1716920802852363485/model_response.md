Here's a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// Add the following import statement
import org.bouncycastle.crypto.tls.impl.TlsUtils;

// Replace the line that causes the error with the following code
TlsUtils.checkVersion(peerVersion, TlsConstants.VERSION_1_2);
```
This patch imports the `TlsUtils` class from the `org.bouncycastle.crypto.tls.impl` package and uses its `checkVersion` method instead of the `TlsFatalAlert` constructor to check the peer version. The `TlsUtils` class is available in the same library version as `TlsFatalAlert`, so it should not introduce any new dependencies.