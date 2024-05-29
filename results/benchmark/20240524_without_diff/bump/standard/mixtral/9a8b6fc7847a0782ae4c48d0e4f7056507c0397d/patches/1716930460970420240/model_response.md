Here's a fixed version of the code that removes the usage of the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);`:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        // it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password); // removed
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

This code change removes the call to `SecurityUtils.scramble(password)` and keeps the call to `SecurityUtils.scramble(chars)` as it is. This should resolve the compilation error.