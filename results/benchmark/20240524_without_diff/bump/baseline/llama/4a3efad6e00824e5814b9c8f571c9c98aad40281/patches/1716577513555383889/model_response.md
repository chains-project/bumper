```java
import java.security.cert.Certificate;
import java.security.cert.CertPath;
import java.security.cert.CertPathValidator;
import java.security.cert.CertPathValidatorException;
import java.security.cert.PKIXParameters;
import java.security.cert.TrustAnchor;

// ...

CertPathValidator validator = CertPathValidator.getInstance("PKIX");
PKIXParameters params = new PKIXParameters(Collections.singleton(new TrustAnchor((Certificate)null, null)));
params.setRevocationEnabled(false);
CertPath certPath = CertPath.getInstance("PKIX");
validator.validate(certPath, params);
```