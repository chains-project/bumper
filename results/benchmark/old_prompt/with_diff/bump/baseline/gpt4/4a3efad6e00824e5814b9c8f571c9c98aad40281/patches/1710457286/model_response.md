The error message indicates that the class `CertificationPermission` cannot be found in the package `eu.europa.esig.dss.pades`. This problem may be caused by the removal or renaming of this class in the new version of the library. 

Without the details of the new library version, it's hard to provide a concrete solution. However, you can try to search for a similar class in the new library version, then replace `CertificationPermission` with the new class. 

For example, if the new version has a class named `CertificationPermissions`, you could replace the import statement like this:

```java
import eu.europa.esig.dss.pades.CertificationPermissions;
```

If the `CertificationPermission` class was removed without a replacement, you might need to restructure your code to not rely on it. This could be more complex and depend on how your code is using this class.