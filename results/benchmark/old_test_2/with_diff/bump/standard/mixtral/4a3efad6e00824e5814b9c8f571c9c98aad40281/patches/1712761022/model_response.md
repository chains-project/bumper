Here's the updated code with the required changes:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.openpdfsign.pdfbox.PdfBoxNativeTableObjectFactory;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyStore;
import java.security.cert.Certificate;
import java.security.cert.CertificateChain;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ...
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    // ...
    signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
    // ...
    PAdESService service = new PAdESService(commonCertificateVerifier);
    // ...
    if (visibleSignature) {
        // ...
        signatureParameters.setImageParameters(imageParameters);
        PdfBoxNativeObjectFactory pdfBoxNativeObjectFactory = new PdfBoxNativeTableObjectFactory();
        service.setPdfObjFactory(pdfBoxNativeObjectFactory);
    }
    // ...
}
```

The changes include importing the required classes and using the fully qualified names for `CertificationPermission`, which has been replaced by `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED` in the updated library. Also, the import for `org.openpdfsign.pdfbox.PdfBoxNativeTableObjectFactory` is added.