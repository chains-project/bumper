```java
import org.bouncycastle.jsse.BCSSLSocket;
import org.bouncycastle.tls.AlertDescription;

// ...

throw new BCSSLTransportException(AlertDescription.INTERNAL_ERROR);
```