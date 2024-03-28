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
        org.springframework.security.crypto.password.Pbkdf2PasswordEncoder encoder = new org.springframework.security.crypto.password.Pbkdf2PasswordEncoder();
        encoder.setEncodeHashAsBase64(true);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```
This patch replaces the removed `PBEPasswordEncoder` with `Pbkdf2PasswordEncoder` from the `org.springframework.security.crypto.password` package. This encoder uses PBKDF2 (Password-Based Key Derivation Function 2), a key derivation function that is part of RSA Laboratories' Public-Key Cryptography Standards (PKCS) series, specifically PKCS #5 v2.0, also published as Internet Engineering Task Force's RFC 2898. It's a widely-used standard for password hashing.