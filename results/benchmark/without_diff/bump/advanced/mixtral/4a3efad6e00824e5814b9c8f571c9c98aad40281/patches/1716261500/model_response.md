Here's the proposed patch for the given client code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.PAdESService;
import eu.europa.esig.dss.pades.SignatureImageParameters;
import eu.europa.esig.dss.pades.signature.PAdESSignatureService;
import eu.europa.esig.dss.pdf.PDFDocument;
import eu.europa.esig.dss.pdf.PDFSignature;
import eu.europa.esig.dss.pdf.PdfDssDictionary;
import eu.europa.esig.dss.pdf.PdfSignatureParameters;
import eu.europa.esig.dss.pdf.PdfSignerData;
import eu.europa.esig.dss.pdf.PDFFieldsData;
import eu.europa.esig.dss.pdf.PdfUtils;
import eu.europa.esig.dss.pades.PAdESSignatureParameters.Builder;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.enumerations.DigestAlgorithm;
import eu.europa.esig.dss.enumerations.SignatureLevel;
import eu.europa.esig.dss.enumerations.CertificateRefDigestAlgorithm;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.InMemoryDocument;
import eu.europa.esig.dss.model.ToBeSigned;
import eu.europa.esig.dss.model.x509.CertificateToken;
import eu.europa.esig.dss.spi.x509.tsp.CompositeTSPSource;
import eu.europa.esig.dss.spi.x509.tsp.TSPSource;
import eu.europa.esig.dss.spi.x509.tsp.OnlineTSPSource;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.openpdfsign.Signer;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    // load PDF file
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    // load certificate and private key
    JKSSignatureToken signingToken = new JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    // PAdES parameters
    Builder signatureParametersBuilder = new PAdESSignatureParameters.Builder(CertificateRefDigestAlgorithm.SHA256);
    if (params.getUseTimestamp() || (!params.getTSA().isEmpty())) {
        signatureParametersBuilder.setSignatureLevel(SignatureLevel.PAdES_BASELINE_T);
    } else {
        signatureParametersBuilder.setSignatureLevel(SignatureLevel.PAdES_BASELINE_B);
    }
    signatureParametersBuilder.setSigningCertificate(signingToken.getKey(0).getCertificate());
    signatureParametersBuilder.setCertificateChain(signingToken.getKey(0).getCertificateChain());
    PAdESSignatureParameters signatureParameters = signatureParametersBuilder.build();
    // Create common certificate verifier
    CommonCertificateVerifier commonCertificateVerifier = new CommonCertificateVerifier();
    // Create PAdESService for signature
    PAdESService service = new PAdESService(commonCertificateVerifier);
    // Initialize visual signature and configure
    if (visibleSignature) {
        SignatureImageParameters imageParameters = new SignatureImageParameters();
        PDFFieldsData fieldParameters = new PDFFieldsData();
        imageParameters.setFieldParameters(fieldParameters);
        // ...
        fieldParameters.setSignaturString(signingToken.getKey(0).getCertificate().getSubject().getPrettyPrintRFC2253());
        // ...
        signatureParameters.setImageParameters(imageParameters);
        PdfBoxNativeObjectFactory pdfBoxNativeObjectFactory = new PdfBoxNativeTableObjectFactory();
        service.setPdfObjFactory(pdfBoxNativeObjectFactory);
    }
    // ...
}
```

I have replaced the `CertificationPermission` with the `CertificateRefDigestAlgorithm`. Also, I have imported and used the required classes explicitly for better readability and to avoid potential conflicts.