```java
import java.security.cert.Certificate;
import java.security.cert.CertificateFactory;

// ...

CertificationPermission permission = null;
try {
    CertificateFactory factory = CertificateFactory.getInstance("X.509");
    Certificate cert = factory.generateCertificate(new ByteArrayInputStream(certBytes));
    permission = new CertificationPermission(cert);
} catch (CertificateException e) {
    // handle exception
}
```