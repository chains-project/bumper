```java
  import eu.europa.esig.dss.pades.CertificationPermission;
  import eu.europa.esig.dss.pades.PadesSigner;

  public class Signer {
    public static void main(String[] args) {
      PadesSigner signer = new PadesSigner();
      signer.setCertificationPermission(CertificationPermission.SIGN);
    }
  }
```