Here's a possible patch for the failing client code:
```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new StandardPasswordEncoder();
    return encoder;
}
```
Note that this patch uses the `StandardPasswordEncoder` class from Spring Security instead of the `PasswordEncoder` class from Jasypt.
This is because the `PasswordEncoder` class from Jasypt is no longer available in the latest version of the library.
The `StandardPasswordEncoder` class from Spring Security provides similar functionality and should work as a drop-in replacement.