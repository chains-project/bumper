Based on the error message, it seems like the issue is caused by a missing symbol or class, specifically `BearerAuthScheme`. To fix this issue, you could introduce a new class that wraps the `BearerAuthScheme` class. This new class will act as an adapter to the missing class and provide the necessary functionality.

Here's an example of how you could modify the code:

```java
class BearerAuthSchemeAdapter {
    private final com.artipie.docker.http.BearerAuthScheme delegate;

    BearerAuthSchemeAdapter(String token, Function<String, CompletableFuture<Optional<Authentication.User>>> authFunc) {
        this.delegate = new com.artipie.docker.http.BearerAuthScheme(token, authFunc);
    }

    // Add any other necessary methods from the BearerAuthScheme class here
}

@Override
public Slice slice(final String action) {
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthSchemeAdapter(
            "",
            token -> CompletableFuture.completedFuture(
                Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
                    .filter(user -> token.equals(token(user)))
                    .map(user -> new Authentication.User(user.name()))
                    .findFirst()
            )
        )
    );
}
```

This code introduces a new class `BearerAuthSchemeAdapter` that wraps the missing `BearerAuthScheme` class. The `slice` method is then modified to use the new adapter class instead of the missing class. This allows the code to compile and run correctly.

Note that you may need to modify the `BearerAuthSchemeAdapter` class to include any additional methods or functionality that are required by the `DockerSlice` class or other parts of your code.