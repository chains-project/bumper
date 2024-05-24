Here's the proposed patch to fix the error:

```java
import com.artipie.http.auth.AuthUser;

@Override
public Optional<AuthUser> user() {
    return Optional.of(new AuthUser("alice"));
}
```
The changes made are:

* Import the `AuthUser` class from the new `com.artipie.http.auth` package.
* Replace the `Authentication.User` class with the new `AuthUser` class.