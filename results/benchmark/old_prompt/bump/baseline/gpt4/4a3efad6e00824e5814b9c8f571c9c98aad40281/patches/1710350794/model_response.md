Based on the error message, it seems like the compiler is not able to find the `CertificationPermission` class in the `eu.europa.esig.dss.pades` package. This could be because the library that contains this package is not added in the classpath.

However, as per the constraints, we can only modify the client code and not the project configuration or dependencies. 

If the library has been updated and the `CertificationPermission` class has been moved to a different package or renamed, we should import the correct class. 

Unfortunately, without knowing the changes in the external library, it's not possible to provide a specific fix. 

But, generally, the solution would be to replace the import statement with the correct one. For example, if the `CertificationPermission` class has been moved to `eu.europa.esig.dss.newpackage` package, the fixed code would be:

```java
  import eu.europa.esig.dss.newpackage.CertificationPermission;
```

You should replace `newpackage` with the actual package name where `CertificationPermission` class is located in the new version of the library.