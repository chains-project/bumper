Here's a proposed patch for the code, taking into account the new library version changes:
```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.pades.signature.SignatureImageParameters;
import eu.europa.esig.dss.pades.signature.TableSignatureFieldParameters;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;
import org.openpdfsign.dss.SignatureToken;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyStore;
import java.security.KeyStore.PasswordProtection;
import java.security.cert.Certificate;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ...
    // load certificate and private key
    SignatureToken signingToken = new SignatureToken(keyStore, new PasswordProtection(keyStorePassword));
    // ...
    // PAdES parameters
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    // ...
    // Create common certificate verifier
    CommonCertificateVerifier commonCertificateVerifier = new CommonCertificateVerifier();
    // Create PAdESService for signature
    PAdESService service = new PAdESService(commonCertificateVerifier);
    // ...
    // Initialize visual signature and configure
    if (visibleSignature) {
        SignatureImageParameters imageParameters = new SignatureImageParameters();
        TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
        imageParameters.setFieldParameters(fieldParameters);
        // ...
        if (!Strings.isStringEmpty(params.getImageFile())) {
            imageParameters.setImage(new InMemoryDocument(Files.readAllBytes(Paths.get(params.getImageFile()))));
        } else {
            imageParameters.setImage(new InMemoryDocument(IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("signature.png"))));
        }
        // ...
        fieldParameters.setPermission(Permission.MINIMAL_CHANGES_PERMITTED);
        // ...
        signatureParameters.setImageParameters(imageParameters);
        PdfBoxNativeTableObjectFactory pdfBoxNativeObjectFactory = new PdfBoxNativeTableObjectFactory();
        service.setPdfObjFactory(pdfBoxNativeObjectFactory);
        // ...
    }
    // ...
}

static class SignatureToken extends JKSSignatureToken {
    public SignatureToken(byte[] keyStoreData, PasswordProtection password) {
        super(keyStoreData, password);
    }

    public Certificate getCertificate(String alias) {
        return getKeys().get(0).getCertificate();
    }

    public Certificate[] getCertificateChain(String alias) {
        return getKeys().get(0).getCertificateChain();
    }

    public Key getKey(String alias) {
        return getKeys().get(0).getPrivateKey();
    }
}
```
The changes include:

- Importing the necessary classes for the new library version
- Creating a `SignatureToken` class that extends `JKSSignatureToken` to handle the certificate and private key
- Replacing `CertificationPermission` with `Permission`
- Replacing `eu.europa.esig.dss.enumerations` with the appropriate imports (e.g., `eu.europa.esig.dss.pades.PAdESSignatureParameters`)
- Removing unnecessary imports