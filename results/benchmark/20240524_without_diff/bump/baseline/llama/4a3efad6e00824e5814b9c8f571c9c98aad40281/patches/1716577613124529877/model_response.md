```java
import java.security.cert.CertPath;
import java.security.cert.Certificate;
import java.security.cert.CertificateFactory;

// ...

CertPath certPath = CertificateFactory.getInstance("X.509").generateCertPath(certificateChain);
```