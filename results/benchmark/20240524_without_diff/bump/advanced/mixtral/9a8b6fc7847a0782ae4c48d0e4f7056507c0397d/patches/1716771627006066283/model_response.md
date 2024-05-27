Here's a fixed version of the `createStringEncoder` method that uses the Java 8 `StringPasswordEncoder` instead of the deprecated `StrongPasswordEncryptor`:
```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StringPasswordEncoder());
    return encoder;
}
```
Note that this code assumes that the `StringPasswordEncoder` class is available in the `org.jasypt.util.password` package. If that's not the case, you may need to adjust the package name accordingly.