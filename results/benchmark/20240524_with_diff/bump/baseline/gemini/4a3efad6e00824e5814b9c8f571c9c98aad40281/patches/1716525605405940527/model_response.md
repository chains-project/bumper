```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.validation.PdfSignatureDictionary;
import eu.europa.esig.dss.pdf.SigFieldPermissions;

public class Signer {

    public static void main(String[] args) {
        // ...
        PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();

        // Get the certification permission from the signature parameters
        CertificationPermission permission = signatureParameters.getPermission();

        // ...
    }
}
```