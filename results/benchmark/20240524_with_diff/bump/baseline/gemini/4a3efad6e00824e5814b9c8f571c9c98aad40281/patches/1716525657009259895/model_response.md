```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

public class Signer {

    public void sign(byte[] document) {
        // ...
        PAdESSignatureParameters parameters = new PAdESSignatureParameters();
        parameters.setPermission(CertificationPermission.SIGNING);
        // ...
    }
}
```