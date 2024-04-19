Here's a fixed version of the method that should resolve the issue:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;
import eu.europa.esig.dss.pades.PadesSignatureService;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PdfBoxUtils;
import eu.europa.esig.dss.pades.PdfPublicKeyDataProvider;
import eu.europa.esig.dss.pades.validation.PdfDocumentValidator;
import eu.europa.esig.dss.pades.validation.PdfSignatureValidationContext;
import eu.europa.esig.dss.pades.validation.reports.PdfValidationReport;
import eu.europa.esig.dss.pades.validation.reports.Problems;
import eu.europa.esig.dss.pades.validation.reports.Rejection;
import eu.europa.esig.dss.pades.validation.reports.ValidationMessage;
import eu.europa.esig.dss.pades.validation.reports.ValidationResult;
import eu.europa.esig.dss.pades.validation.reports.ValidationSection;
import eu.europa.esig.dss.token.Pkcs12KeyStore;
import eu.europa.esig.dss.token.SignatureTokenConnection;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.CertificateVerifierProvider;
import eu.europa.esig.dss.validation.ProcessMode;
import eu.europa.esig.dss.validation.reports.Reports;
import eu.europa.esig.dss.validation.reports.SubFilter;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.Security;
import java.security.cert.CertificateException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.List;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.openpdfsign.Signer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class Signer {
    // ...
    
    @Override
    public void sign(File inputFile, File outputFile, String pin) throws Exception {
        // ...

        // Replace CertificationPermission with PadesCertificationLevel
        PadesCertificationLevel certificationLevel = PadesCertificationLevel.CERTIFY_MINOR_CHANGES;

        // ...

        // Replace CertificationPermission with PadesCertificationLevel
        PadesSigner signer = new PadesSigner(signingCertificateSource, pkcs12KeyStore, certificationLevel);

        // ...
    }
}
```

In this patch, I replaced `CertificationPermission` with `PadesCertificationLevel` and set it to `CERTIFY_MINOR_CHANGES`. This should resolve the issue with the missing symbol.