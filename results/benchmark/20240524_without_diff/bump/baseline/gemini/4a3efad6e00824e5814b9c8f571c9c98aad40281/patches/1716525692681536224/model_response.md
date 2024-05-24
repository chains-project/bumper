```java
  import eu.europa.esig.dss.enumerations.CertificationPermission;
  import eu.europa.esig.dss.pades.PAdESSignatureParameters;

  public class Signer {

    public void sign(String filePath, String outputFilePath, String signatureAlgorithm, String signatureValue, String certificateChain, String tsaUrl, String tsaUsername, String tsaPassword, String signingCertificateAlias, String signingCertificatePassword, String reason, String location, String contactInfo, String signingTime, String policyId, String policyHash, String policyHashAlgorithm, String signatureProfile, CertificationPermission permission) throws Exception {
      // ...
      PAdESSignatureParameters parameters = new PAdESSignatureParameters();
      parameters.setPermission(permission);
      // ...
    }
  }
```