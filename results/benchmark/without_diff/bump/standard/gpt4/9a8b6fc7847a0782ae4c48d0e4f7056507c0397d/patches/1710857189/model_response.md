The error message indicates that the symbol (method, variable, or class) used in the code was not found. The error is at line 103, column 36. The error could be due to a missing library or the method might have been removed or renamed in the updated version of the dependency.

The failing code does not have line numbers, so it's not clear exactly where the error is. However, from the error message, it seems that the error is related to the `setPasswordCharArray` method, which may have been removed or renamed.

Here is a proposed patch:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPassword(new String(chars)); // Changed line
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

In this patch, I replaced `setPasswordCharArray(chars)` with `setPassword(new String(chars))`. This change is based on the assumption that the `setPasswordCharArray` method has been removed or renamed and that the `setPassword` method is an appropriate replacement. If this assumption is incorrect, a different solution will be needed.