```java
import java.security.cert.Certificate;
import java.security.cert.CertPath;
import java.security.cert.CertPathValidatorException;
import java.security.cert.PKIXParameters;

// ...

CertPath cp = null;
PKIXParameters params = null;
try {
    cp = cf.generateCertPath(list);
    params = new PKIXParameters(Collections.singleton(trustAnchor));
    params.setRevocationEnabled(false);
    CertPathValidator validator = CertPathValidator.getInstance("PKIX");
    validator.validate(cp, params);
} catch (CertPathValidatorException e) {
    // handle exception
}
```