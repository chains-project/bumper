Here is a suggestion for a fix to the `createStringEncoder` method:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.util.text.TextEncryptor stringEncrypter = new org.jasypt.util.text.DefaultLazyPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setTextEncryptor(stringEncrypente);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

This fix uses the new `org.jasypt.util.text.TextEncryptor` interface to replace the `org.jasypt.encryption.pbe.PBEStringEncryptor` class that was removed. The `PBEPasswordEncoder` class has been updated to use the new `setTextEncryptor` method instead of the old `setPbeStringEncryptor` method.

I hope this helps! Let me know if you have any questions.