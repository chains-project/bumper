Here is the proposed patch for the failing client code:
```java
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.docker.http.DockerSlice(new com.artipie.docker.asto.AstoDocker(new com.artipie.asto.memory.InMemoryStorage()), new com.artipie.http.auth.Permissions.Single(new com.artipie.http.auth.AuthUser(TestAuthentication.ALICE.name(), action), action), new com.artipie.http.auth.BearerAuthScheme(( token) -> java.util.concurrent.CompletableFuture.completedFuture(java.util.stream.Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter(( user) -> token.equals(token(user))).map(( user) -> new com.artipie.http.auth.AuthUser(user.name(), user.name())).findFirst()), ""));
}
```
The changes made in this patch include:

* Replacing `com.artipie.http.auth.Authentication.Single` with `com.artipie.http.auth.Permissions.Single`
* Replacing `com.artipie.http.auth.Authentication.User` with `com.artipie.http.auth.AuthUser`
* Changing the constructor arguments for `com.artipie.http.auth.AuthUser` to match the new constructor signature
* Adding a second argument for the `AuthUser` constructor to match the new constructor signature

These changes should fix the "cannot find symbol" error by using the new `AuthUser` class instead of the removed `Authentication.User` class.