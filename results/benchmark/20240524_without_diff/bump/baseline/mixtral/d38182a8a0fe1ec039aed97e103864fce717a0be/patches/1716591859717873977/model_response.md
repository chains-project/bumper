Here is a possible patch for the failing code:

```java
import static java.util.stream.Collectors.toList;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Stream;

@Override
public Slice slice(final String action) {
    List<Authentication.User> users = Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB)
        .map(user -> new Authentication.User(user.name()))
        .collect(toList());
    Function<String, CompletableFuture<Authentication.User>> authScheme =
        token -> CompletableFuture.completedFuture(
            users.stream()
                .filter(user -> token.equals(token(user)))
                .findFirst()
                .orElse(null)
        );
    return new DockerSlice(
        new AstoDocker(new InMemoryStorage()),
        new Permissions.Single(TestAuthentication.ALICE.name(), action),
        new BearerAuthScheme(authScheme, "")
    );
}
```

This patch creates a list of `Authentication.User` objects from the `TestAuthentication` enum values, and uses it to implement the authentication scheme. This avoids the need to call `token()` on each `TestAuthentication` object, which may have been causing the "cannot find symbol" error.

Note that this patch assumes that the `BearerAuthScheme` constructor takes a `Function<String, CompletableFuture<Authentication.User>>` as its first argument. If this is not the case, you may need to adjust the patch accordingly.