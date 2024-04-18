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
                                    .orElseThrow(() -> new AssertionError("Authentication failed"))
                    ),
                    ""
            )
    );
}
```
The patch adds a `orElseThrow` method to the `BearerAuthScheme` constructor to provide a default authentication user if the token is not found. This should prevent the NPE that's causing the test to fail.

Note that the `token(user)` method is not shown in the code snippet provided, so I assume it's not relevant to the issue at hand. If it is relevant, please provide more context.