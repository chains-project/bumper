```java
@Override
public Slice slice(final String action) {
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(user.name()))
                    .map(user -> new Authentication.User(user.name()))
                    .findFirst()
            ),
            ""
        )
    );
}
```