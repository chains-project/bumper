```java
  import eu.europa.esig.dss.pades.CertificationPermission;

  import java.util.ArrayList;
  import java.util.List;

  public class Signer {

      public List<CertificationPermission> getPermissions() {
          List<CertificationPermission> permissions = new ArrayList<>();
          permissions.add(CertificationPermission.ADD_SIGNATURE);
          permissions.add(CertificationPermission.REMOVE_SIGNATURE);
          permissions.add(CertificationPermission.ADD_CERTIFICATION);
          permissions.add(CertificationPermission.REMOVE_CERTIFICATION);
          permissions.add(CertificationPermission.ADD_REVOCATION);
          permissions.add(CertificationPermission.REMOVE_REVOCATION);
          permissions.add(CertificationPermission.ADD_OCSP);
          permissions.add(CertificationPermission.REMOVE_OCSP);
          permissions.add(CertificationPermission.ADD_OTHER);
          permissions.add(CertificationPermission.REMOVE_OTHER);
          return permissions;
      }
  }
```