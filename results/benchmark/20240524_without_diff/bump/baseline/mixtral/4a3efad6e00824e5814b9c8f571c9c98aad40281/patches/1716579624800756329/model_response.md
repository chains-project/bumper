Here's a possible patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PdfBoxUtils;
import eu.europa.esig.dss.pades.PdfSignatureParameters;
import eu.europa.esig.dss.pades.PdfSignerDoc;
import eu.europa.esig.dss.pades.token.PdfTokenConnection;
import eu.europa.esig.dss.signature.DocumentSignatureService;
import eu.europa.esig.dss.signature.InMemoryDocument;
import eu.europa.esig.dss.signature.SignatureValue;
import eu.europa.esig.dss.token.AbstractTokenConnection;
import eu.europa.esig.dss.token.SignatureTokenConnection;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Security;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.List;

// ...

public class Signer {

    // ...

    @Override
    protected void signPdf(InputStream inputStream, OutputStream outputStream, X509Certificate certificate, String password) throws Exception {
        Security.addProvider(new BouncyCastleProvider());

        // ...

        // Replace CertificationPermission with PadesCertificationLevel
        PadesCertificationLevel certificationLevel = PadesCertificationLevel.CERTIFY_MINOR_CHANGES;

        // ...

        // Replace CertificationPermission with PdfSignatureParameters
        PdfSignatureParameters parameters = new PdfSignatureParameters();
        parameters.setCertificationLevel(certificationLevel);
        parameters.setSigningCertificate(certificate);

        // ...

        // Replace CertificationPermission with PdfSigner
        PdfSigner pdfSigner = new PdfSigner(new PdfBoxUtils(), new PdfTokenConnection());

        // ...

        // Replace CertificationPermission with PdfSignerDoc
        PdfSignerDoc pdfSignerDoc = new PdfSignerDoc(pdfSigner, inputStream, outputStream);

        // ...

        // Replace CertificationPermission with DocumentSignatureService
        DocumentSignatureService<PdfSignerDoc, PdfSignatureParameters> documentSignatureService = new DocumentSignatureService<>(pdfSignerDoc);

        // ...

        // Replace CertificationPermission with SignatureValue
        SignatureValue signatureValue = documentSignatureService.signDocument(parameters, signatureTokenConnection);

        // ...
    }

    // ...
}
```

This patch replaces all occurrences of `CertificationPermission` with appropriate classes and interfaces from the updated library. It also adds the required import statements at the beginning of the file.