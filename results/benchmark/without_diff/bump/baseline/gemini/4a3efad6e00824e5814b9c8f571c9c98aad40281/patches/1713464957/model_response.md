```java
  import eu.europa.esig.dss.pades.CertificationPermission;
  import eu.europa.esig.dss.pades.PAdESSignatureParameters;
  import eu.europa.esig.dss.pades.signature.PAdESService;
  import eu.europa.esig.dss.token.DSSPrivateKeyEntry;
  import eu.europa.esig.dss.validation.reports.Reports;
  import org.apache.pdfbox.pdmodel.PDDocument;
  import org.apache.pdfbox.pdmodel.interactive.digitalsignature.PDSignature;
  import org.apache.pdfbox.pdmodel.interactive.digitalsignature.SignatureInterface;
  import org.openpdfsign.Signature;
  import org.openpdfsign.SignatureOptions;

  import java.io.IOException;
  import java.io.InputStream;
  import java.io.OutputStream;
  import java.security.cert.X509Certificate;

  public class Signer implements SignatureInterface {
      private final DSSPrivateKeyEntry privateKeyEntry;
      private final X509Certificate certificate;
      private final String reason;
      private final String location;
      private final SignatureOptions options;

      public Signer(DSSPrivateKeyEntry privateKeyEntry, X509Certificate certificate, String reason, String location, SignatureOptions options) {
          this.privateKeyEntry = privateKeyEntry;
          this.certificate = certificate;
          this.reason = reason;
          this.location = location;
          this.options = options;
      }

      @Override
      public void sign(InputStream content, OutputStream output) throws IOException {
          try (PDDocument document = PDDocument.load(content)) {
              PDSignature signature = new PDSignature();
              signature.setFilter(PDSignature.FILTER_ADOBE_PPKMS);
              signature.setSubFilter(PDSignature.SUBFILTER_ADBE_PKCS7_DETACHED);
              signature.setName(certificate.getSubjectDN().getName());
              signature.setLocation(location);
              signature.setReason(reason);
              signature.setSignDate(options.getSigningDate());

              PAdESSignatureParameters parameters = new PAdESSignatureParameters();
              parameters.setSigningCertificate(certificate);
              parameters.setBouncyCastleProvider(options.getProvider());
              parameters.setExternalSigningCertificate(options.getExternalSigningCertificate());
              parameters.setIncludeOnlySigningCertificate(options.isIncludeOnlySigningCertificate());
              parameters.setSignatureLevel(options.getSignatureLevel());
              parameters.setSignaturePackaging(options.getSignaturePackaging());
              parameters.setDigestAlgorithm(options.getDigestAlgorithm());
              parameters.setIncludeCertificateValues(options.isIncludeCertificateValues());
              parameters.setIncludeRevocationValues(options.isIncludeRevocationValues());
              parameters.setCommitmentTypeIndications(options.getCommitmentTypeIndications());
              parameters.setSigningTime(options.getSigningTime());
              parameters.setIncludeTimestamp(options.isIncludeTimestamp());
              parameters.setIncludeOnlyWholeObjectDigest(options.isIncludeOnlyWholeObjectDigest());
              parameters.setIncludePolicyOnlyHash(options.isIncludePolicyOnlyHash());
              parameters.setIncludeCommitmentTypeIndications(options.isIncludeCommitmentTypeIndications());
              parameters.setIncludeSignaturePolicyIdentifier(options.isIncludeSignaturePolicyIdentifier());
              parameters.setIncludeAcroFields(options.isIncludeAcroFields());
              parameters.setIncludeOCSPResponses(options.isIncludeOCSPResponses());
              parameters.setIncludeCRLValues(options.isIncludeCRLValues());
              parameters.setSignaturePolicyId(options.getSignaturePolicyId());
              parameters.setSignaturePolicyHash(options.getSignaturePolicyHash());
              parameters.setSignaturePolicyQualifiers(options.getSignaturePolicyQualifiers());
              parameters.setSignaturePolicyIdentifier(options.getSignaturePolicyIdentifier());
              parameters.setExternalDSSDigestAlgorithm(options.getExternalDSSDigestAlgorithm());
              parameters.setExternalSignatureLevel(options.getExternalSignatureLevel());
              parameters.setExternalSignaturePackaging(options.getExternalSignaturePackaging());
              parameters.setExternalIncludeCertificateValues(options.isExternalIncludeCertificateValues());
              parameters.setExternalIncludeRevocationValues(options.isExternalIncludeRevocationValues());
              parameters.setExternalCommitmentTypeIndications(options.getExternalCommitmentTypeIndications());
              parameters.setExternalSigningTime(options.getExternalSigningTime());
              parameters.setExternalIncludeTimestamp(options.isExternalIncludeTimestamp());
              parameters.setExternalIncludeOnlyWholeObjectDigest(options.isExternalIncludeOnlyWholeObjectDigest());
              parameters.setExternalIncludePolicyOnlyHash(options.isExternalIncludePolicyOnlyHash());
              parameters.setExternalIncludeCommitmentTypeIndications(options.isExternalIncludeCommitmentTypeIndications());
              parameters.setExternalIncludeSignaturePolicyIdentifier(options.isExternalIncludeSignaturePolicyIdentifier());
              parameters.setExternalIncludeAcroFields(options.isExternalIncludeAcroFields());
              parameters.setExternalIncludeOCSPResponses(options.isExternalIncludeOCSPResponses());
              parameters.setExternalIncludeCRLValues(options.isExternalIncludeCRLValues());
              parameters.setExternalSignaturePolicyId(options.getExternalSignaturePolicyId());
              parameters.setExternalSignaturePolicyHash(options.getExternalSignaturePolicyHash());
              parameters.setExternalSignaturePolicyQualifiers(options.getExternalSignaturePolicyQualifiers());
              parameters.setExternalSignaturePolicyIdentifier(options.getExternalSignaturePolicyIdentifier());
              parameters.setExternalIncludeOnlySigningCertificate(options.isExternalIncludeOnlySigningCertificate());
              parameters.setExternalIncludeCertificateRevocationLists(options.isExternalIncludeCertificateRevocationLists());
              parameters.setExternalIncludeAttributeCertificateRevocationLists(options.isExternalIncludeAttributeCertificateRevocationLists());
              parameters.setExternalIncludeCertificateValues(options.isExternalIncludeCertificateValues());
              parameters.setExternalIncludeRevocationValues(options.isExternalIncludeRevocationValues());
              parameters.setExternalIncludeOnlyWholeObjectDigest(options.isExternalIncludeOnlyWholeObjectDigest());
              parameters.setExternalIncludePolicyOnlyHash(options.isExternalIncludePolicyOnlyHash());
              parameters.setExternalIncludeCommitmentTypeIndications(options.isExternalIncludeCommitmentTypeIndications());
              parameters.setExternalIncludeSignaturePolicyIdentifier(options.isExternalIncludeSignaturePolicyIdentifier());
              parameters.setExternalIncludeAcroFields(options.isExternalIncludeAcroFields());
              parameters.setExternalIncludeOCSPResponses(options.isExternalIncludeOCSPResponses());
              parameters.setExternalIncludeCRLValues(options.isExternalIncludeCRLValues());
              parameters.setExternalIncludeOnlySigningCertificate(options.isExternalIncludeOnlySigningCertificate());
              parameters.setExternalIncludeCertificateRevocationLists(options.isExternalIncludeCertificateRevocationLists());
              parameters.setExternalIncludeAttributeCertificateRevocationLists(options.isExternalIncludeAttributeCertificateRevocationLists());
              parameters.setExternalSignaturePolicyId(options.getExternalSignaturePolicyId());
              parameters.setExternalSignaturePolicyHash(options.getExternalSignaturePolicyHash());
              parameters.setExternalSignaturePolicyQualifiers(options.getExternalSignaturePolicyQualifiers());
              parameters.setExternalSignaturePolicyIdentifier(options.getExternalSignaturePolicyIdentifier());
              parameters.setExternalSigningTime(options.getExternalSigningTime());
              parameters.setExternalIncludeTimestamp(options.isExternalIncludeTimestamp());
              parameters.setExternalIncludeOnlyWholeObjectDigest(options.isExternalIncludeOnlyWholeObjectDigest());
              parameters.setExternalIncludePolicyOnlyHash(options.isExternalIncludePolicyOnlyHash());
              parameters.setExternalIncludeCommitmentTypeIndications(options.isExternalIncludeCommitmentTypeIndications());
              parameters.setExternalIncludeSignaturePolicyIdentifier(options.isExternalIncludeSignaturePolicyIdentifier());
              parameters.setExternalIncludeAcroFields(options.isExternalIncludeAcroFields());
              parameters.setExternalIncludeOCSPResponses(options.isExternalIncludeOCSPResponses());
              parameters.setExternalIncludeCRLValues(options.isExternalIncludeCRLValues());
              parameters.setExternalIncludeOnlySigningCertificate(options.isExternalIncludeOnlySigningCertificate());
              parameters.setExternalIncludeCertificateRevocationLists(options.isExternalIncludeCertificateRevocationLists());
              parameters.setExternalIncludeAttributeCertificateRevocationLists(options.isExternalIncludeAttributeCertificateRevocationLists());
              parameters.setExternalSignaturePolicyId(options.getExternalSignaturePolicyId());
              parameters.setExternalSignaturePolicyHash(options.getExternalSignaturePolicyHash());
              parameters.setExternalSignaturePolicyQualifiers(options.getExternalSignaturePolicyQualifiers());
              parameters.setExternalSignaturePolicyIdentifier(options.getExternalSignaturePolicyIdentifier());
              parameters.setExternalIncludeTimestamp(options.isExternalIncludeTimestamp());
              parameters.setExternalIncludeOnlyWholeObjectDigest(options.isExternalIncludeOnlyWholeObjectDigest());
              parameters.setExternalIncludePolicyOnlyHash(options.isExternalIncludePolicyOnlyHash());
              parameters.setExternalIncludeCommitmentTypeIndications(options.isExternalIncludeCommitmentTypeIndications());
              parameters.setExternalIncludeSignaturePolicyIdentifier(options.isExternalIncludeSignaturePolicyIdentifier());
              parameters.setExternalIncludeAcroFields(options.isExternalIncludeAcroFields());
              parameters.setExternalIncludeOCSPResponses(options.isExternalIncludeOCSPResponses());
              parameters.setExternalIncludeCRLValues(options.isExternalIncludeCRLValues());
              parameters.setExternalIncludeOnlySigningCertificate(options.isExternalIncludeOnlySigningCertificate());
              parameters.setExternalIncludeCertificateRevocationLists(options.isExternalIncludeCertificateRevocationLists());
              parameters.setExternalIncludeAttributeCertificateRevocationLists(options.isExternalIncludeAttributeCertificateRevocationLists());
              parameters.setExternalSignaturePolicyId(options.getExternalSignaturePolicyId());
              parameters.setExternalSignaturePolicyHash(options.getExternalSignaturePolicyHash());
              parameters.setExternalSignaturePolicyQualifiers(options.getExternalSignaturePolicyQualifiers());
              parameters.setExternalSignaturePolicyIdentifier(options.getExternalSignaturePolicyIdentifier());
              parameters.setExternalIncludeOnlyWholeObjectDigest(options.isExternalIncludeOnlyWholeObjectDigest());
              parameters.setExternalIncludePolicyOnlyHash(options.isExternalIncludePolicyOnlyHash());
              parameters.setExternalIncludeCommitmentTypeIndications(options.isExternalIncludeCommitmentTypeIndications());
              parameters.setExternalIncludeSignaturePolicyIdentifier(options.isExternalIncludeSignaturePolicyIdentifier());
              parameters.setExternalIncludeAcroFields(options.isExternalIncludeAcroFields());
              parameters.setExternalIncludeOCSPResponses(options.isExternalIncludeOCSPResponses());
              parameters.setExternalIncludeCRLValues(options.isExternalIncludeCRLValues());
              parameters.setExternalIncludeOnlySigningCertificate(options.isExternalIncludeOnlySigningCertificate());
              parameters.setExternalIncludeCertificateRevocationLists(options.isExternalIncludeCertificateRevocationLists());
              parameters.setExternalIncludeAttributeCertificateRevocationLists(options.isExternalIncludeAttributeCertificateRevocationLists());
              parameters.setExternalSignaturePolicyId(options.getExternalSignaturePolicyId());
              parameters.setExternalSignaturePolicyHash(options.getExternalSignaturePolicyHash());
              parameters.setExternalSignaturePolicyQualifiers(options.getExternalSignaturePolicyQualifiers());
              parameters.setExternalSignaturePolicyIdentifier(options.getExternalSignaturePolicyIdentifier());
              parameters.setExternalIncludeTimestamp(options.isExternalIncludeTimestamp());
              parameters.setExternalIncludeOnlyWholeObjectDigest(options.isExternalIncludeOnlyWholeObjectDigest());
              parameters.setExternalIncludePolicyOnlyHash(options.isExternalIncludePolicyOnlyHash());
              parameters.setExternalIncludeCommitmentTypeIndications(options.isExternalIncludeCommitmentTypeIndications());
              parameters.setExternalIncludeSignaturePolicyIdentifier(options.isExternalIncludeSignaturePolicyIdentifier());
              parameters.setExternalIncludeAcroFields(options.isExternalIncludeAcroFields());
              parameters.setExternalIncludeOCSPResponses(options.isExternalIncludeOCSPResponses());
              parameters.setExternalIncludeCRLValues(options.isExternalIncludeCRLValues());
              parameters.setExternalIncludeOnlySigningCertificate(options.isExternalIncludeOnlySigningCertificate());
              parameters.setExternalIncludeCertificateRevocationLists(options.isExternalIncludeCertificateRevocationLists());
              parameters.setExternalIncludeAttributeCertificateRevocationLists(options.isExternalIncludeAttributeCertificateRevocationLists());
              parameters.setExternalSignaturePolicyId(options.getExternalSignaturePolicyId());
              parameters.setExternalSignaturePolicyHash(options.getExternalSignaturePolicyHash());
              parameters.setExternalSignaturePolicyQualifiers(options.getExternalSignaturePolicyQualifiers());
              parameters.setExternalSignaturePolicyIdentifier(options.getExternalSignaturePolicyIdentifier());

              parameters.setSignaturePermission(CertificationPermission.ANNOTATIONS);

              Signature signatureObject = new Signature(privateKeyEntry, certificate, parameters);
              signatureObject.signDetached(document, signature);

              document.save(output);
          }
      }
  }
```