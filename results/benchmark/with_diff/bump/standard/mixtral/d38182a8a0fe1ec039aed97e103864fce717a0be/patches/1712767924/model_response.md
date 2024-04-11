Here's the updated code that uses the new `AuthUser` class and other relevant changes from the new library version:

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
            token -> CompletableFuture.completedFuture(
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

The main changes include:

- Replacing `com.artipie.http.auth.Authentication.User` with `com.artipie.http.auth.AuthUser`
- Updating the constructor calls and methods accordingly
- Adding missing import statements as needed