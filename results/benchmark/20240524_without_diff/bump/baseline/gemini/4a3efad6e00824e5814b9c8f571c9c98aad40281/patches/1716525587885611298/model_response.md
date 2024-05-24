```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

public class Signer {

    public static void main(String[] args) {
        // Code to sign a PDF document
        PAdESSignatureParameters parameters = new PAdESSignatureParameters();
        parameters.setPermission(CertificationPermission.READ_ONLY);
        // ...
    }
}
```