Here's a patch that you can apply to the `Signer.java` file to fix the error:

```java
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificate;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PadesSigningLevel;
import eu.europa.esig.dss.pades.PadesSignaturePolicy;
import eu.europa.esig.dss.pades.PadesSigningService;
import eu.europa.esig.dss.pades.PadesSignatureParameters;
import eu.europa.esig.dss.pades.PadesSigner.Pkcs12FileCarrier;
import eu.europa.esig.dss.pades.PadesSigner.Pkcs12FileCarrier.Builder;
import eu.europa.esig.dss.pades.PadesSigner.CertificateSourceFunction;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.DSSPrivateKey;
import eu.europa.esig.dss.model.DSSPublicKey;
import eu.europa.esig.dss.model.InMemoryDocument;
import eu.europa.esig.dss.model.ToBeSigned;
import eu.europa.esig.dss.model.x509.CertificateToken;
import eu.europa.esig.dss.token.Pkcs12KeyStore;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.CertificateVerifier;
import eu.europa.esig.dss.validation.SignedDocumentValidator;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.Security;
import java.security.cert.CertificateException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

// ...

private ToBeSigned signDocument(File fileToSign, String certificatePassword, String outputFilePath, String signatureLevel, String signaturePolicy, String reason, String location) throws Exception {
    // ...
    PadesSigningLevel signingLevel = PadesSigningLevel.valueOf(signatureLevel.toUpperCase());
    PadesSignaturePolicy signaturePolicyObj = new PadesSignaturePolicy(new File(signaturePolicy));
    // CertificationPermission certificationPermission = CertificationPermission.SIGNATURE_AND_DATA_ACCESS;
    PadesSigningCertificateSource certificateSource = new PadesSigningCertificateSource() {
        @Override
        public CertificateToken getCertificateToken() {
            // ...
        }

        @Override
        public DSSPublicKey getPublicKey() {
            // ...
        }
    };

    PadesSigningService signingService = new PadesSigningService(certificateVerifier);
    PadesSigner signer = new PadesSigner(signingService);
    PadesSignatureParameters signatureParameters = new PadesSignatureParameters();
    signatureParameters.setSigningCertificate(certificateSource);
    signatureParameters.setSignaturePolicy(signaturePolicyObj);
    signatureParameters.setSigningLevel(signingLevel);
    signatureParameters.setReason(reason);
    signatureParameters.setLocation(location);
    signatureParameters.setIncludeCertificate(true);
    signatureParameters.setIncludeCrls(true);
    signatureParameters.setIncludeOcsp(true);

    // ...
}

// ...
```

The patch removes the `CertificationPermission` import and usage, as it has been removed from the library. Instead, the patch adds a custom `PadesSigningCertificateSource` implementation to set the `signingCertificate` in the `PadesSignatureParameters`.

This change should fix the compilation error and allow you to sign documents using the new library version.