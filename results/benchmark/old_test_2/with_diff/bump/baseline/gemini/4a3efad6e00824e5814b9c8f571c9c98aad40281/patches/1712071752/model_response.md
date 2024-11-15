```java
import eu.europa.esig.dss.pades.CertificationPermission;
import eu.europa.esig.dss.pades.PAdESService;
import eu.europa.esig.dss.token.AbstractSignatureTokenConnection;
import eu.europa.esig.dss.token.DSSPrivateKeyEntry;
import eu.europa.esig.dss.token.DocumentTokenConnection;
import eu.europa.esig.dss.token.PasswordInputCallback;
import eu.europa.esig.dss.token.Pkcs12SignatureToken;
import eu.europa.esig.dss.token.SignatureTokenConnection;
import eu.europa.esig.dss.validation.SignedDocumentValidator;
import eu.europa.esig.dss.validation.reports.Reports;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.UnrecoverableEntryException;
import java.security.cert.CertificateException;
import java.util.Base64;
import java.util.Collections;
import java.util.List;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.interactive.digitalsignature.PDSignature;
import org.apache.pdfbox.pdmodel.interactive.digitalsignature.PDSignatureAppearance;
import org.apache.pdfbox.pdmodel.interactive.digitalsignature.PDSignatureField;
import org.bouncycastle.cert.X509CertificateHolder;
import org.bouncycastle.cms.CMSException;
import org.bouncycastle.cms.CMSSignedData;
import org.bouncycastle.cms.SignerInformation;
import org.bouncycastle.cms.SignerInformationStore;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.operator.ContentSigner;
import org.bouncycastle.operator.OperatorCreationException;
import org.bouncycastle.operator.jcajce.JcaContentSignerBuilder;
import org.bouncycastle.util.Store;

public class Signer {

  private static final String KEY_STORE_TYPE = "PKCS12";
  private static final String SIGNATURE_ALGORITHM = "SHA256withRSA";

  public static void main(String[] args) throws Exception {
    // Load the key store
    KeyStore keyStore = KeyStore.getInstance(KEY_STORE_TYPE);
    keyStore.load(new FileInputStream("my-keystore.p12"), "password".toCharArray());

    // Get the private key entry
    KeyStore.PrivateKeyEntry privateKeyEntry = (KeyStore.PrivateKeyEntry) keyStore.getEntry("my-alias", new KeyStore.PasswordProtection("password".toCharArray()));

    // Create the signature token
    SignatureTokenConnection signatureTokenConnection = new Pkcs12SignatureToken(keyStore, privateKeyEntry.getPrivateKey(), "password".toCharArray());

    // Create the document token
    DocumentTokenConnection documentTokenConnection = new DocumentTokenConnection(new FileInputStream("my-document.pdf"));

    // Create the PAdES service
    PAdESService padesService = new PAdESService(Collections.singletonList(new BouncyCastleProvider()));

    // Create the signature parameters
    CertificationPermission certificationPermission = new CertificationPermission(false, false, false, false, false, false, false, false, false, false, false, false);
    ++CertificationPermission.setIncludeRevocationInfo(certificationPermission, false);
    padesService.setCertificationPermission(certificationPermission);
    padesService.setSignDate(new Date());

    // Sign the document
    PDDocument document = PDDocument.load(new FileInputStream("my-document.pdf"));
    PDSignatureField signatureField = new PDSignatureField(document);
    PDSignatureAppearance signatureAppearance = new PDSignatureAppearance();
    signatureAppearance.setReason("I am signing this document");
    signatureAppearance.setLocation("My location");
    signatureField.setSignature(signatureAppearance);
    document.addSignature(signatureField);

    ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
    padesService.sign(documentTokenConnection, signatureTokenConnection, outputStream);

    // Save the signed document
    FileOutputStream fileOutputStream = new FileOutputStream("my-signed-document.pdf");
    fileOutputStream.write(outputStream.toByteArray());
    fileOutputStream.close();

    // Validate the signature
    SignedDocumentValidator validator = new SignedDocumentValidator();
    Reports reports = validator.validateDocument(new ByteArrayInputStream(outputStream.toByteArray()));
    if (reports.getSummary().isValid()) {
      System.out.println("The signature is valid.");
    } else {
      System.out.println("The signature is invalid.");
    }
  }
}
```