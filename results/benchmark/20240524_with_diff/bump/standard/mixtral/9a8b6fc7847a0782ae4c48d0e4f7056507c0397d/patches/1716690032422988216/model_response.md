Here is the updated `createStringEncoder` method that should resolve the error:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.util.text.TextEncryptor textEncryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        ((org.jasypt.encryption.pbe.PBEStringEncryptor) textEncryptor).setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            ((org.jasypt.encryption.pbe.PBEStringEncryptit.geosolutions.geostore.core.security.password.PBEPasswordEncoder) textEncryptor).setProviderName(getProviderName());
        }
        ((org.jasypt.encryption.pbe.PBEStringEncryptor) textEncryptor).setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setTextEncryptor(textEncryptor);
        return encoder;
   9} finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolution.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

This updated code uses the new `org.jasypt.util.text.TextEncryptor` interface instead of `org.jasypt.encryption.pbe.PBEStringEncryptor`. The `setTextEncryptor` method is used instead of `setPbeStringEncryptor` to configure the `PBEPasswordEncoder`.

Note that the cast `(org.jasypt.encryption.pbe.PBEStringEncryptor)` is used to access the specific methods of `PBEStringEncryptor`.