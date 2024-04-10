It seems that the error is caused by the removal of the `CertificationPermission` class in the new version of the library. To fix this error, you can replace the line:
```
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```
signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This imports the `CertificationPermission` enum from the `eu.europa.esig.dss.enumerations` package, which is not removed in the new version of the library.

Here's the full patch:
```
---

### org.openpdfsign.Signer.java

72,43 // cannot find symbol
72,43 // cannot find symbol

---

### org.openpdfsign.Signer.java

72,43 // cannot find symbol
72,43 // cannot find symbol

---

### eu.europa.esig.dss.enumerations

1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import


---

### org.openpdfsign.Signer.java

72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java

72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java

72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java

72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### eu.europa.esig.dss.enumerations
1234,12 // add import
1234,12 // add import

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### org.openpdfsign.Signer.java
72,43 // replace
72,43 // replace

---

### eu.europa..