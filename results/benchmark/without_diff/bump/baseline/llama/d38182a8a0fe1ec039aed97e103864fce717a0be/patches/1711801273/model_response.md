Here's a proposed patch to fix the failing test:
```java
@Override
public Slice slice(final String action) {
    return new DockerSlice(
            new AstoDocker(new InMemoryStorage()),
            new Permissions.Single(TestAuthentication.ALICE.name(), action),
            new BearerAuthScheme(
                    token -> CompletableFuture.completedFuture(
                            Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                                    .filter(user -> token.equals(token(user)))
                                    .map(user -> new Authentication.User(user.name()))
                                    .findFirst()
                                    .orElseThrow(() -> new RuntimeException("Authentication failed"))
                    ),
                    ""
            )
    );
}
```
The patch adds a `orElseThrow` method to the `BearerAuthScheme` constructor to provide a default user when the `Stream.of` method doesn't find any matching user. This way, the `Authentication.User` object is not `null`, and the `AuthTest` class can run successfully.