```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

public class Signer {

    public void sign(byte[] data) {
        // ...
        CertificationPermission permission = PAdESSignatureParameters.getPermission();
        // ...
    }
}
```