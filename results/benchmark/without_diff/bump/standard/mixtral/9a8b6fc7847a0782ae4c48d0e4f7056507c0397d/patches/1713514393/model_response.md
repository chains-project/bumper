Here's the proposed patch:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = java.util.Base64.getDecoder().decode(new String(password).replace(" ", "+"));
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
        java.util.Arrays.fill(chars, '0');
        java.util.Arrays.fill(password, (byte) 0);
    }
}
```

This patch replaces the `toChars` method from the removed library with a Base64 decoding approach, and replaces the `scramble` method from the removed library with a character and byte array filling approach.