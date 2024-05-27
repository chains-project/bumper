Here is the patched code:

```java
@java.lang.Override
public Optional<com.artipie.http.auth.AuthUser> user() {
    return java.util.Optional.of(new com.artipie.http.auth.AuthUser("alice"));
}
```