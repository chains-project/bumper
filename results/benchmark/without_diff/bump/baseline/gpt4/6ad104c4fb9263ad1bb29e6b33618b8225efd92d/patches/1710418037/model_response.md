It seems like the package `org.bouncycastle.crypto.tls` does not exist anymore. This might be due to a change in the version of the BouncyCastle library. 

The TlsFatalAlert class was moved to a different package in the new version of the BouncyCastle library. You should update the import statement to the new package:

```java
import org.bouncycastle.tls.TlsFatalAlert;
```