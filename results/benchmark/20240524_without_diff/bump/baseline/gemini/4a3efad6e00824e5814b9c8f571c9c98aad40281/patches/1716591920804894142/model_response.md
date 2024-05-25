```java
  import eu.europa.esig.dss.pades.CertificationPermission;

  import java.io.IOException;
  import java.security.cert.X509Certificate;
  import java.util.List;

  import org.bouncycastle.cms.SignerInformation;
  import org.bouncycastle.tsp.TimeStampToken;

  import eu.europa.esig.dss.DSSDocument;
  import eu.europa.esig.dss.DSSException;
  import eu.europa.esig.dss.FileDocument;
  import eu.europa.esig.dss.SignatureLevel;
  import eu.europa.esig.dss.ToBeSigned;
  import eu.europa.esig.dss.pades.PAdESSignature;
  import eu.europa.esig.dss.pades.PAdESSignatureBuilder;
  import eu.europa.esig.dss.token.DSSPrivateKeyEntry;
  import eu.europa.esig.dss.token.MSCAPISignatureToken;
  import eu.europa.esig.dss.validation.CertificateVerifier;
  import eu.europa.esig.dss.validation.CommonCertificateVerifier;

  public class Signer {

      private static final String SIGNATURE_ALGORITHM = "SHA256withRSA";

      public static byte[] sign(byte[] document, DSSPrivateKeyEntry privateKeyEntry, X509Certificate certificate,
              List<X509Certificate> chain, TimeStampToken timeStampToken, CertificationPermission permission)
              throws IOException, DSSException {

          // Create the document to be signed
          DSSDocument toBeSignedDoc = new FileDocument(document);

          // Create the certificate verifier
          CertificateVerifier certificateVerifier = new CommonCertificateVerifier();

          // Create the signature builder
          PAdESSignatureBuilder signatureBuilder = new PAdESSignatureBuilder();
          signatureBuilder.withCertificate(certificate, chain);
          signatureBuilder.withSigningCertificate(certificate, chain);

          // Set the signature level
          signatureBuilder.withSignatureLevel(SignatureLevel.PAdES_BASELINE_B);

          // Set the signature algorithm
          signatureBuilder.withDigestAlgorithm(SIGNATURE_ALGORITHM);

          // Set the signing certificate
          signatureBuilder.withSigningCertificate(certificate, chain);

          // Set the certificate verifier
          signatureBuilder.withCertificateVerifier(certificateVerifier);

          // Set the time stamp token
          signatureBuilder.withTimeStampToken(timeStampToken);

          // Set the permission
          signatureBuilder.withCertificationPermission(permission);

          // Build the signature
          PAdESSignature signature = signatureBuilder.build(toBeSignedDoc);

          // Sign the document
          ToBeSigned dataToSign = signature.getToBeSigned();

          // Create the signature token
          MSCAPISignatureToken signatureToken = new MSCAPISignatureToken(privateKeyEntry);

          // Sign the data
          byte[] signatureValue = signatureToken.sign(dataToSign, null, SIGNATURE_ALGORITHM);

          // Complete the signature
          signature.sign(signatureValue);

          // Get the signed document
          DSSDocument signedDocument = signature.getSignedDocument();

          // Return the signed document
          return signedDocument.getDocument();
      }
  }
```