Here's a possible patch for the failing client code:
```java
@Override
public Slice slice(String action) {
    return new DockerSlice(new AstoDocker(new InMemoryStorage()), new Authentication.Single(new AuthUser(TestAuthentication.ALICE.name(), ""), action), new BearerAuthScheme((token) -> CompletableFuture.completedFuture(Stream.of(TestAuthentication.ALICE, TestAuthentication.BOB).filter((user) -> token.equals(token(user))).map((user) -> new AuthUser(user.name(), "")).findFirst()), ""));
}
```
The changes I made are:

* Replace `Authentication.Single` with `Authentication.Single(AuthUser, String)` constructor.
* Replace `Authentication.User` with `AuthUser` constructor.
* Replace `BearerAuthScheme`'s lambda argument type from `Authentication.User` to `AuthUser`.
* Add an empty string as the second argument for `AuthUser` constructor, since it now requires two arguments.

Note that these changes may not be sufficient if the code that uses the `slice` method has any dependencies on the removed `Authentication.User` class. In that case, further changes may be necessary.