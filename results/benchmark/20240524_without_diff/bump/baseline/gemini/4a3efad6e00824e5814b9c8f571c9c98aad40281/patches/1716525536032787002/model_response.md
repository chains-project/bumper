```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

import eu.europa.esig.dss.pades.PAdESSignatureParameters;

public class Signer {

    public void sign(byte[] document, PAdESSignatureParameters parameters) {
        CertificationPermission permission = parameters.getPermission();
        // ...
    }
}
```