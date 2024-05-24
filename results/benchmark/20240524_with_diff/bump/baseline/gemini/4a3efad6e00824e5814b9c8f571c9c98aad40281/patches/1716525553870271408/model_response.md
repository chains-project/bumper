```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

import eu.europa.esig.dss.pades.PAdESSignatureParameters;

public class Signer {

    public void sign(PAdESSignatureParameters parameters) {
        // ...
        parameters.setPermission(CertificationPermission.READ_ONLY);
        // ...
    }
}
```