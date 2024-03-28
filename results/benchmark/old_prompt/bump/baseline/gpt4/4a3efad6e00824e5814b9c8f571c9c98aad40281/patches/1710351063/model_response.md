The error message states that the symbol cannot be found. This could be due to a few reasons such as the library not being present, wrong import statement, or the library has been updated and the class or method no longer exists.

Since we cannot change the external dependency and the library methods, we can only change the client code. If the library has been updated and the class or method no longer exists, we need to find an alternative class or method that provides the same functionality.

However, without the knowledge of the library updates, it's hard to provide a specific solution. A general solution would be to comment out or remove the import statement and replace the usage of the `CertificationPermission` in the client code with an alternative.

Since the exact usage is not provided, here is a general way of how to do it:

```java
  // import eu.europa.esig.dss.pades.CertificationPermission;
  // Replace the CertificationPermission with an alternative.
```

Remember to replace the usage of `CertificationPermission` in the client code with the alternative.