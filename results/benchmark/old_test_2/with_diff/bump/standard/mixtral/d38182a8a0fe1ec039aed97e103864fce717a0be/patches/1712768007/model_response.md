Here is the fixed version of the failing method:

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
            (token) -> java.util.concurrent.CompletableFuture.completedFuture(
                java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new com.artipie.http.auth.AuthUser(user.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```

I changed the constructor of `com.artipie.http.auth.Permissions.Single` and `com.artipie.http.auth.Authentication.User` to use the new `com.artipie.http.auth.AuthUser` class. I also created a new `com.artipie.http.auth.AuthUser` instance for each user in the stream.