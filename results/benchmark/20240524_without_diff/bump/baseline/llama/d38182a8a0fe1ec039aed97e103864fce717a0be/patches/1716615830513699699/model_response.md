```java
public Slice slice(final String action) {
    Authentication.User alice = new Authentication.User(TestAuthentication.ALICE.name());
    Authentication.User bob = new Authentication.User(TestAuthentication.BOB.name());
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(
            token -> CompletableFuture.completedFuture(
                Stream.of(alice, bob)
                    .filter(user -> token.equals(token(user.getName())))
                    .findFirst()
            ),
            ""
        )
    );
}
```