Here's a fixed version of the method using `java.util.Base64` to encode/decode the password:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPassword(Base64.getEncoder().encodeToString(password));
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
    }
}
```

This version replaces the `toChars` method call with a Base64 encoding of the password. It then sets the password of the `stringEncrypter` using the encoded password. Note that the `scramble` method call in the `finally` block has been left unchanged, but it may need to be updated to handle the new encoding.