Here's the proposed patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PadesSignService;
import eu.europa.esig.dss.pades.PadesSigner.Pkcs12FileCarrier;
import eu.europa.esig.dss.pades.PadesSigner.TsMode;
import eu.europa.esig.dss.pades.validation.PdfDocumentValidator;
import eu.europa.esig.dss.pades.validation.PdfSignatureValidationContext;
import eu.europa.esig.dss.pades.validation.reports.PdfValidationReport;
import eu.europa.esig.dss.token.Pkcs12SignatureToken;
import eu.europa.esig.dss.token.SignatureTokenConnection;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.CertificateVerifierProvider;
import eu.europa.esig.dss.validation.ProcessCertificateSource;
import eu.europa.esig.dss.validation.reports.Reports;
import eu.europa.esig.dss.validation.reports.SimpleReport;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateException;
import java.util.List;
import org.openpdfsign.Signer;

// ...

public class Signer {

    // ...

    public void sign(File inputFile, File outputFile, String alias, String password) throws Exception {
        // ...

        // Replace CertificationPermission with PadesCertificationLevel
        PadesCertificationLevel certificationLevel = PadesCertificationLevel.CERTIFY_MINOR_CHANGES;

        // ...

        // Create a new PadesSigner instance
        PadesSigner padesSigner = new PadesSigner(certificationLevel);

        // ...
    }

    // ...
}
```

This patch replaces the `CertificationPermission` import with the correct one and updates the related code accordingly. It also imports the necessary classes for the `PadesSigner` initialization.