```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

public class Signer {

    public void sign(String filePath) {
        // ...
        PAdESSignatureParameters parameters = new PAdESSignatureParameters();
        parameters.setPermission(CertificationPermission.READ_ONLY);
        // ...
    }
}
```