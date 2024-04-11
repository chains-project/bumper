Here's a possible patch for the failing method:
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
                    .filter((user) -> token.equals(token(user)))
                    .map((user) -> new com.artipie.http.auth.AuthUser(user.name(), ""))
                    .findFirst()
            ),
            ""
        )
    );
}
```
The main change is to replace `com.artipie.http.auth.Authentication.User` with `com.artipie.http.auth.AuthUser` in the `Permissions.Single` constructor, and also in the lambda function that creates the `AuthUser` instance from a `TestAuthentication` object.

Note that I had to make some assumptions about the `token` and `token` methods used in the lambda function, since they were not defined in the provided code. I assumed they are methods of the `TestAuthentication` class that take a `com.artipie.http.auth.AuthUser` object and return a `String` token. If this assumption is incorrect, you may need to adjust the lambda function accordingly.