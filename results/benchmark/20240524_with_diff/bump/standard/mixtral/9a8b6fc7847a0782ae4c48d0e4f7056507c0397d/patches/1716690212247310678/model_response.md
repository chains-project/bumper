Here is the updated version of the `createStringEncoder` method that should work with the new version of the library:
```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.util.text.TextEncryptor textEncryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        textEncryptor.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            textEncrypt.setProviderName(getProviderName());
        }
        textEncrypt.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setTextEncryptor(textEncryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
This updated version uses the `TextEncryptor` class from the `org.jasypt.util.text` package instead of the `PBEStringEncryptor` class from the `org.jasypt.encryption.pbe` package. It also uses the `setTextEncryptor` method instead of the `setPbeStringEncryptor` method.

I hope this helps! Let me know if you have any other questions.