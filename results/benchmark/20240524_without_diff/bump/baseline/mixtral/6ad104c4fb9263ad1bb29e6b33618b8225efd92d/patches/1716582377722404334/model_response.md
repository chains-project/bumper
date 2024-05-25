Here's a potential patch for the failing client code:

```java
import org.bouncycastle.tls.crypto.TlsFatalAlert;
```

In this patch, we're simply changing the import statement to use the new package name for the `TlsFatalAlert` class. This should resolve the error message you're seeing.