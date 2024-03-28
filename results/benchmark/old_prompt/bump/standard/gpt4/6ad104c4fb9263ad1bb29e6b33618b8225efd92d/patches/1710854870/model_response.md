The error message indicates that the package `org.bouncycastle.crypto.tls` does not exist. It seems like an external dependency issue. The `TlsFatalAlert` class might have been moved to a different package in a newer version of the library. 

You should try replacing the import statement with the correct one. If the `TlsFatalAlert` class was moved to `org.bouncycastle.tls` package, the import statement should be:

```java
import org.bouncycastle.tls.TlsFatalAlert;
```