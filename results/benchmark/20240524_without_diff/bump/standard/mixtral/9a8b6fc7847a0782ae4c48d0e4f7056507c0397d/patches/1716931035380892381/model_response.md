Here is a fixed version of the method that uses the `BCryptPasswordEncoder` from Spring Security instead of the `PasswordEncoder` from Jasypt:

```java
@Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder();
    return encoder;
}
```

This should fix the error by using a different library method that is still available. Note that this will change the way passwords are encoded, so make sure this is what you want.