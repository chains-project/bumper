Here's a patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PdfBoxUtils;
import eu.europa.esig.dss.model.InMemoryDocument;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.DSSPrivateKeyEntry;
import eu.europa.esig.dss.model.x509.CertificateToken;
import eu.europa.esig.dss.spi.x509.CertificateSource;
import eu.europa.esig.dss.spi.x509.CertificateVerifier;
import eu.europa.esig.dss.spi.x509.CryptoProviderTools;
import eu.europa.esig.dss.token.CryptoToken;
import eu.europa.esig.dss.token.Pkcs11Token;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.Security;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Signer {

    private static final Logger LOG = LoggerFactory.getLogger(Signer.class);

    public void signPdf(String inputFilePath, String outputFilePath,
                        String keyStoreFilePath, String keyStorePassword,
                        String certificateAlias) throws Exception {
        Security.addProvider(new BouncyCastleProvider());

        KeyStore keyStore = KeyStore.getInstance("PKCS12");
        keyStore.load(new FileInputStream(keyStoreFilePath), keyStorePassword.toCharArray());

        PrivateKey privateKey = (PrivateKey) keyStore.getKey(certificateAlias, keyStorePassword.toCharArray());
        Certificate certificate = keyStore.getCertificate(certificateAlias);

        CertificateSource certificateSource = new SimpleCertificateSource(certificate);
        CertificateVerifier certificateVerifier = new CommonCertificateVerifier();

        CryptoToken cryptoToken = new Pkcs11Token(certificateSource, certificateVerifier);

        List<String> signingCertificates = new ArrayList<>();
        signingCertificates.add(certificate.getSubjectX500Principal().getName());

        DSSDocument dssDocument = new InMemoryDocument(new File(inputFilePath));

        PadesSigner signer = new PadesSigner(cryptoToken, certificateSource, certificateVerifier);
        signer.setSigningCertificate(certificate);
        signer.setSigningCertificateChain(certificateSource.getCertificates(certificate));
        signer.setCertificationLevel(PadesCertificationLevel.CERTIFIED_NO_CHANGES_ALLOWED);

        File outputFile = new File(outputFilePath);
        try (FileOutputStream outputStream = new FileOutputStream(outputFile)) {
            signer.sign(dssDocument, signingCertificates, outputStream);
        }
    }
}
```

This patch replaces the failing import statement and uses the `PadesSigner` class from the updated library version to sign the PDF document. The `CertificationPermission` class has been removed, so the `PadesCertificationLevel` enum is used to set the certification level.