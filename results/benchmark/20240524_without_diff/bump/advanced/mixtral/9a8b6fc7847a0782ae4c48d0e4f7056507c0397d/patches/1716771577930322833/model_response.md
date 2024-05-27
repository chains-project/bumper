Here's a fixed version of the code that uses the `BCryptPasswordEncoder` from Spring Security instead of the deprecated `StrongPasswordEncryptor` from Jasypt:
```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder());
    return encoder;
}
```
Note that you need to add the Spring Security dependency to your project if it's not already there.