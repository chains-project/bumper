I cannot directly access your codebase, but I can propose a patch for the failing method. Based on the error message, I assume the method looks similar to this:

```java
@Override
public void setCertificationPermission(CertificationPermission permission) {
    // existing code
}
```

Considering the changes in the new library version, it seems that the `CertificationPermission` class is no longer present in the `eu.europa.esig.dss.pades` package. Instead, you can use the `CertificationLevel` enum, which has been added to the `eu.europa.esig.dss.pades` package.

Here's the patched method:

```java
@Override
public void setCertificationPermission(eu.europa.esig.dss.pades.CertificationLevel permission) {
    // Adjust the existing code to work with the CertificationLevel enum
}
```

Note that you'll need to update the method parameter and the existing code accordingly.