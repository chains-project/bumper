```java
import java.security.cert.Certificate;
import java.security.cert.CertPath;
import java.security.cert.CertPathValidator;
import java.security.cert.CertPathValidatorException;
import java.security.cert.PKIXParameters;
import java.security.cert.TrustAnchor;
import java.util.HashSet;
import java.util.Set;

CertPathValidator validator = CertPathValidator.getInstance("PKIX");
PKIXParameters params = new PKIXParameters(Collections.singleton(new TrustAnchor((X509Certificate)null, null)));
params.setRevocationEnabled(false);

CertPath certPath = CertPath.getInstance("X.509");
certPath.addCertificate(new X509Certificate());

try {
    validator.validate(certPath, params);
} catch (CertPathValidatorException e) {
    // handle exception
}
```