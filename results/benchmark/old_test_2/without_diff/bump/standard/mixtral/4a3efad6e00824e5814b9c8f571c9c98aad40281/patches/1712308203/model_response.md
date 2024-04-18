Here's a possible patch for the issue:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.pades.signature.SignatureImageParameters;
import eu.europa.esig.dss.pades.signature.TableSignatureFieldParameters;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;
import org.openpdfsign.Signer;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.security.KeyStore;
import java.security.cert.Certificate;
import java.security.cert.CertificateChain;
import java.util.HashMap;
import java.util.Map;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ...
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    // ...
    JKSSignatureToken signingToken = new JKSSignatureToken(keyStore, new KeyStore.PasswordProtection(keyStorePassword));
    // ...
    if (params.getUseTimestamp() || (!params.getTSA().isEmpty())) {
        // ...
    }
    // ...
    PAdESService service = new PAdESService(commonCertificateVerifier);
    // ...
    if (visibleSignature) {
        SignatureImageParameters imageParameters = new SignatureImageParameters();
        TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
        imageParameters.setFieldParameters(fieldParameters);
        // ...
        fieldParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
        // ...
        service.setPdfObjFactory(new PdfBoxNativeTableObjectFactory());
    }
    // ...
}
```

The patch imports the necessary classes and changes the `CertificationPermission` reference to `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED`. This assumes that the `Permission` enum is part of the `eu.europa.esig.dss.pades.PAdESSignatureParameters` class. If this is not the case, you may need to adjust the import statement accordingly.