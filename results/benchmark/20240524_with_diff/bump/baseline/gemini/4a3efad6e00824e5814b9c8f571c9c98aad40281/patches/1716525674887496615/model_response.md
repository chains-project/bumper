```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

import java.util.List;

public class Signer {
    public void checkDocumentPermissions(PdfDocumentReader pdfDocumentReader) {
        CertificationPermission docMDP = pdfDocumentReader.getCertificationPermission();
        if (docMDP != null) {
            // Check if the document MDP is compatible with the signature policy
        }
        List<SigFieldPermissions> fieldMDPs = pdfDocumentReader.getFieldMDPs();
        for (SigFieldPermissions fieldMDP : fieldMDPs) {
            CertificationPermission fieldCertificationPermission = fieldMDP.getCertificationPermission();
            if (fieldCertificationPermission != null) {
                // Check if the field MDP is compatible with the signature policy
            }
        }
    }
}
```