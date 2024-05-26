Here's a fixed version of the `user()` method that uses the fully qualified name for the `User` class:

```java
@java.lang.Override
public Optional<com.artipie.http.auth.Authentication.User> user() {
    return java.util.Optional.of(new com.artipie.http.auth.Authentication.User("alice"));
}
```

This should resolve the "cannot find symbol" error you were seeing.