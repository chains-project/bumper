```java
@Override
public Slice slice(final String action) {
    final AuthenticationScheme scheme =
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new Authentication.User(user.name()))
                    .findFirst()
            ),
            ""
        );
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        scheme
    );
}
```