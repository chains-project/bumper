Here's a possible patch for the failing client code:

```java
import eu.europa.esig.dss.pades.PadesCertificationLevel;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PadesSigningCertificateValidator;
import eu.europa.esig.dss.pades.PadesSignerOptions;
import eu.europa.esig.dss.pades.PadesUtils;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.DSSException;
import eu.europa.esig.dss.model.InMemoryDocument;
import eu.europa.esig.dss.token.DSSPrivateKeyEntry;
import eu.europa.esig.dss.token.Pkcs11Token;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.CertificateVerifier;
import eu.europa.esig.dss.validation.SignedDocumentValidator;
import org.openpdf.sign.PDFSignature;
import org.openpdf.sign.PDFSigner;

// ...

@Override
public void signPdf(InputStream inputStream, OutputStream outputStream,
                     String certificatePath, String privateKeyPath, String password) throws Exception {
    // ...

    // Use PadesSigner instead of CertificationPermission
    PadesSignerOptions options = new PadesSignerOptions();
    options.setCertificationLevel(PadesCertificationLevel.ESH_OVER_ESH);
    options.setSigningCertificateSource(new PadesSigningCertificateSource(certificate));
    options.setSigningCertificateValidator(new PadesSigningCertificateValidator(new CommonCertificateVerifier()));
    options.setTspSource(tspSource);

    DSSDocument dssDocument = new InMemoryDocument(inputStream);
    DSSPrivateKeyEntry privateKeyEntry = new DSSPrivateKeyEntry(privateKey);
    Pkcs11Token pkcs11Token = new Pkcs11Token(pkcs11Config);
    pkcs11Token.setPrivateKeyEntry(privateKeyEntry);
    pkcs11Token.setAlias(privateKeyAlias);
    pkcs11Token.setPassword(password);

    PadesSigner signer = new PadesSigner(dssDocument, pkcs11Token, pkcs11Token.getPrivateKeyEntry(), options);
    signer.setSignedDocumentValidator(new SignedDocumentValidator(new CommonCertificateVerifier()));

    // Use PadesUtils.signDocument instead of PDFSignature.signDetached()
    DSSDocument signedDocument = PadesUtils.signDocument(signer);
    OutputStream signedOutputStream = new FileOutputStream(outputFile);
    signedDocument.writeTo(signedOutputStream);

    // ...
}
```

This patch replaces the `CertificationPermission` import with the necessary imports for `PadesSigner` and related classes. It also replaces the `PDFSignature.signDetached()` method with `PadesUtils.signDocument()` and updates the method calls accordingly. Note that this patch assumes that the necessary dependencies for the `eu.europa.esig.dss` library have been added to the project.