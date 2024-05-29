Here's the patched code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;

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
import java.util.HashMap;
import java.util.Map;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ... (keep your existing code here)

    // Change this line:
    // signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);

    // To this:
    signatureParameters.setPermission(new eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.Visibility.NOT_VISIBLE, eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.Modification.MINOR_CHANGES_PERMITTED));

    // ... (keep your existing code here)
}
```

The change is in the `signatureParameters.setPermission` line. I replaced `CertificationPermission` with `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission` and provided the required parameters for the permission. This should fix the compilation error.