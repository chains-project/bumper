I cannot determine the exact implementation of the `Signer` class and the method that is causing the issue. However, I can provide a sample code that demonstrates how you can use the new library method to fix the issue.

Assuming that the failing method is called `sign` and it uses `CertificationPermission` to set some permissions, you can modify the method as follows:
```java
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificate;
import eu.europa.esig.dss.pades.PadesSigningCertificateSource;
import eu.europa.esig.dss.pades.PadesSigningCertificateValidator;
import eu.europa.esig.dss.pades.PdfPadesSigner;
import eu.europa.esig.dss.pades.PdfSignatureParameters;
import eu.europa.esig.dss.pades.PdfSignaturePolicy;
import eu.europa.esig.dss.pades.validation.PdfPadesValidationService;
import eu.europa.esig.dss.pades.validation.PdfSignatureValidationContext;
import eu.europa.esig.dss.token.Pkcs12SignatureToken;
import eu.europa.esig.dss.validation.CommonValidationParameters;
import eu.europa.esig.dss.validation.Processable;
import eu.europa.esig.dss.validation.reports.Reports;
import eu.europa.esig.dss.validation.reports.SimpleReport;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateException;
import java.util.List;

public class Signer {

    private static final Logger LOG = LoggerFactory.getLogger(Signer.class);

    // ...

    @Override
    public File sign(File document, String certificateAlias, String password) throws Exception {
        KeyStore keyStore = KeyStore.getInstance("PKCS12");
        keyStore.load(new FileInputStream(certificateAlias), password.toCharArray());

        Pkcs12SignatureToken signatureToken = new Pkcs12SignatureToken(keyStore, password.toCharArray());
        signatureToken.setAlias(certificateAlias);

        PadesSigningCertificateSource certificateSource = new PadesSigningCertificateSource(signatureToken);
        PadesSigningCertificate signingCertificate = certificateSource.getSigningCertificate();

        CommonValidationParameters validationParams = new CommonValidationParameters();
        validationParams.setValidationProcessCritical(false);
        validationParams.setSignaturePolicyId(pdfSignaturePolicy);

        PdfSignaturePolicy pdfSignaturePolicy = new PdfSignaturePolicy(new File("policy.json"));

        PdfPadesSigningCertificateValidator certificateValidator = new PdfPadesSigningCertificateValidator(validationParams);
        certificateValidator.setTrustedServices(trustedServices);

        PadesSigningCertificateValidator.CertificateSource certificateSourceValidator = new PadesSigningCertificateValidator.CertificateSource() {
            @Override
            public List<PadesSigningCertificate> getCertificates() {
                return certificateSource.getCertificates();
            }
        };

        certificateValidator.setCertificateSource(certificateSourceValidator);

        PdfSignatureParameters parameters = new PdfSignatureParameters();
        parameters.setSigningCertificate(signingCertificate);
        parameters.setCertificateValidator(certificateValidator);
        parameters.setSignaturePolicy(pdfSignaturePolicy);

        PadesSigner signer = new PdfPadesSigner(signatureToken);
        signer.setSignaturePolicy(pdfSignaturePolicy);

        try (FileOutputStream output = new FileOutputStream(document)) {
            signer.sign(document, parameters);
        }

        // Validate the signed document
        PdfPadesValidationService validationService = new PdfPadesValidationService();
        PdfSignatureValidationContext validationContext = new PdfSignatureValidationContext();
        validationContext.setValidationProcessCritical(false);

        validationService.setTsaClient(tsaClient);

        Processable<SimpleReport> report = validationService.validateDocument(document, validationContext);
        Reports validationReports = report.get();

        // Check if the signature is valid
        if (validationReports.getSignaturesReports().get(0).isValid()) {
            LOG.info("The signature is valid.");
        } else {
            LOG.error("The signature is not valid.");
        }

        return document;
    }
}
```
In this example, I replaced the use of `CertificationPermission` with a new implementation that uses the `PadesSigningCertificate` class instead. I also added new imports for the new classes used in the code.

Note that this is just a sample code and you may need to modify it to fit your specific use case.