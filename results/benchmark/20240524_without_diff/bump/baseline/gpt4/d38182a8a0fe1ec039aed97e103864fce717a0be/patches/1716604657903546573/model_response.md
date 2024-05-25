```java
@Override
public Slice slice(final String action) {
    Function<String, CompletionStage<Optional<Authentication.User>>> auth = token -> CompletableFuture.completedFuture(
        Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
            .filter(user -> token.equals(user.token()))
            .map(user -> new Authentication.User(user.name()))
            .findFirst()
    );
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(auth, "")
    );
}
```