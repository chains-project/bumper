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
PKIXParameters params = new PKIXParameters(new HashSet<TrustAnchor>(Arrays.asList(trustAnchors)));
params.setRevocationEnabled(false);
CertPath certPath = CertPath.getInstance("X.509", new ByteArrayInputStream(certBytes));
try {
    validator.validate(certPath, params);
} catch (CertPathValidatorException e) {
    // handle exception
}
```