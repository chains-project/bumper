Here's a possible patch for the failing client code:
```java
import static java.util.Collections.singletonList;
import static java.util.stream.Collectors.toList;

@Override
public Slice slice(final String action) {
    AuthScheme authScheme = new BearerAuthScheme(
        token -> CompletableFuture.completedFuture(
            getUserFromToken(token, singletonList(TestAuthentication.ALICE, TestAuthentication.BOB))
        ),
        ""
    );
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        authScheme
    );
}

private Authentication.User getUserFromToken(String token, List<TestAuthentication> users) {
    return users.stream()
        .filter(user -> token.equals(token(user)))
        .map(TestAuthentication::name)
        .map(Authentication.User::new)
        .findFirst()
        .orElseThrow(() -> new RuntimeException("Invalid token"));
}
```
In this patch, we've added a new private method `getUserFromToken` that takes a token and a list of users as input, and returns the `Authentication.User` corresponding to the token. We've also simplified the `slice` method by using the `getUserFromToken` method and the `AuthScheme` constructor directly.

Note that the `singletonList` and `toList` methods are added library methods identified with `++`. If these methods are not available in your version of Java, you can replace them with your own implementation.