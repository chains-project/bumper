Here's a fixed version of the code that uses the new `PasswordEncoder` interface from Spring Security 5.x and the `BCryptPasswordEncoder` implementation:
```java
@Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder();
    return encoder;
}
```
Note that this code uses the `org.springframework.security.crypto.password` package instead of `org.jasypt.spring.security`. This is because the `jasypt` library has been replaced by the built-in password hashing functionality in Spring Security 5.x.