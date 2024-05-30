Here's the fixed version of the code that takes into account the changes in the new library version:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes include:

* Replace `org.jasypt.spring.security.PBEPasswordEncoder` with `org.jasypt.spring.security.PasswordEncoder`
* Replace `org.jasypt.spring.security.PBEPasswordEncoder.setPbeStringEncryptor` with `org.jasypt.spring.security.PasswordEncoder.setPbeStringEncryptor`
* Replace `org.jasypt.spring.security.PBEPasswordEncoder.encodePassword` with `org.jasypt.spring.security.PasswordEncoder.encodePassword`
* Replace `org.jasypt.spring.security.PBEPasswordEncoder.isPasswordValid` with `org.jasypt.spring.security.PasswordEncoder.isPasswordValid`