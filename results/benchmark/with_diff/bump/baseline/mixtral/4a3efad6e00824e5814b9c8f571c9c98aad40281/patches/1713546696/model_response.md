Here's the proposed patch for the failing client code:
```java
import eu.europa.esig.dss.pades.PadesSigningCertificate;
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PdfBoxUtils;
import eu.europa.esig.dss.pades.SignaturePolicy;
import eu.europa.esig.dss.pades.SignaturePolicySource;
import eu.europa.esig.dss.pades.PdfBoxCryptoDocument;
import eu.europa.esig.dss.pades.PdfBoxCrypto;
import eu.europa.esig.dss.enveloped.EnvelopedDataBuilder;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.InMemoryDocument;
import eu.europa.esig.dss.model.ToBeSigned;
import eu.europa.esig.dss.token.DSSPrivateKeyEntry;
import eu.europa.esig.dss.token.DSSPrivateKeySource;
import eu.europa.esig.dss.token.DSSPublicKeySource;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.policy.SignaturePolicyFactory;
import org.bouncycastle.cms.CMSProcessableByteArray;
import org.bouncycastle.cms.CMSProcessableInputStream;
import org.bouncycastle.cms.CMSSignedData;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.tsp.TSPException;

// ...

public class Signer {

    // ...

    @Override
    public DSSDocument sign(InputStream inputStream,
                              String certificateAlias,
                              String pin,
                              String signaturePolicyIdentifier,
                              String signatureName,
                              boolean includeCertificate,
                              boolean includeCadesMode,
                              boolean includeTsaToken,
                              String tsaUrl) throws Exception {

        // ...

        // Replace CertificationPermission with PadesSigningCertificate
        PadesSigningCertificate signingCertificate = new PadesSigningCertificate(certificate);

        // ...

        // Replace CertificationPermission with PadesSigner
        PadesSigner padesSigner = new PadesSigner(signingCertificate, signingCertificate);

        // ...

    }

    // ...

}
```
The changes include importing new classes and replacing `CertificationPermission` with `PadesSigningCertificate` and `PadesSigner`.