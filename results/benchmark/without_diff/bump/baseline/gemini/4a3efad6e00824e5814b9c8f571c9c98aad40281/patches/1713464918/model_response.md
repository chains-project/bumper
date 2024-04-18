```java
  import eu.europa.esig.dss.pades.CertificationPermission;
  import org.apache.pdfbox.pdmodel.PDDocument;
  import org.bouncycastle.cert.ocsp.OCSPResp;
  import org.openpdfsign.cert.CertificateHelper;
  import org.openpdfsign.cert.CertificateVerifier;
  import org.openpdfsign.cert.OCSPVerifier;
  import org.openpdfsign.cert.RevocationVerifier;
  import org.openpdfsign.cert.VerificationException;
  import org.openpdfsign.cert.VerificationResult;
  import org.openpdfsign.cert.VerificationResult.VerificationStatus;

  import java.io.IOException;
  import java.security.cert.X509Certificate;
  import java.util.Date;
  import java.util.List;

  /**
   * Verifies an existing PDF signature.
   *
   * @author <a href="mailto:thomas.wrobel@openpdfsign.org">Thomas Wrobel</a>
   *
   */
  public class Signer {

    // ...

    /**
     * Verifies the certificate chain of the given signer certificate.
     *
     * @param document
     *            the PDF document
     * @param signerCertificate
     *            the signer certificate
     * @param signingTime
     *            the signing time
     * @param certificationPermission
     *            the certification permission
     * @return a {@link VerificationResult}
     * @throws IOException
     *             if an I/O error occurs
     */
    public VerificationResult verifyCertificateChain(final PDDocument document, final X509Certificate signerCertificate,
        final Date signingTime, final CertificationPermission certificationPermission) throws IOException {
      // ...
      // Check if OCSP must be checked
      if (certificationPermission.isOcspCheck()) {
        // OCSP must be checked
        OCSPResp ocspResponse = null;
        // Check if OCSP response is in the signature
        if (signature.getOcspResponses() != null && !signature.getOcspResponses().isEmpty()) {
          // OCSP response is in the signature
          ocspResponse = signature.getOcspResponses().get(0);
        } else {
          // OCSP response is not in the signature
          // Try to get OCSP response from OCSP responder
          ocspResponse = OCSPVerifier.getOCSPResponse(signerCertificate);
        }
        // Check OCSP response
        if (ocspResponse != null) {
          // OCSP response is available
          boolean ocspValid = OCSPVerifier.verifyOCSPResponse(ocspResponse, signerCertificate, signingTime);
          if (ocspValid) {
            // OCSP response is valid
            result.setOcspVerified(true);
          } else {
            // OCSP response is invalid
            result.setOcspVerified(false);
            result.addVerificationMessage(VerificationStatus.UNVERIFIED_OCSP,
                "The OCSP response is invalid.");
          }
        } else {
          // OCSP response is not available
          result.setOcspVerified(false);
          result.addVerificationMessage(VerificationStatus.UNVERIFIED_OCSP,
              "No OCSP response is available.");
        }
      }
      // ...
    }

    // ...

  }
```