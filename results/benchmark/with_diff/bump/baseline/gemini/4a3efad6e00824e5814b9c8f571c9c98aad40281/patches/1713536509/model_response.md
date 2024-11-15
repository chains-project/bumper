```java
  import eu.europa.esig.dss.pades.PAdESService;

  import java.util.EnumSet;

  import org.bouncycastle.cms.CMSSignedDataGenerator;

  import static eu.europa.esig.dss.pades.PAdESService.PADES_B_LEVEL;

  public class Signer {

      public static byte[] sign(byte[] document, String signatureAlgorithm, String digestAlgorithm, String keystorePath, String keystorePassword, String keystoreAlias, String keystoreType, String providerName, String tsaUrl, String policyIdentifier, String signingCertificateChain, String ocspUrl, String crlUrl, String reason, String location, String contactInfo, String signingTime, String signatureProductionPlace, String signatureProductionCity, String signatureProductionCountry, String signatureProductionPostalCode, String signatureProductionStateOrProvince, String signatureProductionAddress, String signatureProductionDescription) throws Exception {
          PAdESService padesService = new PAdESService(new CMSSignedDataGenerator());
          padesService.setSignPolicy(PADES_B_LEVEL, policyIdentifier);
          padesService.setSignatureAlgorithm(signatureAlgorithm);
          padesService.setDigestAlgorithm(digestAlgorithm);
          padesService.setTSAUrl(tsaUrl);
          padesService.setSigningCertificateChain(signingCertificateChain);
          padesService.setOCSPUrl(ocspUrl);
          padesService.setCRLUrl(crlUrl);
          padesService.setReason(reason);
          padesService.setLocation(location);
          padesService.setContactInfo(contactInfo);
          padesService.setSigningTime(signingTime);
          padesService.setSignatureProductionPlace(signatureProductionPlace);
          padesService.setSignatureProductionCity(signatureProductionCity);
          padesService.setSignatureProductionCountry(signatureProductionCountry);
          padesService.setSignatureProductionPostalCode(signatureProductionPostalCode);
          padesService.setSignatureProductionStateOrProvince(signatureProductionStateOrProvince);
          padesService.setSignatureProductionAddress(signatureProductionAddress);
          padesService.setSignatureProductionDescription(signatureProductionDescription);

          return padesService.sign(document, keystorePath, keystorePassword, keystoreAlias, keystoreType, providerName, EnumSet.of(CertificationPermission.SIGN));
      }
  }
```