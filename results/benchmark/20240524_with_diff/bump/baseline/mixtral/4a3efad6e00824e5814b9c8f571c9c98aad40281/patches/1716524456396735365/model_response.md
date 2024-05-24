Here's the proposed patch:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

import eu.europa.esig.dss.pdf.PdfDocumentReader;
import eu.europa.esig.dss.pdf.SigFieldPermissions;

// ...

public class Signer {

    // ...

    private void checkDocumentPermissions(DSSDocument document) {
        PdfDocumentReader pdfDocumentReader = new PdfDocumentReader(document);
        pdfDocumentReader.checkDocumentPermissions();
        CertificationPermission permission = pdfDocumentReader.getCertificationPermission();
        // ...
    }

    // ...

}
```

The patch modifies the `checkDocumentPermissions` method to use the new `PdfDocumentReader` class and its methods to get the certification permission.