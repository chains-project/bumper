```java
@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    org.jasypt.util.password.StrongPasswordEncryptor passwordEncryptor = new org.jasypt.util.password.StrongPasswordEncryptor();
    encoder.setPasswordEncryptor(passwordEncryptor);
    return encoder;
}
```