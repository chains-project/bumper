```java
@java.lang.Override
protected it.geosolutions.geostore.core.security.password.PasswordEncoder createStringEncoder() {
    it.geosolutions.geostore.core.security.password.PasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PasswordEncoder();
    // The setPasswordEncryptor method was removed from the library.
    // encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```