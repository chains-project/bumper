Here is the updated code with the necessary changes:

```java
import eu.europa.esig.dss.certificate.CertificateToken;
import eu.europa.esig.dossier.validation.CAdESParameter;
import org.openpdf.Signer;

//...

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    // ...
    // PAdES parameters
    eu.europa.esig.dss.pades.PAdESParameter param = new eu.europa.esign.dss.pades.PAdESParameter();
    // ...
    param.setCertificationLevel(eu.europa.esign.dss.pades.PAdESParameter.CERTIFICATION_MINIMAL_PERMITTED);
    // ...
    // Create PAdESService for signature
    eu.europa.esign.dss.pades.signature.PAdESService service = new eu.europa.esign.dss.pades.signature.PAdESService();
    // ...
    // Get the SignedInfo segment that need to be signed.
    // ...
    if (visibleSignature) {
        // ...
        // Use the new parameter for certification level
        param.setCertificationLevel(eu.europa.esign.dss.pades.PAdESParameter.CERTIFCertificateToken.CERTIFICATION_MINIMAL_PERMITTED);
        // ...
    }
    // ...
}
```

In the updated code, I replaced `eu.europa.esig.dss.certificate.CertificationPermission` with `eu.europa.esig.dss.pades.PAdESParameter.CERTIFICATION_MINIMAL_PERMITTED` and changed the import statement accordingly.

Note that I couldn'
```