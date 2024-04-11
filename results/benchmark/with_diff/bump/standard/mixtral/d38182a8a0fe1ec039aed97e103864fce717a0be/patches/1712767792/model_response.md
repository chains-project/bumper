Here's the fixed version of the failing method using the new library version:

```java
@Override
public com.artipie.http.Slice slice(final String action) {
    return new com.artipie.docker.http.DockerSlice(
        new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()),
        new com.artipie.http.auth.Permissions.Single(
            new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), ""),
            action
        ),
        new com.artipie.http.auth.BearerAuthScheme(
            (token) -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new com.artipie.http.auth.AuthUser(user.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```

The main change is the usage of `com.artipie.http.auth.AuthUser` instead of `com.artipie.http.auth.Authentication.User`. The `AuthUser` class has the same methods as the `User` class, but with a different constructor.