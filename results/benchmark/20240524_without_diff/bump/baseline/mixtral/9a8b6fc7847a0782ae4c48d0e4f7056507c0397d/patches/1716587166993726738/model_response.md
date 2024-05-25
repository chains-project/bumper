Here's a possible patch for the given code. It replaces the usage of `StrongPasswordEncryptor` with `BCryptPasswordEncoder`, which is a more common and widely-used implementation for password encoding in Spring Security.

```java
@Override
protected PasswordEncoder createStringEncoder() {
    BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
    return encoder;
}
```

This solution assumes that the `BCryptPasswordEncoder` class is available in the classpath. If it's not, you may need to add the appropriate dependency to your project's build configuration.

Note that I had to remove the line where you were setting the `PasswordEncryptor` on the `PasswordEncoder` instance since `BCryptPasswordEncoder` doesn't have such a method. The `BCryptPasswordEncoder` generates a salt automatically and includes it in the encoded password.